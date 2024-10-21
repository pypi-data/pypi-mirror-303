import re
import uuid
from datetime import datetime, timedelta, date
from enum import Enum
import hashlib
from typing import Optional, Any, List, Dict

from loguru import logger
from pydantic import BaseModel


class RespType(Enum):
    """
    调用返回类型
    """
    task_success = 1  # 任务成功执行，并得到预期结果
    task_normal = 0  # 任务执行
    task_failed = -1  # 任务执行失败
    task_delay = -2  # 任务任务需延迟执行，比如下一次执行时间5min后,加入redis控制
    task_stock_limit = -3  # 无库存
    task_stock_overload = -4  # 舱位已超
    task_exception = -10  # 执行出现异常
    session_invalid_user_pw = -11  # 无效用户名
    session_invalid_token = -21  # 无效token
    session_request_limit = -31  # 访问次数受限
    network_timeout_error = -41  # 代理服务器错误,或超时
    proxy_error = -42  # 代理服务器错误
    never_run = -51  # 未执行
    unknown = -52  # 未知


class SessionData(BaseModel):
    """
    session信息
    """
    session_guid: Optional[str] = None
    carrier_id: Optional[str] = None
    account: Optional[str] = None
    sub_code: Optional[str] = None
    org_code: Optional[str] = None
    bookingagent_id: Optional[str] = None
    proxy_id: Optional[str] = None
    data: dict = {}
    lock_id: Optional[str] = None  # 锁ID
    login_time: Optional[float] = None
    last_access_time: Optional[float] = None
    last_access_resp_type: Optional[RespType] = RespType.task_normal

    def __init__(self, **data: Any):
        super().__init__(**data)
        if not data.get('session_guid'):
            self.session_guid = uuid.uuid4().hex

    def __str__(self):
        return f'{self.carrier_id}-{self.account}-{self.sub_code}-{self.proxy_id}'

    @property
    def redis_session_key(self):
        return f'{self.carrier_id}-{self.account}-{self.sub_code}-{self.session_guid}'


# 调用返回类型
class ActionType(Enum):
    """
    动作类型
    """
    bill_info = 1  # 获取提单信息
    ctn_list = 2  # 获取集装箱列表
    apply_eir = 3  # 申请条码
    print_eir = 4  # 打印条码
    login = 5  # 登录
    check_valid = 10  # 检查提单有效性
    get_bill_id = 11  # 获取提单号
    get_vessel_info = 12  # 获取船名航次
    get_vessel_id = 13  # 获取航次ID
    set_vessel = 14  # 设置船名
    get_apply_yard = 15  # 获取推荐堆场
    cancel_eir = 16  # 取消条码


def get_f_time(action):
    if action == ActionType.bill_info:
        return 'last_bill_info_time'
    elif action == ActionType.ctn_list:
        return 'last_ctn_list_time'
    elif action == ActionType.apply_eir:
        return 'last_apply_eir_time'
    else:
        return 'last_print_eir_time'


class ResponseData(BaseModel):
    """
    响应类
    """
    code: Optional[RespType] = None
    msg: Optional[str] = ''
    data: Optional[Any] = None  # 转换后的数据
    response: Optional[Any] = None  # 原始响应
    action: Optional[ActionType] = None  # 动作类型
    source: Optional[Any] = None  # 原始对象
    session_data: Optional[Any] = None
    log: bool = True  # 是否打印日志

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if kwargs.get('source'):
            self.source = f"{kwargs.get('source')}"
        if kwargs.get('session_data'):
            self.session_data = f"{kwargs.get('session_data')}"
        long_txt = self.log_text()
        long_txt = f'\n{self.msg}' + f'\n{long_txt}' if long_txt else ''
        if self.code == RespType.task_failed and (self.msg or self.data or self.response):
            logger.error(long_txt)
        elif (self.msg or self.data or self.response) and self.log:
            if self.code == RespType.task_success and self.action in [ActionType.print_eir, ActionType.apply_eir]:
                logger.error(long_txt)
            elif self.code == RespType.task_success:
                logger.info(long_txt)
            else:
                logger.info(long_txt)

    def log_text(self):
        result = []
        if self.code:
            result.append(self.code.name)
        if self.data:
            result.append(f'{self.data}')
        if self.action:
            result.append(self.action.name)
        if self.source:
            result.append(f'{self.source}')
        if self.session_data:
            result.append(f'{self.session_data}')
        if self.response:
            result.append(f'{self.response}')
        return '\n'.join(result)


