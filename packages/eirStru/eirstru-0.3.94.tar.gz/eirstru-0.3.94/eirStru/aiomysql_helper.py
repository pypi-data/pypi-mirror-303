import inspect
from typing import Any, Dict, List, Optional

import aiomysql

from loguru import logger


# 封装执行命令
async def execute(pool, sql, param=None):
    """
    【主要判断是否有参数和是否执行完就释放连接】
    :param pool:
    :param sql: 字符串类型，sql语句
    :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
    """
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                if param:
                    rec_count = await cur.execute(sql, param)
                else:
                    rec_count = await cur.execute(sql)
                await conn.commit()
                if rec_count == 0:
                    logger.info(f'sql未更新数据执行\n{sql}\n{param}')
                return rec_count
            except aiomysql.Error as e:
                await conn.rollback()
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]
                logger.error('mysql error %d: %s; %s' % (e.args[0], e.args[1], f_name))


async def select(pool, sql, param=None):
    """
    【主要判断是否有参数和是否执行完就释放连接】
    :param pool:
    :param sql: 字符串类型，sql语句
    :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
    """
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            try:
                if param:
                    await cur.execute(sql, param)
                else:
                    await cur.execute(sql)
                r = await cur.fetchall()
                return r
            except aiomysql.Error as e:
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]
                logger.error('mysql error %d: %s; %s' % (e.args[0], e.args[1], f_name))


async def selectone(pool, sql, param=None):
    """
    【主要判断是否有参数和是否执行完就释放连接】
    :param pool:
    :param sql: 字符串类型，sql语句
    :param param: sql语句中要替换的参数"select %s from tab where id=%s" 其中的%s就是参数
    """
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            try:
                if param:
                    await cur.execute(sql, param)
                else:
                    await cur.execute(sql)

                r = await cur.fetchall()
                if len(r) > 0:
                    return r[0]
                else:
                    return {}

            except aiomysql.Error as e:
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]

                logger.error('mysql error %d: %s; %s' % (e.args[0], e.args[1], f_name))
            # finally:
            #     logger.info(f'\n{sql}\n\t{param}')


async def selectvalue(pool, sql, param=None):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            try:
                if param:
                    await cur.execute(sql, param)
                else:
                    await cur.execute(sql)
                r = await cur.fetchall()
                if len(r) > 0:
                    result = r[0]
                else:
                    result = {}
                if result:
                    return list(result.values())[0]
            except aiomysql.Error as e:
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]

                logger.error('mysql error %d: %s; %s' % (e.args[0], e.args[1], f_name))


# 执行多条命令
async def executemany(pool, lis):
    """
    :param pool: 连接池
    :param lis: 是一个列表，里面放的是每个sql的字典'[{"sql":"xxx","param":"xx"}....]'
    :return:
    """
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                for order in lis:
                    sql = order['sql']
                    param = order['param']
                    if param:
                        await cur.execute(sql, param)
                    else:
                        await cur.execute(sql)
                await conn.commit()
            except aiomysql.Error as e:
                await conn.rollback()
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]

                logger.error('mysql error %d: %s; %s' % (e.args[0], e.args[1], f_name))
            # finally:
            #     logger.info(f'\n{sql}\n\t{param}')


# 增加
async def insertone(pool, sql, param):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            try:
                if param:
                    await cur.execute(sql, param)
                else:
                    await cur.execute(sql)
                insert_id = conn.insert_id()
                await conn.commit()
                return insert_id
            except aiomysql.Error as e:
                await conn.rollback()
                f_name = inspect.getframeinfo(inspect.currentframe().f_back)[2]

                logger.error('mysql error %d: %s,%s' % (e.args[0], e.args[1], f_name))
            # finally:
            #     logger.info(f'\n{sql}\n\t{param}')


class MysqlHelper:
    def __init__(self, database_set: Dict[str, Any]):
        self.database_set = database_set
        self._pool: Optional[aiomysql.Pool] = None

    @property
    async def pool(self) -> aiomysql.Pool:
        if self._pool is None:
            self._pool = await aiomysql.create_pool(
                host=self.database_set['host'],
                port=self.database_set['port'],
                user=self.database_set['user'],
                password=self.database_set['password'],
                db=self.database_set['db'],
                minsize=1,
                maxsize=10,
                autocommit=True
            )
        return self._pool

    async def execute(self, sql: str, param: Optional[Dict[str, Any]] = None) -> int:
        return await execute(await self.pool, sql, param)

    async def select(self, sql: str, param: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        return await select(await self.pool, sql, param)

    async def selectone(self, sql: str, param: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return await selectone(await self.pool, sql, param)

    async def selectvalue(self, sql: str, param: Optional[Dict[str, Any]] = None) -> Any:
        return await selectvalue(await self.pool, sql, param)

    async def executemany(self, lis: List[Dict[str, Any]]) -> None:
        await executemany(await self.pool, lis)

    async def insertone(self, sql: str, param: Optional[Dict[str, Any]] = None) -> int:
        return await insertone(await self.pool, sql, param)
