import pandas as pd
import re
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
from .models import *
from .constants import *


def clean_hist(ticker: yf.ticker.Ticker, period: str = "17y"):
    hist = ticker.history(period = period)
    hist.index = list(map(lambda x: x.strftime("%Y-%m-%d"), hist.index))

    return hist

def to_int(val: str):
    try:
        return int(re.sub("[\$\,]", "", val))
    except:
        return None

def sustain(data: pd.Series, period: int) -> List[bool]:
    q = []
    result = []

    for item in data:
        if q and q[-1] == item:
            q.append(item)
        else:
            q = [item]

        if len(q) == period:
            result.append(q[-1])
            q.pop(0)
        else:
            result.append(False)

    return result

class BackTesting(BaseModel, extra="allow"):
    init_asset: Asset
    data: pd.DataFrame
    strategy_type: StrategyType
    shares_trime_digits: int = 3 # Taiwan stock 1 order = 1000 shares
    hard_transaction_mode: bool = True # Can't transaction when 漲跌停
    assets: List[Asset] = []
    transactions: List[Transaction] = []
    transaction_cost: Mapping[ActionType, TransactionCost] = TRANSACTION_COST

    class Config:
        arbitrary_types_allowed = True
        
    def model_post_init(self, __context):
        self.shares_factor = 10 ** self.shares_trime_digits

        self.assets.append(self.init_asset)

        self.price_type_while_action = {
            StrategyType.BUY_LOW_SELL_HIGH: {
                ActionType.BUY: StockPriceType.LOW,
                ActionType.SELL: StockPriceType.HIGH,
            },
            StrategyType.BUY_SELL_OPEN: {
                ActionType.BUY: StockPriceType.OPEN,
                ActionType.SELL: StockPriceType.OPEN,                
            },
            StrategyType.BUY_SELL_CLOSE: {
                ActionType.BUY: StockPriceType.CLOSE,
                ActionType.SELL: StockPriceType.CLOSE,                
            },
            StrategyType.BUY_HIGH_SELL_LOW: {
                ActionType.BUY: StockPriceType.HIGH,
                ActionType.SELL: StockPriceType.LOW,                
            }
        }
        
    def generate_stock_data_list(self, from_field: str, to_field: str = "value") -> List[StockData]:
        df = self.data[["date", from_field]]
        df[from_field] = df[from_field] / df[from_field].iloc[0]

        return list(map(lambda d: StockData(**d), df.rename({from_field: to_field}, axis=1).to_dict(orient="records")))
        
    def plus_transaction_cost(self, price: float, action_type: ActionType):
        multiplier = 1
        if action_type == ActionType.BUY:
            multiplier += self.transaction_cost[action_type].percentage
        elif action_type == ActionType.SELL:
            multiplier -= self.transaction_cost[action_type].percentage
        return price * multiplier
    
    def decide_price_type(self, action: float) -> StockPriceType:
        action_type = ActionType.SELL
        if not pd.isnull(action):
            action_type = ActionType.BUY if action > 0 else ActionType.SELL
        return self.price_type_while_action[self.strategy_type][action_type]
    
    def generate_result(self, first_asset: Asset, last_asset: Asset) -> BackTestingResultUnit:
        first_asset_value = first_asset.get_net_value()
        profit = last_asset.get_net_value() - first_asset_value
        profit_rate = profit / first_asset_value
        return BackTestingResultUnit(
            profit = profit,
            profit_rate = profit_rate,
        )
        
    def generate_overall_result(self) -> BackTestingOverallResultUnit:
        first_asset = self.assets[0]
        last_asset = self.assets[-1]
        
        price_type = self.decide_price_type(self.data.iloc[-1].action)
        last_price = self.data.iloc[-1][price_type.value.lower()]
        last_date = self.data.iloc[-1].date
        
        transaction_pairs, transactions_still_open = self.get_transaction_pairs(self.transactions, last_date, last_price)
        profits = list(map(lambda t: t.profit, transaction_pairs))
        number_profits = len(list(filter(lambda x: x > 0, profits)))
        number_losses = len(profits) - number_profits
        first_asset_value = first_asset.get_net_value()
        profit = last_asset.get_net_value() - first_asset_value

        return BackTestingOverallResultUnit(
            profit = profit,
            profit_rate = profit / first_asset_value,
            winning_rate = number_profits / len(profits) if profits else None,
            number_of_profits = number_profits,
            number_of_losses = number_losses,   
            transaction_pairs = transaction_pairs,
            transactions_still_open = transactions_still_open,
        )
    
    def get_transaction_pairs(
        self,
        transactions: List[Transaction],
        last_date: str,
        last_price: float,
    ) -> (List[TransactionPair], List[TransactionPair]):
        left_queue = []
        right_queue = deepcopy(transactions)
        transaction_pairs = []
        transactions_still_open = []
        
        while right_queue:
            if not left_queue:
                left_queue.append(right_queue.pop(0))
                continue
            transaction_right = right_queue[0]
            transaction_left = left_queue[-1]
            if transaction_left.type == transaction_right.type and\
                transaction_right.type == TransactionType.CASH and\
                transaction_left.action == ActionType.BUY and\
                transaction_right.action == ActionType.SELL:
                    shares_to_sell = min(transaction_left.shares, -transaction_right.shares)
                    profit = (transaction_right.price - transaction_left.price) * shares_to_sell
                    profit_rate = (transaction_right.price - transaction_left.price) / transaction_left.price
                    left_queue[-1].shares -= shares_to_sell
                    right_queue[0].shares += shares_to_sell
                    if left_queue[-1].shares <= 0:
                        left_queue.pop()
                        transaction_pair = TransactionPair(
                            date_buy = transaction_left.date,
                            date_sell = transaction_right.date,
                            price_buy = transaction_left.price,
                            price_sell = transaction_right.price,
                            profit = profit,
                            profit_rate = profit_rate,
                            shares = shares_to_sell,
                            transaction_type = TransactionType.CASH,
                        )
                        transaction_pairs.append(transaction_pair)
                    if right_queue[0].shares >= 0:
                        right_queue.pop(0)
            else:
                left_queue.append(right_queue.pop(0))
                
        while left_queue:
            transaction_left = left_queue.pop(0)

            if transaction_left.type == TransactionType.CASH:
                profit = last_price * transaction_left.shares
                profit_rate = (last_price - transaction_left.price) / transaction_left.price
                transaction_still_open = TransactionPair(
                    date_buy = transaction_left.date,
                    date_sell = last_date,
                    price_buy = transaction_left.price,
                    price_sell = last_price,
                    profit = profit,
                    profit_rate = profit_rate,
                    shares = transaction_left.shares,
                    transaction_type = TransactionType.CASH,
                )
                transactions_still_open.append(transaction_still_open)

        return transaction_pairs, transactions_still_open
        
    def run_transactions(self) -> None:
        did_not_buy = False
        did_not_sell = False
        # TODO: action is for only one target so far. Can support multiple by a dict
        for i, (_, record) in enumerate(self.data.iterrows()):
            price_type = self.decide_price_type(record.action)
            price = record[price_type.value.lower()]
            if pd.isnull(price): continue # TODO: price shouldn't be null

            asset = self.assets[-1]

            # skip high == low since might not buyable / sellable
            if pd.isnull(record.action) or not record.actionable:
                if not record.actionable:
                    if record.action > 0:
                        did_not_buy = True
                    elif record.action < 0:
                        did_not_sell = True
                new_asset = asset.update_price(record.date, price)
                self.assets.append(new_asset)
                continue

            transaction = None

            if record.action > 0 or (self.hard_transaction_mode and did_not_buy):
                cash_to_spend = asset.cash * record.action
                # assume no odd lot
                shares_to_buy = (cash_to_spend // (self.plus_transaction_cost(price, ActionType.BUY) * self.shares_factor)) * self.shares_factor
                if shares_to_buy > 0:
                    transaction = Transaction(
                        id = record.id,
                        date = record.date,
                        action = ActionType.BUY,
                        shares = shares_to_buy,
                        price = price
                    )
                    did_not_buy = False
            elif record.action < 0 or (self.hard_transaction_mode and did_not_sell):
                # assume no odd lot
                if record.id not in asset.equities: # no staok yet
                    continue
                # TODO: support multiple equities
                shares_to_sell = (int(asset.equities[record.id].shares * record.action) // self.shares_factor) * self.shares_factor
                if shares_to_sell < 0:
                    transaction = Transaction(
                        id = record.id,
                        date = record.date,
                        action = ActionType.SELL,
                        shares = shares_to_sell,
                        price = self.plus_transaction_cost(price, ActionType.SELL)
                    )
                    did_not_sell = False

            if transaction:
                #print(transaction)
                self.transactions.append(transaction)
                new_asset = asset.place_order(transaction)
            else:
                new_asset = asset.update_price(record.date, price)

            self.assets.append(new_asset)
        
        self.assets.pop(0) # pop dummy init asset

    def calculate_drawdowns(self, df: pd.DataFrame = None, field: str = "value") -> (float, List[Drawdown]):
        if df is None:
            df = pd.DataFrame(map(lambda a: {"date": a.date, field: a.get_net_value()}, self.assets))
        df = df.assign(previous_peak = df[field].cummax())
        df = df.assign(drawdown = (df[field] - df.previous_peak) / df.previous_peak)
        return min(df.drawdown), list(map(lambda d: Drawdown(date = d[1].date, value = d[1].drawdown), df.iterrows()))
    
    def calculate_buy_and_hold_baseline(self, stock_price_type: StockPriceType = StockPriceType.OPEN) -> Baseline:
        field = stock_price_type.value.lower()
        buy_and_hold_history = self.generate_stock_data_list(field)
        
        return self.calculate_baseline(buy_and_hold_history)
    
    def calculate_index_baseline(self) -> Baseline:
        baseline_history = self.generate_stock_data_list("baseline")
        
        return self.calculate_baseline(baseline_history)
    
    def calculate_baseline(
        self,
        data: List[StockData],
        field: str = "value",
    ) -> Baseline:
        dates, prices = [d.date for d in data], [d.value for d in data]
        growths = list(map(lambda p: p / prices[0], prices))
        profit_rate = (growths[-1] - growths[0]) / growths[0]
        history = pd.DataFrame({"date": dates, field: growths})
        max_drawdown, drawdowns = self.calculate_drawdowns(history, field)
        
        return Baseline(
            profit_rate = profit_rate,
            max_drawdown = max_drawdown,
            history = data,
            drawdowns = drawdowns,
        )
                
    def run(self) -> BackTestResult:
        self.run_transactions()
        max_drawdown, drawdowns = self.calculate_drawdowns()

        return BackTestResult(
            overall = self.generate_overall_result(),
            max_drawdown = max_drawdown,
            drawdowns = drawdowns,
            transactions = self.transactions,
            asset_hist = self.assets,
        )

def generate_stock_back_testing_results(df: pd.DataFrame) -> StockBackTestingResult:
    results = {}
    
    for strategy_type in (
            StrategyType.BUY_LOW_SELL_HIGH,
            StrategyType.BUY_SELL_OPEN,
            StrategyType.BUY_SELL_CLOSE,
            StrategyType.BUY_HIGH_SELL_LOW,
        ):

        init_asset = Asset(
            date = "1000-01-01",
            cash = 10000000,
            equities = {}
        )

        back_testing = BackTesting(
            data = df,
            init_asset = init_asset,
            strategy_type = strategy_type,
        )
        
        results[strategy_type.value] = back_testing.run()
        
    results["BUY_AND_HOLD"] = back_testing.calculate_buy_and_hold_baseline()

    results["BASELINE"] = back_testing.calculate_index_baseline()
    
    return StockBackTestingResult(**results)

def draw_stock_back_test_performance(
    stock_back_testing_results: StockBackTestingResult,
    width = 18.5,
    height = 10.5
):
    fig = plt.gcf()
    fig.set_size_inches(width, height)

    baseline = stock_back_testing_results.BASELINE.history

    if baseline:
        dates, baseline_values = [d.date for d in baseline], [d.value for d in baseline]

        plt.plot(dates, baseline_values, color = CHART_COLOR.BASELINE)

        plt.fill_between(dates, baseline_values, color = CHART_COLOR.BASELINE, alpha = 0.2)

    for strategy_type in (
            StrategyType.BUY_LOW_SELL_HIGH,
            StrategyType.BUY_SELL_OPEN,
            StrategyType.BUY_SELL_CLOSE,
            StrategyType.BUY_HIGH_SELL_LOW,
        ):
        assets = getattr(stock_back_testing_results, strategy_type.value).asset_hist

        transaction_pairs = getattr(stock_back_testing_results, strategy_type.value).overall.transaction_pairs

        transactions_still_open = getattr(stock_back_testing_results, strategy_type.value).overall.transactions_still_open

        transaction_pairs += transactions_still_open

        color = getattr(CHART_COLOR, strategy_type.value)

        dates, values = [d.date for d in assets], [d.get_net_value() / assets[0].get_net_value() for d in assets]

        plt.plot(dates, values, color = color)

        plt.fill_between(dates, values, color = color, alpha = 0.2)

        for transaction_pair in transaction_pairs:
            plt.fill_between(
                dates,
                values,
                where =[dt >= transaction_pair.date_buy and dt <= transaction_pair.date_sell for dt in dates],
                color = color,
                alpha = 0.4
            )

    buy_and_hold = stock_back_testing_results.BUY_AND_HOLD.history

    if buy_and_hold:
        dates, buy_and_hold_values = [d.date for d in buy_and_hold], [d.value for d in buy_and_hold]

        plt.plot(dates, buy_and_hold_values, color = CHART_COLOR.BUY_AND_HOLD)

        plt.fill_between(dates, buy_and_hold_values, color = CHART_COLOR.BUY_AND_HOLD, alpha = 0.2)

    plt.show()

def draw_stock_back_test_drawdowns(
    stock_back_testing_results: StockBackTestingResult,
    strategy_type = StrategyType.BUY_SELL_OPEN,
    width = 18.5,
    height = 10.5
):
    fig = plt.gcf()
    fig.set_size_inches(width, height)

    baseline_drawdowns = stock_back_testing_results.BASELINE.drawdowns

    if baseline_drawdowns:
        dates, baseline_values = [d.date for d in baseline_drawdowns], [d.value for d in baseline_drawdowns]

        plt.plot(dates, baseline_values, color = CHART_COLOR.BASELINE)

        plt.fill_between(dates, baseline_values, color = CHART_COLOR.BASELINE, alpha = 0.2)

    drawdowns = getattr(stock_back_testing_results, strategy_type.value).drawdowns

    color = getattr(CHART_COLOR, strategy_type.value)

    dates, values = [d.date for d in drawdowns], [d.value for d in drawdowns]

    plt.plot(dates, values, color = color)

    plt.fill_between(dates, values, color = color, alpha = 0.2)

    buy_and_hold_drawdowns = stock_back_testing_results.BUY_AND_HOLD.drawdowns

    if buy_and_hold_drawdowns:
        dates, values = [d.date for d in buy_and_hold_drawdowns], [d.value for d in buy_and_hold_drawdowns]

        plt.plot(dates, values, color = CHART_COLOR.BUY_AND_HOLD)

        plt.fill_between(dates, values, color = CHART_COLOR.BUY_AND_HOLD, alpha = 0.2)

    plt.show()

def print_stock_back_test_overall_performance(
    symbol: str,
    stock_back_testing_results: StockBackTestingResult,
    separate_line_width: int = 30,
):
    print(f"[{symbol}]")

    for strategy_type in (
            StrategyType.BUY_LOW_SELL_HIGH,
            StrategyType.BUY_SELL_OPEN,
            StrategyType.BUY_SELL_CLOSE,
            StrategyType.BUY_HIGH_SELL_LOW,
        ):
        overall = getattr(stock_back_testing_results, strategy_type.value).overall
        max_drawdown = getattr(stock_back_testing_results, strategy_type.value).max_drawdown

        print("-" * separate_line_width)
        print(f"**{strategy_type.value}**")
        print(f"profit rate: {overall.profit_rate}")
        print(f"winning rate: {overall.winning_rate}")
        print(f"number of profits: {overall.number_of_profits}")
        print(f"number of losses: {overall.number_of_losses}")
        print(f"maximum drawdown: {max_drawdown}")

    baseline = stock_back_testing_results.BASELINE.history

    baseline_max_drawdown = stock_back_testing_results.BASELINE.max_drawdown

    buy_and_hold = stock_back_testing_results.BUY_AND_HOLD.history

    buy_and_hold_max_drawdown = stock_back_testing_results.BUY_AND_HOLD.max_drawdown

    if baseline:
        print("-" * separate_line_width)
        print("**BASELINE**")
        print(f"profit rate: {baseline[-1].value / baseline[0].value - 1}")
        print(f"maximum drawdown: {baseline_max_drawdown}")

    if buy_and_hold:
        print("-" * separate_line_width)
        print("**BUY_AND_HOLD**")
        print(f"profit rate: {buy_and_hold[-1].value / buy_and_hold[0].value - 1}")
        print(f"maximum drawdown: {buy_and_hold_max_drawdown}")

    print("=" * separate_line_width)

def get_inventory_data(sustain_fall_period: int = 1, sustain_rise_period: int = 2):
    df = pd.read_clipboard()
    df["inventory"] = df["inventory"].apply(lambda x: to_int(x))
    df = df.sort_values("date")
    df = df.assign(diff = df.inventory.diff(1))
    df = df.assign(is_fall = df["diff"].apply(lambda x: x < 0))
    df = df.assign(is_rise = df["diff"].apply(lambda x: x > 0))
    df = df.assign(fall_sustain = sustain(df.is_fall, sustain_fall_period))
    df = df.assign(rise_sustain = sustain(df.is_rise, sustain_rise_period))
    df = df.assign(action = df.fall_sustain.apply(lambda x: int(x)) + df.rise_sustain.apply(lambda x: -int(x)))

    return df

def get_inventory_income_data(sustain_fall_period: int = 1, sustain_rise_period: int = 2):
    df = pd.read_clipboard()
    df["inventory"] = df["inventory"].apply(lambda x: to_int(x))
    df["income"] = df["income"].apply(lambda x: to_int(x))
    df = df.sort_values("date")
    df = df.assign(inventory_diff = df.inventory.diff(1))
    df = df.assign(inventory_is_fall = df["inventory_diff"].apply(lambda x: x < 0))
    df = df.assign(inventory_is_rise = df["inventory_diff"].apply(lambda x: x > 0))
    df = df.assign(inventory_fall_sustain = sustain(df.inventory_is_fall, sustain_fall_period))
    df = df.assign(inventory_rise_sustain = sustain(df.inventory_is_rise, sustain_rise_period))

    df = df.assign(income_diff = df.income.diff(1))
    df = df.assign(income_is_fall = df["income_diff"].apply(lambda x: x < 0))
    df = df.assign(income_is_rise = df["income_diff"].apply(lambda x: x > 0))
    df = df.assign(income_fall_sustain = sustain(df.income_is_fall, sustain_fall_period))
    df = df.assign(income_rise_sustain = sustain(df.income_is_rise, sustain_rise_period))

    df = df.assign(fall_sustain = df.inventory_fall_sustain & df.income_rise_sustain)
    df = df.assign(rise_sustain = df.inventory_rise_sustain & df.income_fall_sustain)

    df = df.assign(action = df.fall_sustain.apply(lambda x: int(x)) + df.rise_sustain.apply(lambda x: -int(x)))

    return df

def get_inventory_income_ratio_data(sustain_fall_period: int = 1, sustain_rise_period: int = 2):
    df = pd.read_clipboard()
    df["inventory"] = df["inventory"].apply(lambda x: to_int(x))
    df["income"] = df["income"].apply(lambda x: to_int(x))
    df = df.assign(inventory_income_ratio = df.inventory / df.income)
    df = df.sort_values("date")
    df = df.assign(ratio_diff = df.inventory_income_ratio.diff(1))
    df = df.assign(ratio_is_fall = df["ratio_diff"].apply(lambda x: x < 0))
    df = df.assign(ratio_is_rise = df["ratio_diff"].apply(lambda x: x > 0))
    df = df.assign(ratio_fall_sustain = sustain(df.ratio_is_fall, sustain_fall_period))
    df = df.assign(ratio_rise_sustain = sustain(df.ratio_is_rise, sustain_rise_period))

    df = df.assign(income_diff = df.income.diff(1))
    df = df.assign(income_is_fall = df["income_diff"].apply(lambda x: x < 0))
    df = df.assign(income_is_rise = df["income_diff"].apply(lambda x: x > 0))
    df = df.assign(income_fall_sustain = sustain(df.ratio_is_fall, sustain_fall_period))
    df = df.assign(income_rise_sustain = sustain(df.ratio_is_rise, sustain_rise_period))

    df = df.assign(fall_sustain = df.ratio_fall_sustain & df.income_rise_sustain)
    df = df.assign(rise_sustain = df.ratio_rise_sustain & df.income_fall_sustain)

    df = df.assign(action = df.fall_sustain.apply(lambda x: int(x)) + df.rise_sustain.apply(lambda x: -int(x)))

    return df

def get_inventory_income_ratio_only_data(sustain_fall_period: int = 1, sustain_rise_period: int = 2):
    df = pd.read_clipboard()
    df["inventory"] = df["inventory"].apply(lambda x: to_int(x))
    df["income"] = df["income"].apply(lambda x: to_int(x))
    df = df.assign(inventory_income_ratio = df.inventory / df.income)
    df = df.sort_values("date")
    df = df.assign(ratio_diff = df.inventory_income_ratio.diff(1))
    df = df.assign(ratio_is_fall = df["ratio_diff"].apply(lambda x: x < 0))
    df = df.assign(ratio_is_rise = df["ratio_diff"].apply(lambda x: x > 0))
    df = df.assign(ratio_fall_sustain = sustain(df.ratio_is_fall, sustain_fall_period))
    df = df.assign(ratio_rise_sustain = sustain(df.ratio_is_rise, sustain_rise_period))


    df = df.assign(fall_sustain = df.ratio_fall_sustain)
    df = df.assign(rise_sustain = df.ratio_rise_sustain)

    df = df.assign(action = df.fall_sustain.apply(lambda x: int(x)) + df.rise_sustain.apply(lambda x: -int(x)))

    return df

def create_data_for_back_test(
    symbol: str,
    df_action: pd.DataFrame,
    create_baseline: bool = True,
    baseline_field: str = "open"
):
    hist = yf.Ticker(symbol)
    hist = clean_hist(hist)

    date_start = max(hist.index[0], df_action.date.iloc[0])
    hist = hist.query(f"index >= '{date_start}'")
    df_action = df_action.query(f"date >= '{date_start}'")

    df = pd.merge(hist, df_action.set_index("date"), how = "outer", left_index = True, right_index = True).sort_index(ascending = True)
    df.columns = [col.lower() for col in df.columns]
    df = df[["open", "high", "low", "close", "action"]].reset_index().rename({"index": "date"}, axis = 1)
    df = df.assign(id=symbol)
    df.action = df.action.shift(1)

    if create_baseline:
        df_baseline = create_data_for_back_test("^TWII", df_action, False)
        df = pd.merge(
            df,
            df_baseline[["date", baseline_field]].rename({baseline_field: "baseline"}, axis = 1),
            how = "outer",
            on = "date"
        )

    df = df.sort_values("date")

    cols = ["open", "high", "low", "close", "baseline"] if create_baseline else ["open", "high", "low", "close"]
    df.loc[:,cols] = df.loc[:,cols].bfill()
    df = df.dropna(subset = cols)
    df = df.assign(actionable = df.high != df.low)

    return df
