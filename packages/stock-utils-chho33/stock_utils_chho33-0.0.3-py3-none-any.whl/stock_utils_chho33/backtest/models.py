from __future__ import annotations
from datetime import datetime, date
from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from typing import List, TypedDict, Mapping, Optional
from enum import Enum
from copy import deepcopy
from functools import reduce

@dataclass
class FinanceData:
    id: Optional[str]
    name: Optional[str]
    date: date

@dataclass
class StockPrice(FinanceData):
    open: float
    close: float
    high: float
    low: float

@dataclass
class Equity:
    id: str
    shares: int = 0
    price: float = 0

class TransactionType(Enum):
    CASH = "CASH"
    MARGIN_BUY = "MARGIN_BUY"
    MARGIN_SELL = "MARGIN_SELL"

class StockPriceType(Enum):
    OPEN = "OPEN"
    CLOSE = "CLOSE"
    HIGH = "HIGH"
    LOW = "LOW"

class ActionType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

class StrategyType(Enum):
    BUY_LOW_SELL_HIGH = "BUY_LOW_SELL_HIGH"
    BUY_SELL_OPEN = "BUY_SELL_OPEN"
    BUY_SELL_CLOSE = "BUY_SELL_CLOSE"
    BUY_HIGH_SELL_LOW = "BUY_HIGH_SELL_LOW"

@dataclass
class Action(FinanceData):
    action: ActionType
    portion: float # buy or sell fraction. -1.0 ~ +1.0

@dataclass
class Transaction:
    id: str
    date: date
    action: ActionType
    shares: int # +: buy, -: sell
    price: float
    type: TransactionType = TransactionType.CASH

@dataclass
class TransactionCost:
    val: float
    percentage: float

@dataclass
class Asset:
    date: date
    cash: float
    equities: Mapping[str, Equity]

    def place_order(self, transaction: Transaction) -> Asset:
        cash = self.cash - (transaction.shares * transaction.price)
        equities = deepcopy(self.equities)

        if transaction.id not in equities:
            equities[transaction.id] = Equity(
                id = transaction.id,
                shares = transaction.shares,
                price = transaction.price
            )
        else:
            new_shares = equities[transaction.id].shares + transaction.shares
            if new_shares > 0:
                new_equity = Equity(
                    id = transaction.id,
                    shares = new_shares,
                    price = transaction.price
                )
                equities[transaction.id] = new_equity
            else:
                equities[transaction.id] = Equity(
                    id = transaction.id,
                    price = transaction.price
                )

        return Asset(
            date = transaction.date,
            cash = cash,
            equities = equities
        )

    def update_price(self, date, price) -> Asset:
        equities = deepcopy(self.equities)

        for id in equities.keys():
            equities[id] = Equity(
                id = id,
                shares = equities[id].shares,
                price = price
            )

        return Asset(
            date = date,
            cash = self.cash,
            equities = equities
        )

    def get_net_value(self):
        return self.cash + (reduce(
            lambda x, y: x + y,
            map(lambda eq: eq.shares * eq.price, self.equities.values())
        ) if self.equities else 0)

@dataclass
class GenericFinanceData:
    date: date
    value: float

@dataclass
class Drawdown(GenericFinanceData):
    pass

@dataclass
class StockData(GenericFinanceData):
    pass
        
class TransactionPair(BaseModel):
    date_buy: date
    date_sell: date
    holding_dates: int = 0
    price_buy: float
    price_sell: float
    profit: float
    profit_rate: float
    shares: int
    transaction_type: TransactionType
        
    class Config:
        arbitrary_types_allowed = True

    def model_post_init(self, __context):
        self.holding_dates = abs((self.date_sell - self.date_buy).days)
        
@dataclass
class Baseline:
    profit_rate: float
    max_drawdown: float
    history: List[StockData]
    drawdowns: List[Drawdown]

@dataclass
class BackTestTransactions:
    profits: List[float]
    transaction_date_pairs: List[TransactionPair]

@dataclass
class BackTestingResultUnit:
    profit: float
    profit_rate: float

@dataclass
class BackTestingOverallResultUnit(BackTestingResultUnit):
    winning_rate: Optional[float]
    number_of_profits: int
    number_of_losses: int
    transaction_pairs: List[TransactionPair]
    transactions_still_open: List[TransactionPair] 
    
@dataclass
class BackTestResult:
    overall: BackTestingOverallResultUnit
    #by_year: List[BackTestingResultUnit]
    #by_month: List[BackTestingResultUnit]
    drawdowns: List[Drawdown]
    max_drawdown: float
    transactions: List[Transaction]
    asset_hist: List[Asset]

@dataclass        
class StockBackTestingResult:
    BUY_LOW_SELL_HIGH: BackTestResult
    BUY_SELL_OPEN: BackTestResult
    BUY_SELL_CLOSE: BackTestResult
    BUY_HIGH_SELL_LOW: BackTestResult
    BUY_AND_HOLD: Baseline
    BASELINE: Baseline

@dataclass
class ChartColor:
    BASELINE: str = "grey"
    BUY_LOW_SELL_HIGH: str = "greenyellow"
    BUY_SELL_OPEN: str = "skyblue"
    BUY_SELL_CLOSE: str = "lightsteelblue"
    BUY_HIGH_SELL_LOW: str = "plum"
    BUY_AND_HOLD: str = "goldenrod"
