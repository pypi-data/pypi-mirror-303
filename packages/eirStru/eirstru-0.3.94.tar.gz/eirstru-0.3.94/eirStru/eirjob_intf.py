from aiohttp import ClientSession, ClientConnectorError

from eirStru import *


class EirOrderParams(BaseModel):
    session_data: Optional[SessionData] = None
    order: Optional[EirOrder] = None
    params: Optional[dict] = None


class JobIntf:
    def __init__(self, host):
        self.host = host

    async def do_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        return await self.call_eir_job('do_eir', session_data, order)

    async def get_bill_info(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        """
        获取提单信息
        """
        url = f'{self.host}/get_bill_info/'
        data = EirOrderParams(session_data=session_data, order=order)

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=data.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    if r_json.get('data'):
                        r_json['data'] = EirOrder(**r_json['data'])
                    return ResponseData(**r_json)
        except ClientConnectorError as e:
            return ResponseData(code=RespType.network_timeout_error, msg=f'获取提单信息失败，{order} {e}')
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'登录失败{order}:{e}')

    async def get_ctn_list(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('get_ctn_list', session_data, order)
        if resp.code == RespType.task_success and resp.data:
            resp.data = list(map(lambda x: CtnInfo(**x), resp.data))
        return resp

    async def cancel_eir_ctns(self, session_data: SessionData, order: EirOrder, ctn_ids) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        return await self.call_eir_job('cancel_eir_ctns', session_data, order, {"ctn_ids": ctn_ids})

    async def get_apply_cy(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        return await self.call_eir_job('get_apply_cy', session_data, order)

    async def apply_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('apply_eir', session_data, order)
        if resp.code == RespType.task_success and resp.data:
            try:
                resp.data = list(map(lambda x: CtnInfo(**x), resp.data))
            except Exception as e:
                logger.error(f'申请eir转换箱型出错{order} {resp.data} {e}')
                resp.data = []
        return resp

    async def get_qrcode(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('get_qrcode', session_data, order)
        return resp

    async def print_eir(self, session_data: SessionData, order: EirOrder) -> ResponseData:
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('print_eir', session_data, order)
        if resp.code == RespType.task_success and resp.data:
            try:
                resp.data = list(map(lambda x: CtnInfo(**x), resp.data))
            except Exception as e:
                logger.error(f'打印eir转换箱型出错{order} {resp.data} {e}')
                resp.data = []
        return resp

    async def download_eir(self, session_data: SessionData, order: EirOrder):
        if not order.booking_no:
            logger.error(f'{order} 没有 bookingno')
            return ResponseData(code=RespType.task_failed, msg=f'{order} 没有 bookingno')
        resp = await self.call_eir_job('download_eir', session_data, order)
        return resp

    async def call_eir_job(self, job_type, session_data: SessionData, order: EirOrder,
                           params: dict = None) -> ResponseData:
        url = f'{self.host}/{job_type}/'
        data = EirOrderParams(session_data=session_data, order=order, params=params)
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        data = data.model_dump_json()
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=data, verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{order}:{e}')

    async def quote_spot(self, params: SpotParams):
        url = f'{self.host}/quote_spot'
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }
        try:
            async with ClientSession() as cs:
                async with cs.post(url, headers=headers, data=params.model_dump_json(), verify_ssl=False) as resp:
                    r_json = await resp.json()
                    return ResponseData(**r_json)
        except Exception as e:
            return ResponseData(code=RespType.task_exception, msg=f'{e}')
