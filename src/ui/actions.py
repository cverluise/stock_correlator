"""App actions"""

from typing import List

import pandas as pd
import plotly.graph_objects as go
from vizro.models.types import capture

from processing import get_stock_correlation
from ui.graphs import stock_correlation_fig


@capture("action")
def stock_correlation_action(tickers: List[str], date_range: List[str]) -> go.Figure:
    """Stock correlation action."""
    data = get_stock_correlation(
        tickers,
        start_date=date_range[0],
        end_date=date_range[1],
    )
    data_frame = pd.DataFrame.from_dict(data).round(2)

    fig = stock_correlation_fig(data_frame)
    return fig
