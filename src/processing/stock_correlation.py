"""Process stock time series data."""

from typing import Dict, List, Literal

import yfinance as yf
import pandas as pd
from pandas import Timestamp

from logger import logger

OhlcOptions = Literal["Open", "High", "Low", "Close"]
IntervalOptions = Literal["1d", "1d", "5d", "1wk", "1mo", "3mo"]
StockDataType = Dict[str, Dict[Timestamp, float]]
MethodOptions = Literal["pearson", "spearman", "kendall"]


def _get_stock_ts(
    tickers: List[str],
    start_date: str,
    end_date: str,
    interval: IntervalOptions = "1d",
    ohlc: OhlcOptions = "Close",
    **kwargs,
) -> StockDataType:
    """
    Fetches the time series data for given stock tickers between start_date and end_date with
    the specified interval.

    Args:
        tickers: List of stock tickers to fetch data for.
        start_date: Start date for the time series data in 'YYYY-MM-DD' format.
        end_date: End date for the time series data in 'YYYY-MM-DD' format.
        interval: interval of the time series data. Defaults to '1d'.
        ohlc: The OHLC column to fetch. Defaults to 'Close'.
        kwargs: additional arguments to pass to the yfinance download function.

    Returns:
        The time series data for the given stock tickers
    """
    # Download the data
    df = yf.download(
        tickers=" ".join(tickers),
        start=start_date,
        end=end_date,
        interval=interval,
        group_by="ticker",
        **kwargs,
    )

    # Filter and format the data
    df = df.filter(regex=ohlc)

    df = df.ffill()  # ffill potential missing values
    df = df.dropna(axis=1)  # drop columns with remaining NaN values (only nan)

    # prep data
    df.columns = df.columns.get_level_values(0)
    df.index = df.index.strftime("%Y-%m-%d %H:%M:%S")
    ts_data = df.to_dict()

    # logging
    downloaded_tickers = set(ts_data.keys())
    logger.info(
        "Successful data download for the following tickers: %s", downloaded_tickers
    )
    if not downloaded_tickers.issuperset(tickers):
        logger.warning(
            "Data not available for the following tickers: %s",
            set(tickers) - downloaded_tickers,
        )

    return ts_data


def _get_correlation_matrix(
    data: StockDataType, method: MethodOptions, on_returns: bool = True
) -> pd.DataFrame:
    """
    Calculate the correlation matrix of the stock data.

    Args:
        data: The stock data to calculate the correlation matrix for.
        method: The method to use for calculating the correlation. Can be 'pearson', 'spearman',
            or 'kendall'.
        on_returns: Whether to calculate the correlation on returns or not. Defaults to True.

    Returns:
        The correlation matrix of the stock data.
    """
    df = pd.DataFrame.from_dict(data)

    if on_returns:
        df = df.pct_change().dropna()

    df_corr = df.corr(method=method)

    corr_data = df_corr.to_dict()
    logger.info("Correlation matrix calculated successfully")

    return corr_data


def get_stock_correlation(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    tickers: List[str],
    start_date: str,
    end_date: str,
    interval: IntervalOptions = "1d",
    ohlc: OhlcOptions = "Close",
    method: MethodOptions = "pearson",
    on_returns: bool = True,
):
    """Download stock data and calculate the correlation matrix.

    Args:
        tickers: List of stock tickers to fetch data for.
        start_date: Start date for the time series data in 'YYYY-MM-DD' format.
        end_date: End date for the time series data in 'YYYY-MM-DD' format.
        interval: interval of the time series data. Defaults to '1d'.
        ohlc: The OHLC column to fetch. Defaults to 'Close'.
        method: The method to use for calculating the correlation. Can be 'pearson', 'spearman',
            or 'kendall'.
        on_returns: Whether to calculate the correlation on returns or not. Defaults to True.

    Example:

        ```python
            ts_data = get_stock_ts(
            tickers=["AAPL", "GOOG", "MSFT"],
            start_date="2010-01-01",
            end_date="2010-01-11",
            interval="1d",
            prepost=False,
            progress=False,
        )
        corr_data = get_correlation_matrix(ts_data, method="pearson", on_returns=True)
        print(corr_data)
        ```

    returns:
        The correlation matrix of the stock data
    """
    ts_data = _get_stock_ts(
        tickers=tickers,
        start_date=start_date,
        end_date=end_date,
        interval=interval,
        ohlc=ohlc,
    )

    corr_data = _get_correlation_matrix(ts_data, method=method, on_returns=on_returns)

    return corr_data


if __name__ == "__main__":
    correlation_data = get_stock_correlation(
        tickers=["AAPL", "GOOG", "MSFT", "CYRIL"],
        start_date="2010-01-01",
        end_date="2010-01-11",
        interval="1d",
        ohlc="Close",
        method="pearson",
        on_returns=True,
    )
    print(correlation_data)