# 服务器返回消息类型
class RespTextType(BaseModel):
    code: Optional[RespType] = None
    resp_key: Optional[str] = None
    describe: Optional[str] = None


class EirTaskInfo(BaseModel):
    order_guid: Optional[str] = None
    carrier_id: Optional[str] = ''  # 船公司
    bookingagent_id: Optional[str] = ''  # 一代
    account: Optional[str] = ''  # 账号
    password: Optional[str] = ''  # 密码
    mobile: Optional[str] = ''  # 手机号码
    bill_no: Optional[str] = ''  # 提单号
    valid_code: Optional[str] = ''  # 校验码

    apply_ctntypedigit: Optional[str] = ''  # 需一次性申请的箱型箱量
    ctntype_id: Optional[str] = ''  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    cyname: Optional[str] = None  # 推荐堆场
    vessel: Optional[str] = None
    voyage: Optional[str] = None

    client_user: Optional[str] = ''  # 客户用户名
    client_user_openid: Optional[str] = ''  # 客户用户Openid用于推送

    callback_url: Optional[str] = ''  # 回调url
    notify_email: Optional[str] = ''

    begin_time: Optional[datetime] = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                                       '%Y-%m-%d %H:%M:%S')  # 刷箱开始时间
    end_time: Optional[datetime] = datetime.strptime(
        datetime.strftime(datetime.now() + timedelta(hours=4), '%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')  # 刷箱结束时间
    plan_amount: Optional[int] = 0  # 计划数 todo
    memo: Optional[str] = None  # 备注
    account_list: Optional[List[dict]] = []

    def __str__(self):
        return f'{self.carrier_id} {self.bill_no} {str(self.ctn_digit) + "*" if self.ctn_digit else ""} {self.ctntype_id if self.ctntype_id else ""}'


class CtnInfo(BaseModel):
    """
    集装箱信息
    """
    bill_no: Optional[str] = None  # 提单号
    ctn_id: Optional[str] = None  # 集装箱号
    ctntype_id: Optional[str] = None  # 箱型
    ctn_data: Optional[Any] = None  # 服务器返回的集装箱数据
    is_applied: Optional[bool] = None  # 是否已申请
    is_printed: Optional[bool] = None  # 是否已打印
    apply_account: Optional[str] = None  # 申请账号
    apply_data: Optional[Any] = None  # 申请返回数据
    barcode: Optional[str] = None  # 条码
    print_account: Optional[str] = None  # 打印账号
    print_data: Optional[Any] = None  # 打印返回数据


class CtnTypeDigit(BaseModel):
    """
    箱型箱量
    """
    ctntype_id: Optional[str] = None  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    ctn_digit_applied: Optional[int] = 0  # 已申请量
    ctn_digit_printed: Optional[int] = 0  # 已打印量
    ctn_digit_for_apply: Optional[int] = 0  # 可申请量，未申请
    ctn_digit_for_print: Optional[int] = 0  # 可打印量，已申请未打印
    ctn_digit_need_apply: Optional[int] = 0  # 总申请量,订单传过来的，
    ctn_list_count: Optional[int] = 0  # 集装箱列表量

    # 总申请量>0 本次需申请量=总申请量-已申请量, 总申请量=0 本次申请量=箱量-可打印量
    # 本次打印量=min(可打印量,箱量)
    def __str__(self):
        return f'{self.ctn_digit}x{self.ctntype_id.upper()}'


def convert_ctntype_tolist(ctntype_id, ctn_digit=1) -> List[CtnTypeDigit]:
    """
    将箱型箱量字符串1x20gp;2x40gp，转化为箱型箱量对象列表
    """
    ctntypedigit_list = []
    if not ctntype_id:
        return ctntypedigit_list

    ctntype_id = ctntype_id.upper()

    # 如果未输入箱量并且箱型不符合 1x20GP 这样的格式,将ctntypedigit_list清空
    if not ctn_digit and not re.search('[xX]', ctntype_id):
        return ctntypedigit_list

    if ctntype_id.find('X') != -1:
        for item in re.split(r'[;,]', ctntype_id):
            if item:
                lst = re.split(r'[xX]', item)
                ctntypedigit = CtnTypeDigit()
                if lst[0].isdigit():
                    ctntypedigit.ctntype_id = lst[1]
                    ctntypedigit.ctn_digit = int(lst[0])
                else:
                    ctntypedigit.ctntype_id = lst[0]
                    ctntypedigit.ctn_digit = int(lst[1])
                ctntypedigit_list.append(ctntypedigit)
    elif ctntype_id:
        ctntypedigit = CtnTypeDigit()
        ctntypedigit.ctntype_id = ctntype_id
        ctntypedigit.ctn_digit = ctn_digit
        ctntypedigit_list.append(ctntypedigit)
    return ctntypedigit_list


# 存到redis，需延后打印的eir
class EirOrderForPrint(BaseModel):
    order_guid: Optional[str] = None
    carrier_id: str  # 船公司
    account: str  # 账号
    bill_no: str  # 提单号
    ctn_ids: List[str] = []  # 集装箱列表
    stamp: Optional[float] = None  # 上一次执行打印的时间

    @property
    def key(self):
        return hashlib.md5(self.model_dump_json().encode('utf-8')).hexdigest()


class EirOrder(BaseModel):
    order_guid: Optional[str] = None

    carrier_id: Optional[Any] = None  # 船公司
    bill_no: Optional[Any] = None  # 提单号
    booking_no: Optional[Any] = None  # 订舱号
    cyname: Optional[str] = None  # 推荐堆场
    ctntype_id: Optional[str] = ''  # 箱型
    ctn_digit: Optional[int] = 0  # 箱量
    vessel: Optional[Any] = None  # 船名
    voyage: Optional[Any] = None  # 航次
    apply_ctntypedigit: Optional[str] = ''  # 需一次性申请的箱型箱量

    client_id: Optional[str] = None  # 客户编号
    client_user: Optional[str] = ''  # 客户用户名
    client_user_openid: Optional[str] = ''  # 客户用户Openid用于推送

    callback_url: Optional[str] = ''  # 回调url
    notify_email: Optional[str] = ''  # 通知邮件

    begin_time: Optional[datetime] = datetime.strptime(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'),
                                                       '%Y-%m-%d %H:%M:%S')  # 刷箱开始时间
    end_time: Optional[datetime] = datetime.strptime(
        datetime.strftime(datetime.now() + timedelta(hours=4), '%Y-%m-%d %H:%M:%S'),
        '%Y-%m-%d %H:%M:%S')  # 刷箱结束时间

    yard_info: Optional[Dict] = {}  # msk 推荐堆场，按箱型
    bookingagent_id: Optional[Any] = None  # 账号对应的订舱代理

    ctntypedigit_list: List[CtnTypeDigit] = []  # eir订单箱型箱量
    is_disabled: Optional[Any] = False  # 人工取消 or 任务失败
    is_released: Optional[Any] = False  # 是否已放箱，有些以申请为准，有些以打印为准
    is_completed: Optional[Any] = False  # 已完成
    is_inited: Optional[Any] = False  # 是否已初始化

    internal_ctns: List[CtnInfo] = []  # 集装箱列表
    timestamp: Optional[Any] = 0  # 上一次执行时间
    last_timestamp: Optional[Any] = 0  # 将上一次执行时间保存下来，下次执行如果碰到网络异常的情况，可以回到上次执行时间
    accounts: List[str] = []  # 匹配的账号
    must_refresh_ctns: bool = False  # 必须刷新集装箱列表
    memo1: Optional[str] = None  # 备注1

    def check_ctntype_id(self, ctntype_id, ctn_list: List[CtnInfo]):
        """
        检查箱型是否和集装箱列表的数据相匹配
        """
        # 集装箱列表中箱型集合
        set1 = set(map(lambda ctn: ctn.ctntype_id, ctn_list))

        # 将ctntype_id转化为箱型箱量结构
        ctntypedigit_list = convert_ctntype_tolist(ctntype_id)
        # ctntype_id对应的箱型集合
        set2 = set(map(lambda ctntypedigit: ctntypedigit.ctntype_id, ctntypedigit_list))

        # 如果2边都是单箱型，自动将ctntype_id转化为集装箱列表的箱型
        if len(set1) == 1 and len(set2) == 1:
            ctntype_id = ctntype_id.replace(list(set2)[0], list(set1)[0])
            return ResponseData(code=RespType.task_success, msg=f'{self} 箱型成功转化', data=ctntype_id)
        elif set2 - set1:
            return ResponseData(code=RespType.task_failed, msg=f'{self} 放舱列表中未找到对应箱型，请联系一代')
        else:
            return ResponseData(code=RespType.task_success, msg=f'{self} 箱型匹配', data=ctntype_id)

    def __str__(self):
        return f'{self.carrier_id} {self.bill_no}'

    @property
    def status(self):
        return f"申请量:{len(filter(lambda ctn: ctn.is_applied, self.ctns))} 打印量:{len(filter(lambda ctn: ctn.is_printed, self.ctns))}"

    @property
    def ctns(self) -> List[CtnInfo]:
        return self.internal_ctns

    @ctns.setter
    def ctns(self, value: List[CtnInfo]):
        """
        设置集装箱列表时，将箱型箱量重新计算一遍
        """
        self.internal_ctns = value
        ctntypedigit_dict = {}

        # 指定箱型箱量模式
        if self.ctntype_id:
            ctntypedigit_list = convert_ctntype_tolist(self.ctntype_id, self.ctn_digit)
            ctntypedigit_dict = {x.ctntype_id: x for x in ctntypedigit_list}

            # cma统一申请模式,更新各箱型 ctn_digit_need_apply
            if self.apply_ctntypedigit:
                apply_ctntypedigit_list = convert_ctntype_tolist(self.apply_ctntypedigit)
                for item in apply_ctntypedigit_list:
                    ctntypedigit = ctntypedigit_dict.get(item.ctntype_id)
                    if ctntypedigit:
                        ctntypedigit.ctn_digit_need_apply = item.ctn_digit
                    else:
                        ctntypedigit_dict.update({item.ctntype_id: item})

        # 更新各箱型已申请量、已打印量
        for ctn in value:
            ctntypedigit = ctntypedigit_dict.get(ctn.ctntype_id)
            if not ctntypedigit:
                ctntypedigit = CtnTypeDigit()
                ctntypedigit.ctntype_id = ctn.ctntype_id
                ctntypedigit_dict.update({ctn.ctntype_id: ctntypedigit})
            if ctn.is_applied:
                ctntypedigit.ctn_digit_applied += 1
            if ctn.is_printed:
                ctntypedigit.ctn_digit_printed += 1
            ctntypedigit.ctn_list_count += 1

        for item in ctntypedigit_dict.values():
            item.ctn_digit = item.ctn_digit or item.ctn_list_count

            # 本次打印量=min(已申请量-已打印量,箱量)
            item.ctn_digit_for_print = min(item.ctn_digit_applied - item.ctn_digit_printed, item.ctn_digit)

            # 非msk,cma;
            if self.carrier_id not in ['MSK-EIR', 'CMA-EIR']:
                # 非msk，cma因为有集装箱列表，所以只需考虑可申请数量
                max_apply_count = item.ctn_list_count - item.ctn_digit_applied
                item.ctn_digit_for_apply = min(item.ctn_digit, max_apply_count)
            elif item.ctn_digit_need_apply > item.ctn_digit_applied:
                # cma统一申请模式
                item.ctn_digit_for_apply = item.ctn_digit_need_apply - item.ctn_digit_applied
            elif item.ctn_digit > item.ctn_list_count:
                # msk模式  改成 计划量减去集装箱量；如果4个柜子，已经申请了2个，就有2条记录；如果再想申请一个，需要将计划数量改成3，这样计算得出还需要1个箱子
                item.ctn_digit_for_apply = item.ctn_digit - item.ctn_list_count
            else:
                item.ctn_digit_for_apply = 0
        self.ctntypedigit_list = list(ctntypedigit_dict.values())

    def check_completed(self):
        """
        不需要申请，不需要打印
        """
        return not (self.need_apply or self.need_print) and self.ctns and True

    def ctns_for_apply(self):
        """
        获得待申请集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        """
        if self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_apply:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and not x.is_applied,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_apply]
            return ctns
        else:
            return list(filter(lambda x: not x.is_applied, self.ctns))

    def ctns_for_print(self) -> List[CtnInfo]:
        """
        获得待打印集装箱清单，整单则返回所有，按箱型则返回该箱型实际需求量
        """
        if self.carrier_id == 'HPL-EIR':
            return self.ctns
        elif self.ctntypedigit_list:
            ctns = []
            for ctntypedigit in self.ctntypedigit_list:
                if ctntypedigit.ctn_digit_for_print:
                    ctn_list = list(
                        filter(lambda x: x.ctntype_id == ctntypedigit.ctntype_id and x.is_applied and not x.is_printed,
                               self.ctns))
                    ctns += ctn_list[:ctntypedigit.ctn_digit_for_print]
                return ctns
        else:
            return list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns))

    @property
    def need_apply(self):
        """
        判断本单是否需要申请
        """
        if self.ctntypedigit_list:
            return bool(list(filter(lambda x: x.ctn_digit_for_apply, self.ctntypedigit_list)))
        else:
            return bool(list(filter(lambda x: not x.is_applied, self.ctns)))

    @property
    def need_print(self):
        """
        判断本单是否需要打印,未打印的 大于 未申请的 大于 0
        """
        if self.ctntypedigit_list:
            return bool(list(filter(lambda x: x.ctn_digit_for_print, self.ctntypedigit_list)))
        else:
            return bool(list(filter(lambda x: x.is_applied and not x.is_printed, self.ctns)))

    def to_order_for_print(self, account) -> EirOrderForPrint:
        ctn_ids = list(map(lambda x: x.ctn_id, self.ctns_for_print()))
        return EirOrderForPrint(carrier_id=self.carrier_id, account=account, bill_no=self.bill_no, ctn_ids=ctn_ids)


