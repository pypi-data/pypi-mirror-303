from pyqqq.utils.api_client import raise_for_status, send_request
from pyqqq.utils.logger import get_logger
from pyqqq.utils.singleton import singleton
import pyqqq.config as c
import asyncio
import os
import websockets
import json


logger = get_logger("realtime")


def get_all_last_trades():
    """
    모든 종목의 최근 체결 정보를 반환합니다.

    Returns:
        list:
        - dict:
            - chetime (str): 체결시간
            - sign (str): 전일대비구분
            - change (int): 전일대비가격
            - drate (float): 전일대비등락율
            - price (int): 체결가
            - opentime (str): 시가시간
            - open (int): 시가
            - hightime (str): 고가시간
            - high (int): 고가
            - lowtime (str): 저가시간
            - low (int): 저가
            - cgubun (str): 체결구분
            - cvolume (int): 체결량
            - volume (int): 누적거래량
            - value (int): 누적거래대금(백만)
            - mdvolume (int): 매도체결수량
            - mdchecnt (int): 매도체결건수
            - msvolume (int): 매수체결수량
            - mschecnt (int): 매수체결건수
            - cpower (float): 체결강도
            - offerho (int): 매도호가
            - bidho (int): 매수호가
            - status (str): 장정보
            - jnilvolume (int): 전일동시간대거래량
            - shcode (str): 종목코드

    """

    r = send_request("GET", f"{c.PYQQQ_API_URL}/domestic-stock/trades")
    raise_for_status(r)

    data = r.json()
    result = [data[k] for k in data.keys()]

    return result


@singleton
class TickEventListener:
    """
    틱 데이터를 실시간으로 구독하는 서버와 websocket으로 연결되오,
    원하는 조건이 충족되었을 때 콜백을 호출하는 클래스입니다.

    객체를 생성 후, start() 하면 웹소켓이 연결됩니다.
    start() 전, 후에 관계없이 append_event()로 이벤트를 추가할 수 있습니다.

    Args:
        client_id (str): 클라이언트 ID. 고유한 값이어야 합니다.
        url (str): 웹소켓 서버 주소. TICKEVENT_URL 환경변수로 설정할 수 있습니다.
        config (dict): 설정값
            event_add_delay (float): 이벤트 추가 딜레이 시간. 기본값은 1초입니다.
    """

    LOG_TAG = "[TickEventListener]"

    def __init__(self, client_id, url=None, config={}):
        self.ws_connected = False
        self.events = {}
        self.pending_events = []
        self.event_add_delay = 1.0
        self.health_ping_delay = 10
        self.retry_cnt = 0
        self.quit = False

        if 'event_add_delay' in config:
            self.event_add_delay = config['event_add_delay']

        if 'health_ping_delay' in config:
            self.health_ping_delay = config['health_ping_delay']

        if client_id is not None:
            api_key = os.getenv("PYQQQ_API_KEY") or ""
            self.client_id = client_id + api_key
        else:
            self.client_id = api_key

        self.url = url
        if self.url is None:
            self.url = os.getenv("TICKEVENT_URL") or c.PYQQQ_EVENT_WS_URL

    async def start(self):
        """
        틱데이터 이벤트 리스너를 시작합니다
        """
        self.tasks = [
            asyncio.create_task(self.process_events_appending()),
            asyncio.create_task(self.connect_ws()),
            asyncio.create_task(self.health_ping())
        ]

    async def stop(self):
        """
        틱데이터 이벤트 리스너를 종료합니다.
        """
        for t in self.tasks:
            t.cancel()

        await asyncio.gather(*self.tasks)

    async def connect_ws(self):
        """
        웹소켓 서버에 연결하여 틱데이터 이벤트를 수신합니다.
        """
        try:
            async with websockets.connect(self.url) as websocket:
                self.retry_cnt = 0
                self.ws_connected = True
                self.ws = websocket

                await self.register(websocket)

                try:
                    async for message in websocket:
                        logger.debug(f"{self.LOG_TAG}message: {message}")
                        self.handle_response(message)
                except websockets.exceptions.ConnectionClosed:
                    logger.info(f"{self.LOG_TAG}Connection closed")
                    await self.on_connect_failed()
        except Exception as e:
            logger.info(f"{self.LOG_TAG}Connection failed. error: {e}")
            await self.on_connect_failed()
        finally:
            self.ws_connected = False

    async def health_ping(self):
        """
        웹소켓 서버에 헬스체크를 보냅니다.
        """
        while not self.quit:
            if self.ws_connected:
                await self.ws.send(json.dumps({
                    "type": "ping",
                    "client_id": self.client_id
                }))
            await asyncio.sleep(self.health_ping_delay)

    async def on_connect_failed(self):
        self.ws_connected = False
        self.move_events_to_pending()
        self.retry_cnt += 1

        if self.retry_cnt <= 5:
            await asyncio.sleep(self.retry_cnt * 2)
            await self.connect_ws()
        else:
            self.quit = True

    def append_event(self, ticker, event_id, price, once, side, price_comparison, listen_callback):
        """
        사용자로부터 틱데이터 이벤트 추가 요청을 등록합니다. 즉시 처리되진 않습니다.
        """
        self.events[event_id] = TickEvent(ticker, self.client_id, event_id, price, once, side, price_comparison, listen_callback)
        self.pending_events.append(event_id)

    async def append_event_async(self, ticker, event_id, price, once, side, price_comparison, listen_callback):
        """
        사용자로부터 틱데이터 이벤트 추가 요청을 등록합니다. 비동기로 가능한 한 즉시 처리됩니다.
        """
        self.events[event_id] = TickEvent(ticker, self.client_id, event_id, price, once, side, price_comparison, listen_callback)
        await self.events[event_id].listen_tick_event(self.ws)

    async def remove_event(self, event_id):
        """
        사용자로부터 틱데이터 이벤트 제거 요청을 받아 처리합니다.
        """
        if event_id in self.events:
            await self.events[event_id].close_tick_event(self.ws)
            self.events[event_id].remove()

        if event_id in self.pending_events:
            self.pending_events.remove(event_id)

    async def process_events_appending(self):
        """
        사용자로부터 받았던 틱데이터 이벤트 요청을 모아서 처리합니다.
        """
        while True:
            if self.ws_connected:
                res = []
                cur_pending_events = list(self.pending_events)
                for pending_event_id in cur_pending_events:
                    if not self.events[pending_event_id].check_removed():
                        await self.events[pending_event_id].listen_tick_event(self.ws)
                        res.append(pending_event_id)
                    self.pending_events.remove(pending_event_id)

                logger.debug(f"{self.LOG_TAG}try connect events:{cur_pending_events}, connected: {res}")

            else:
                logger.debug(f"{self.LOG_TAG}not connected")
            await asyncio.sleep(self.event_add_delay)
            if self.quit:
                return

    def move_events_to_pending(self):
        self.pending_events = list(self.events.keys())

    async def register(self, ws):
        """
        서버에 유저를 등록합니다.
        """
        data = json.dumps({
            "type": "register",
            "client_id": self.client_id
        })
        logger.info(f"{self.LOG_TAG}registering. data:{data}")
        await ws.send(data)

    def handle_response(self, response):
        """
        서버로부터 받은 틱데이터 이벤트를 처리합니다.
        """
        data = json.loads(response)
        if "event_id" not in data:
            res_data = data["data"]
            if res_data["message"] == "pong":
                logger.debug(f"{self.LOG_TAG} pong response")
            return
        event_id = data["event_id"]
        if event_id in self.events:
            event = self.events[event_id]
            if event.check_removed():
                self.events.remove(event_id)
                return
            else:
                event.handle_tick_data(data)
        else:
            logger.warning(f"{self.LOG_TAG}event_id {event_id} not found")


