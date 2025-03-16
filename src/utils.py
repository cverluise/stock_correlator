"""Utility functions."""

from typing import List


def get_ticker_list(ticker_file: str = "data/00_asset/yf_main.txt") -> List[str]:
    """Get the list of stock tickers from the input file."""
    with open(ticker_file, "r") as file:
        # Read all lines and strip whitespace
        ticker_list = [line.strip() for line in file.readlines()]

        # Filter out any empty lines
        ticker_list = [ticker for ticker in ticker_list if ticker]
        ticker_list = list(sorted(ticker_list))
    return ticker_list
