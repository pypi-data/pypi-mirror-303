from sqlalchemy import inspect, DateTime
from dateutil import parser
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession as BaseSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
import asyncio
import aiomysql
from pg_environment import config as penv
from pg_mysql.define import *
from pg_common import log_info, log_error, SingletonBase, RuntimeException


__all__ = ("AsyncSession", "SADataSource", "SADataSourceManager", "BASE", "BASE_SHARD")


def _to_dict(self):
    _ret = {}
    _class = inspect(self.__class__)
    for _k in _class.columns.keys():
        _col = _class.columns[_k]
        if isinstance(_col.type, DateTime):
            _d = getattr(self, _k)
            if _d:
                _d = _d.isoformat()
            _ret[_k] = _d
        else:
            _ret[_k] = getattr(self, _k)
    return _ret


def _from_dict(self, _dict):
    _class = inspect(self.__class__)
    for _k in _class.columns.keys():
        _col = _class.columns[_k]
        if isinstance(_col.type, DateTime):
            _str_datetime = _dict[_k]
            if _str_datetime:
                _str_datetime = parser.parse(_str_datetime)
            setattr(self, _k, _str_datetime)
        else:
            setattr(self, _k, _dict[_k])


BASE = declarative_base()
BASE.to_dict = _to_dict
BASE.from_dict = _from_dict

BASE_SHARD = declarative_base()
BASE_SHARD.to_dict = _to_dict
BASE_SHARD.from_dict = _from_dict


class AsyncSession(BaseSession):
    async def execute(self, *args, **kwargs):
        auto_scalars = kwargs.pop('auto_scalars', True)
        result = await super().execute(*args, **kwargs)
        if auto_scalars and len(result.keys()) == 1:
            return result.scalars()
        return result


class SADataSource(object):
    def __init__(self, source_name):
        self.source_name = source_name
        self.session = None
        self.engine = None
        self.init_finished = False

    async def _create_database(self):
        _cfg_mysql = penv.get_conf(KEY_MYSQL)
        _cfg_source = _cfg_mysql[self.source_name]
        _conn = await aiomysql.connect(host=_cfg_source[KEY_MYSQL_HOST], port=_cfg_source[KEY_MYSQL_PORT],
                                       user=_cfg_source[KEY_MYSQL_USER], password=_cfg_source[KEY_MYSQL_PASSWORD],
                                       echo=penv.is_debug(), autocommit=True)
        async with _conn.cursor() as _cur:
            await _cur.execute("show databases;")
            _dbs = await _cur.fetchall()
            log_info(_dbs)
            if (_cfg_source[KEY_MYSQL_DATABASE], ) not in _dbs:
                _sql = f"create database if not exists {_cfg_source[KEY_MYSQL_DATABASE]} " \
                       "default character set utf8mb4 collate utf8mb4_unicode_ci;"
                await _cur.execute(_sql)
        _conn.close()

    async def db_init(self):
        while not self.init_finished:
            try:
                await self._create_database()
                self.init_finished = True
            except Exception as e:
                log_error(e)
                await asyncio.sleep(2)

        _cfg_mysql = penv.get_conf(KEY_MYSQL)
        _cfg_source = _cfg_mysql[self.source_name]

        _db_url = "mysql+aiomysql://%s:%s@%s:%s/%s?charset=utf8mb4" % (_cfg_source[KEY_MYSQL_USER],
                                                                       _cfg_source[KEY_MYSQL_PASSWORD],
                                                                       _cfg_source[KEY_MYSQL_HOST],
                                                                       _cfg_source[KEY_MYSQL_PORT],
                                                                       _cfg_source[KEY_MYSQL_DATABASE])
        log_info(_db_url)
        self.engine = create_async_engine(_db_url, echo=penv.is_debug(),
                                          pool_size=_cfg_source[KEY_MYSQL_POOL_SIZE],
                                          pool_pre_ping=True,
                                          max_overflow=_cfg_source[KEY_MYSQL_MAX_OVERFLOW])

        async with self.engine.begin() as conn:
            if _cfg_source[KEY_MYSQL_SHARD]:
                await conn.run_sync(BASE_SHARD.metadata.create_all)
            else:
                await conn.run_sync(BASE.metadata.create_all)

        self.session = sessionmaker(class_=AsyncSession,
                                    autoflush=False,
                                    autocommit=False,
                                    bind=self.engine)

    async def get_db_session(self)->AsyncSession:
        async with self.session() as session:
            yield session

    async def shutdown(self):
        await self.engine.dispose()


class _SADataSourceManager(SingletonBase):
    def __init__(self):
        self.datasource = {}

    async def init_datasource(self):
        _mysql_cfg = penv.get_conf(KEY_MYSQL)
        if not _mysql_cfg:
            raise RuntimeException("InitDataSource", "mysql configuration does not exist.")
        for _k, _v in _mysql_cfg.items():
            self.datasource[_k] = SADataSource(_k)
            await self.datasource[_k].db_init()

    def get_datasource(self, source_name):
        return self.datasource[source_name] if source_name in self.datasource else None

    async def shutdown(self):
        for _dc in self.datasource.values():
            await _dc.shutdown()


SADataSourceManager = _SADataSourceManager()