class TickEvent:
    """
    TickEventListener 클래스에서 사용하는 틱데이터 이벤트 클래스입니다.
    """

    LOG_TAG = "[TickEvent]"

    def __init__(self, ticker, client_id, event_id, price, once, side, price_comparison, listen_callback):
        self.removed = False
        self.ticker = ticker
        self.client_id = client_id
        self.event_id = event_id
        self.price = price
        self.once = once
        self.side = side
        self.price_comparison = price_comparison
        self.listen_callback = listen_callback

    async def listen_tick_event(self, ws):
        logger.info(f"{self.LOG_TAG} listen {self.event_id}")
        self.removed = False
        await ws.send(json.dumps({
            "type": "subscribe",
            "ticker": self.ticker,
            "client_id": self.client_id,
            "event_id": self.event_id,
            "price": self.price,
            "once": self.once,
            "side": self.side,
            "price_comparison": self.price_comparison
        }))

    def handle_tick_data(self, data):
        if self.listen_callback:
            self.listen_callback(data)

        if self.once:
            self.remove()

    async def close_tick_event(self, ws):
        """
        서버에 틱데이터 이벤트 구독 해지 요청을 보낸 후 이벤트를 제거합니다.
        """
        logger.info(f"{self.LOG_TAG} close {self.event_id}")
        await ws.send(json.dumps({
            "type": "unsubscribe",
            "ticker": self.ticker,
            "client_id": self.client_id,
            "event_id": self.event_id,
        }))
        self.remove()

    def remove(self):
        self.removed = True

    def check_removed(self):
        return self.removed
