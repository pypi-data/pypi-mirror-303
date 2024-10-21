from pg_environment import config
import aiomysql
from pg_mysql.define import *
from pg_common import SingletonBase, log_info, RuntimeException


__all__ = ("Connection", "ConnectionManager")


class Connection(object):
    def __init__(self, source_name):
        self.source_name = source_name
        self.pool = None

    async def init(self):
        _mysql_cfg = config.get_conf(KEY_MYSQL)
        _cfg_source = _mysql_cfg[self.source_name]
        self.pool = await aiomysql.create_pool(
            echo=config.is_debug(),
            host=_cfg_source[KEY_MYSQL_HOST],
            port=_cfg_source[KEY_MYSQL_PORT],
            user=_cfg_source[KEY_MYSQL_USER],
            password=_cfg_source[KEY_MYSQL_PASSWORD],
            db=_cfg_source[KEY_MYSQL_DATABASE],
            minsize=_cfg_source[KEY_MYSQL_POOL_SIZE],
            maxsize=_cfg_source[KEY_MYSQL_POOL_SIZE] + _cfg_source[KEY_MYSQL_MAX_OVERFLOW]
        )

    async def __execute_sql(self, _sql, _select=True):
        log_info(f"execute sql: {_sql}")
        async with self.pool.acquire() as _conn:
            async with _conn.cursor(aiomysql.DictCursor) as _cur:
                await _cur.execute(_sql)
                if _select:
                    _ret = await _cur.fetchall()
                else:
                    _ret = _cur.rowcount
                return _ret

    async def select(self, _sql):
        return await self.__execute_sql(_sql)

    async def update(self, _sql):
        return await self.__execute_sql(_sql, _select=False)

    async def shutdown(self):
        self.pool.close()
        await self.pool.wait_closed()


class _ConnectionManager(SingletonBase):
    def __init__(self):
        self.connections = {}

    async def init_connections(self):
        _mysql_cfg = config.get_conf(KEY_MYSQL)
        if not _mysql_cfg:
            raise RuntimeException("InitConnections", f"mysql configuration does not exist.")
        for _k, _v in _mysql_cfg.items():
            self.connections[_k] = Connection(_k)
            await self.connections[_k].init()

    def get_connection(self, source_name: str):
        return self.connections[source_name] if source_name in self.connections else None

    async def shutdown(self):
        for _c in self.connections.values():
            await _c.shutdown()


ConnectionManager = _ConnectionManager()
