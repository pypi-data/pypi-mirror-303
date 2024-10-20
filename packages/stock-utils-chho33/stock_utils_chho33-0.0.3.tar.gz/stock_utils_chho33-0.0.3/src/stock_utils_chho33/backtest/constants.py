from .models import ActionType, ChartColor, TransactionCost

TRANSACTION_COST = {
    ActionType.BUY: TransactionCost(val = 0, percentage = 0.0015),
    ActionType.SELL: TransactionCost(val = 0, percentage = 0.0045)
}

CHART_COLOR = ChartColor()
