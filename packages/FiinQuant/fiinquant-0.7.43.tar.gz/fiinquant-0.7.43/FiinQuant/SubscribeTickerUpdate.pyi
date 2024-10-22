from datetime import datetime, timedelta

class SubscribeTickerUpdate:
    def __init__(self, access_token: str, ticker: str, callback: callable, 
                 by: str = '1M', 
                 from_date: str | datetime = datetime.now() - timedelta(days=30)) -> None:
        
        self.ticker: str
        self._stop: bool

    def start(self) -> None: ...
    
    def stop(self) -> None: ...


