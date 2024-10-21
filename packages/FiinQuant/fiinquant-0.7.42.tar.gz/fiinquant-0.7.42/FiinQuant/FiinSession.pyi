from .FiinIndicator import FiinIndicator
from .SubscribeDerivativeEvents import SubscribeDerivativeEvents
from datetime import datetime
from .Aggregates import IndexBars, TickerBars, CoveredWarrantBars, DerivativeBars
from .SubscribeCoveredWarrantEvents import SubscribeCoveredWarrantEvents
from .SubscribeIndexEvents import SubscribeIndexEvents
from .SubscribeTickerEvents import SubscribeTickerEvents


class FiinSession:
    def __init__(self, username: str, password: str):...

    def login(self) -> FiinSession: ...
        
    def _is_valid_token(self) -> bool: ...
   
    def FiinIndicator(self) -> FiinIndicator: ...
    
    def IndexBars(self,ticker: str, by: str, from_date: str | datetime, 
                           to_date: str | datetime  = datetime.now(), multiplier: int = 1, limit: int = 1000) -> IndexBars:...
    
    def TickerBars(self,ticker: str, by: str, from_date: str | datetime, 
                           to_date: str | datetime = datetime.now(), multiplier: int = 1, limit: int = 1000) -> TickerBars:...
    
    def DerivativeBars(self,ticker: str, by: str, from_date: str | datetime, 
                           to_date: str | datetime = datetime.now(), multiplier: int = 1, limit: int = 1000) -> DerivativeBars:...
    
    def CoveredWarrantBars(self,ticker: str, by: str, from_date: str | datetime, 
                           to_date: str | datetime = datetime.now(), multiplier: int = 1, limit: int = 1000) -> CoveredWarrantBars:...
    
    def SubscribeDerivativeEvents(self,
                            tickers: list, 
                            callback: callable) -> SubscribeDerivativeEvents: ...
    def SubscribeCoveredWarrantEvents(self,
                            tickers: list, 
                            callback: callable) -> SubscribeCoveredWarrantEvents: ...
    def SubscribeTickerEvents(self,
                            tickers: list, 
                            callback: callable) -> SubscribeTickerEvents: ...
    def SubscribeIndexEvents(self,
                            tickers: list, 
                            callback: callable) -> SubscribeIndexEvents: ...
    
    
