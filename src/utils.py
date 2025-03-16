"""Utility functions."""

import ast
from typing import List


def get_ticker_list(ticker_file: str = "data/00_asset/yf_symbols.txt") -> List[str]:
    """Get the list of stock tickers from the input file."""
    with open(ticker_file, "r") as f:
        content = f.read().strip()
    ticker_list = list(ast.literal_eval(content))
    return ticker_list
