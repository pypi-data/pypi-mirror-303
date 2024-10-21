class SubscribeTickerUpdate:
    def __init__(self, access_token: str, ticker: str, callback: callable, by: str, from_date: str) -> None:
        self.ticker: str
        self._stop: bool

    def start(self) -> None: ...
    
    def stop(self) -> None: ...


