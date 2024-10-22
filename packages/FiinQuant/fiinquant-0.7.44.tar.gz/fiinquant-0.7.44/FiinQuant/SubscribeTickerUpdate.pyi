class SubscribeTickerUpdate:
    def __init__(self, access_token: str, ticker: str, callback: callable, by: str, from_date: str, wait_for_full_time_frame: bool) -> None:
        self.ticker: str
        self._stop: bool
    def start(self) -> None: ...
    def stop(self) -> None: ...


