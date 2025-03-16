"""App graphs."""

import pandas as pd

import plotly.graph_objects as go
import plotly.express as px
from vizro.models.types import capture


@capture("graph")
def stock_correlation_fig(data_frame: pd.DataFrame) -> go.Figure:
    """Create a correlation matrix figure.

    Args:
        data_frame: The data frame to create the correlation matrix for.

    Returns:
        The correlation matrix figure.
    """

    fig = px.imshow(
        data_frame,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        origin="lower",
    )
    return fig
