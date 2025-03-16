"""App custom components."""

from typing import Literal

import vizro.models as vm
from dash import html


class Line(vm.VizroBaseModel):
    """New custom component `Line`."""

    type: Literal["line"] = "line"
    title: str = ""

    def build(self):  # pylint: disable=missing-function-docstring
        _div = []
        if self.title:
            _div += [html.H4(self.title)]
        _div += [html.Hr()]
        return html.Div(_div)
