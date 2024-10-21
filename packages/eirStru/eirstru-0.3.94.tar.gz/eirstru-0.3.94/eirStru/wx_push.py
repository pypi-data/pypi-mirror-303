import json

import aiohttp
import httpx
from loguru import logger


class NotifyPush:
    def __init__(self):
        self.wx_template_msg_url = None
        self.wx_text_msg_url = None
        self.mail_server_url = None

    async def send_email_with_attachments(self, subject, body, recipient):

        data = {
            "subject": subject,
            "body": body,
            "recipient": recipient
        }

        # files = [
        #     ("files", ("ocr.png", open("ocr.png", "rb"))),
        #     ("files", ("requirements.txt", open("requirements.txt", "rb"))),
        # ]

        async with httpx.AsyncClient() as client:
            response = await client.post(self.mail_server_url, data=data)
            # response = await client.post(url, data=data, files=files)
            print(response.status_code)
            print(response.json())

    # 发送微信模版消息
    async def send_wx_template_msg(self, openid, data, template_id):
        param = {
            'template_id': template_id,
            'url': '',
            'topcolor': '#173177',
            'data': data}

        param_str = json.dumps(param)
        payload = {
            'weChatConfigId': '4544c916-0ee1-4d89-8c8d-10d21287334a',
            'openidList': openid,
            'msgJson': param_str

        }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.wx_template_msg_url, params=payload) as resp:
                    if resp.status in [200, 201]:
                        r_text = await resp.text()
                        logger.info(f'发送微信模版消息{openid} {data} {r_text}')
        except Exception as e:
            logger.error(f'发送微信文本消息{openid} {data} {e}')

    # 发送微信文本消息
    async def send_wx_text_msg(self, wx_id, text_msg):

        payload = json.dumps({
            "wxidorgid": wx_id,
            "msg": text_msg
        })
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.wx_text_msg_url, data=payload) as resp:
                    r_text = await resp.text()
                    logger.info(f'发送微信文本消息{wx_id} {text_msg} {r_text}')
        except Exception as e:
            logger.error(f'发送微信文本消息{wx_id} {text_msg} {e}')