class AccountInfo(BaseModel):
    carrier_id: Optional[str] = None  # 船公司
    account: Optional[str] = None  # 账号
    password: Optional[str] = None  # 密码
    mobile: Optional[str] = None  # 手机号
    bookingagent_id: Optional[str] = None  # 账号对应的代理
    info: dict = {}  # 其他信息，比如说可以存储密钥之类

    def __str__(self):
        return f'{self.carrier_id} {self.account}'


# 运价参数
class SpotParams(BaseModel):
    session_data: Optional[SessionData] = None
    carrier_id: Optional[str] = None
    from_port_id: Optional[str] = None  # 起运港
    to_port_id: Optional[str] = None  # 目的港
    ctntype_id: Optional[str] = None  # 箱型
    begin_time: Optional[datetime] = None
    end_time: Optional[datetime] = None


class QQParams(BaseModel):
    session_data: Optional[SessionData] = None
    carrier_id: Optional[str] = None
    from_port_id: Optional[str] = None  # 起运港
    to_port_id: Optional[str] = None  # 目的港
    container_group: str = "STANDARD"  # 箱型组
    valid_from: Optional[date] = None

    def __str__(self):
        return f"{self.carrier_id} {self.from_port_id} {self.to_port_id} {self.container_group} {self.valid_from}"


