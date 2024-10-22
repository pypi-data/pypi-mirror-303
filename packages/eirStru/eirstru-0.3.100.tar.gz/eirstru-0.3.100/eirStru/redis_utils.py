import uuid

from redis.asyncio import Redis,ConnectionPool


def new_redis(db, host, port=6079, password=None) -> Redis:
    r_pool = ConnectionPool(
        host=host,
        password=password,
        port=port,
        db=db,
        decode_responses=True)
    return Redis(connection_pool=r_pool)


async def acquire_lock(redis_clt: Redis, lock_name, lock_timeout=5):
    """
    param lock_name: 锁名称
    param acquire_timeout: 客户端获取锁的超时时间
    param lock_timeout: 锁过期时间, 超过这个时间锁自动释放
    """
    identifier = str(uuid.uuid4())

    # setnx(key, value) 只有 key 不存在情况下将 key 设置为 value 返回 True
    # 若 key 存在则不做任何动作,返回 False
    if await redis_clt.setnx(lock_name, identifier):
        await redis_clt.expire(lock_name, lock_timeout)  # 设置锁的过期时间，防止线程获取锁后崩溃导致死锁
        return identifier  # 返回锁唯一标识
    elif await redis_clt.ttl(lock_name) == -1:  # 当锁未被设置过期时间时，重新设置其过期时间
        await redis_clt.expire(lock_name, lock_timeout)
    return False  # 获取超时返回 False


async def release_lock(redis_clt: Redis, lock_name, lock_id):
    cur_value = await redis_clt.get(lock_name)
    if cur_value == lock_id:
        await redis_clt.delete(lock_name)
