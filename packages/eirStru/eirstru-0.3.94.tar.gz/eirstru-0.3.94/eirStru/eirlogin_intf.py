from aiohttp import ClientSession, ClientConnectorError

from eirStru import *


class LoginIntf:
    def __init__(self, host):
        self.host = host

    async def check_account_info(self, params: AccountInfo) -> ResponseData:
        """
        检查账号
        """
        url = f'{self.host}/check_account_info/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = params.model_dump_json()

        # try:
        #     resp = httpx.post(url, params=data, headers=headers, verify=False)
        #     r_json = resp.json()
        #     if r_json.get('data'):
        #         r_json['data'] = AccountInfo(**r_json['data'])
        #     return ResponseData(**r_json)
        # except Exception as e:
        #     logger.info(e)
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=data, verify_ssl=False) as resp:
                    r_json = await resp.json()
                    if r_json.get('data'):
                        r_json['data'] = AccountInfo(**r_json['data'])
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def login(self, params: AccountInfo) -> ResponseData:
        """
        检查账号
        """
        url = f'{self.host}/login/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = params.model_dump_json()

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=data, verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except ClientConnectorError as e:
            return ResponseData(code=RespType.network_timeout_error, msg=f'校验账号异常,登录服务器未启动')
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'校验账号异常,{params} {e}')

    async def get_session(self, carrier_id, action: ActionType, account: str = None, bookingagent_id: str = None,
                          sub_code: str = None) -> ResponseData:
        url = f'{self.host}/get_session/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        params = ParamsGetSession()
        params.carrier_id = carrier_id
        params.action = action
        params.account = account
        params.bookingagent_id = bookingagent_id
        params.sub_code = sub_code

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=params.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    if r_json.get('data'):
                        r_json['data'] = SessionData(**r_json['data'])
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def return_session(self, resp_type: RespType, session_data: SessionData) -> ResponseData:
        url = f'{self.host}/return_session/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        session_data.last_access_resp_type = resp_type
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=session_data.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def check_session_count(self, carrier_id, order_dict) -> ResponseData:
        url = f'{self.host}/check_session_count/'

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = {'carrier_id': carrier_id}

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, params=data, verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def get_session_summary(self, carrier_id) -> ResponseData:
        url = f'{self.host}/get_session_summary/'

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = {'carrier_id': carrier_id}

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, params=data, verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def get_session_by_guid(self, carrier_id, action: ActionType, session_guid) -> ResponseData:
        url = f'{self.host}/get_session_by_guid/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        params = ParamsGetSession(**{'carrier_id': carrier_id, 'action': action, 'session_guid': session_guid})

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=params.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')

    async def get_valid_sessions(self, carrier_id, action: ActionType) -> ResponseData:
        url = f'{self.host}/get_valid_sessions/'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        params = ParamsGetSession(**{'carrier_id': carrier_id, 'action': action})

        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=params.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')