# 运价
class SpotData(BaseModel):
    carrier_id: Optional[str] = None
    from_port_id: Optional[str] = None  # 起运港
    to_port_id: Optional[str] = None  # 目的港
    ctntype_id: Optional[str] = None  # 箱型

    spot_id: Optional[str] = None  # spot_id
    vessel: Optional[str] = None  # 船名
    voyage: Optional[str] = None  # 航次
    carrier_line: Optional[str] = None  # 船公司航线
    etd: Optional[date] = None  # 开港日
    eta: Optional[date] = None  # 抵港日
    days: Optional[int] = None  # 航程
    cut_off_datetime: Optional[datetime] = None  # 截港日
    doc_closure_datetime: Optional[datetime] = None  # 截单日
    base_price: Optional[float] = None  # 运费
    total_price: Optional[float] = None  # 总运费
    spot_price: Optional[float] = None
    spot_total_price: Optional[float] = None
    last_base_price: Optional[float] = None
    last_spot_price: Optional[float] = None
    spot_info: Optional[dict] = None  # json数据
    spot_time: datetime = datetime.now()  # 报价时间
    carrier_account: Optional[str] = None


# 获得session参数
class ParamsGetSession(BaseModel):
    carrier_id: Optional[str] = None
    action: Optional[ActionType] = None
    account: Optional[str] = None
    bookingagent_id: Optional[str] = None
    sub_code: Optional[str] = None
    session_guid: Optional[str] = None


# 检查账号是否有效,调用参数
class ParamsCheckAccount(BaseModel):
    carrier_id: str = ''  # 船公司
    account: str = ''  # 账号
    password: str = ''  # 密码

    def __str__(self):
        return f'{self.carrier_id}/{self.account}'


# 登录参数
class LoginParams(BaseModel):
    carrier_id: str = ''  # 船公司
    account: str = ''  # 账号
    password: str = ''  # 密码
    proxy_id: Optional[str] = None

    def __str__(self):
        return f'{self.carrier_id}-{self.account} {self.proxy_id if self.proxy_id else ""}'


# 处理retry，引入的异常
class RespSessionException(Exception):
    def __init__(self, code, msg, detail=None):
        self.code = code
        self.msg = msg
        self.detail = detail

    def __str__(self):
        return f'\n{str(self.code)}\n{self.detail or self.msg}'


class RespProxyException(RespSessionException):
    pass


class RespNetworkException(RespSessionException):
    pass


async def find_keys(redis, pattern):
    cursor = '0'
    keys = []
    while cursor != 0:
        cursor, results = await redis.scan(cursor=cursor, match=pattern)
        keys.extend(results)
    return keys
