KEY_MYSQL = "mysql"
KEY_MYSQL_HOST = "host"
KEY_MYSQL_PORT = "port"
KEY_MYSQL_DATABASE = "database"
KEY_MYSQL_USER = "user"
KEY_MYSQL_PASSWORD = "password"
KEY_MYSQL_POOL_SIZE = "pool_size"
KEY_MYSQL_MAX_OVERFLOW = "max_overflow"
KEY_MYSQL_DEFAULT_KEY = "default"
KEY_MYSQL_SHARD = "shard"
"""
mysql configuration format
====
{
  "mysql": {
    "default": {
      "host": "dc.mysql.candyworks.cn",
      "port": 3306,
      "database": "room_fc",
      "user": "root",
      "password": "Abc123654",
      "pool_size": 1,
      "max_overflow": 5,
      "shard": false
    },
    "datasource_0": {
      "host": "dc.mysql.candyworks.cn",
      "port": 3306,
      "database": "room_0",
      "user": "root",
      "password": "Abc123654",
      "pool_size": 1,
      "max_overflow": 5,
      "shard": true
    },
    "datasource_1": {
      "host": "dc.mysql.candyworks.cn",
      "port": 3306,
      "database": "room_1",
      "user": "root",
      "password": "Abc123654",
      "pool_size": 1,
      "max_overflow": 5,
      "shard": true
    }
  }
}
"""