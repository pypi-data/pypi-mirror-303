import json
import os
import uuid

from loguru import logger

develop_mode = os.environ.get('BOOKING_DEVELOPMENT') == '1'


def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac


def clear_dict(d):
    """
    清除字典中的none值
    @param d:
    @return:
    """
    if not d:
        return None
    elif isinstance(d, list):
        return list(filter(lambda x: x is not None, map(clear_dict, d)))
    elif not isinstance(d, dict):
        return d
    else:
        r = dict(filter(lambda x: x[1], map(lambda x: (x[0], clear_dict(x[1])), d.items())))
        if not bool(r):
            return None
        return r


def is_json(ss):
    """
    判断是否json
    """
    try:
        return json.loads(ss)
    except:
        return


def get_guid():
    return uuid.uuid4().hex


def list_locate(lst, key, value):
    """
    返回list中指定key，value的记录
    """
    result = list(filter(lambda x: x.get(key) == value, lst))
    if result:
        return result[0]


def parse_cookies(cookies, name):
    tags = list(filter(lambda x: x['name'] == name, cookies))
    if tags:
        return tags[0]['value']
    else:
        return None


def parse_proxyid(proxy_id):
    if proxy_id:
        return {"server": f'http://{proxy_id.split("@")[1]}',
                "username": proxy_id.split('@')[0].split('//')[1].split(':')[0],
                "password": proxy_id.split('@')[0].split('//')[1].split(':')[1]}
    else:
        return None
