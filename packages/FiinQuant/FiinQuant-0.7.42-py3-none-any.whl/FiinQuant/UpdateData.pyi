import pandas as pd

class UpdateData:
    def __init__(self, data: pd.DataFrame) -> None:
        self.__private_attribute: pd.DataFrame 
        self.TradingDate: str
        self.OpenPrice: float
        self.LowestPrice: float
        self.HighestPrice: float
        self.ClosePrice: float
        self.MatchVolume: int

    def get_data(self) -> pd.DataFrame: ...
