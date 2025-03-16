"""Library of static objects"""

import pandas as pd
from src.utils import get_ticker_list

TICKER_LIST = get_ticker_list()

STOCK_CORRELATION_STARTER_DF = pd.DataFrame.from_dict(
    {
        "GOOG": {"GOOG": 1.0, "MSFT": 0.9615403708872001, "AAPL": 0.8214847050734883},
        "MSFT": {"GOOG": 0.9615403708872001, "MSFT": 1.0, "AAPL": 0.6429335126080351},
        "AAPL": {"GOOG": 0.8214847050734883, "MSFT": 0.6429335126080351, "AAPL": 1.0},
    }
)
