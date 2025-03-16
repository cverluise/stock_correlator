"""App."""

import vizro.models as vm
from vizro import Vizro

from vizro.models._components.form._user_input import UserInput

from ui.actions import stock_correlation_action
from ui.components import Line
from ui.graphs import stock_correlation_fig

from lib import TICKER_LIST, STOCK_CORRELATION_STARTER_DF


vm.Page.add_type("controls", vm.Dropdown)
vm.Page.add_type("controls", vm.DatePicker)
vm.Page.add_type("controls", vm.Button)
vm.Page.add_type("controls", UserInput)
vm.Page.add_type("controls", Line)
vm.Page.add_type("components", vm.Card)


stock_correlation_page = vm.Page(
    title="Stock correlation",
    components=[
        vm.Graph(
            id="stock_correlation_fig",
            title="Stock correlation",
            figure=stock_correlation_fig(STOCK_CORRELATION_STARTER_DF),
        ),
    ],
    controls=[
        vm.Button(
            text="Run",
            actions=[
                vm.Action(
                    function=stock_correlation_action(),  # pylint: disable=no-value-for-parameter
                    inputs=["ticker_dropdown.value", "ticker_date_picker.value"],
                    outputs=["stock_correlation_fig.figure"],
                )
            ],
        ),
        Line(),
        vm.Dropdown(
            id="ticker_dropdown",
            title="Tickers",
            options=TICKER_LIST,
            multi=True,
            value=["AAPL", "GOOG", "MSFT"],
        ),
        vm.DatePicker(
            id="ticker_date_picker",
            title="Date range",
            min="2010-01-01",
            max="2010-01-11",
        ),
    ],
)

dashboard = vm.Dashboard(pages=[stock_correlation_page])

if __name__ == "__main__":
    Vizro().build(dashboard).run()  # debug=True
