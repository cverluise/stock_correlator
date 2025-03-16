"""Test the stock_correlator module."""

# pylint: disable=missing-function-docstring,redefined-outer-name

import pytest
from pytest import approx
from src.processing import get_stock_correlation


@pytest.fixture
def expected_output():
    return {
        "GOOG": {"GOOG": 1.0, "MSFT": 0.9615403708872001, "AAPL": 0.8214847050734883},
        "MSFT": {"GOOG": 0.9615403708872001, "MSFT": 1.0, "AAPL": 0.6429335126080351},
        "AAPL": {"GOOG": 0.8214847050734883, "MSFT": 0.6429335126080351, "AAPL": 1.0},
    }


@pytest.fixture
def common_params():
    return {
        "start_date": "2010-01-01",
        "end_date": "2010-01-11",
        "interval": "1d",
        "ohlc": "Close",
    }


@pytest.mark.parametrize(
    "tickers",
    [
        ["AAPL", "GOOG", "MSFT"],
        ["AAPL", "GOOG", "MSFT", "CYRIL"],
    ],
)
def test_get_stock_ts(tickers, expected_output, common_params):
    result = get_stock_correlation(tickers, **common_params)

    assert result.keys() == expected_output.keys()
    for ticker in expected_output.keys():
        assert result[ticker] == approx(expected_output[ticker], abs=1e-3)


if __name__ == "__main__":
    pytest.main()
