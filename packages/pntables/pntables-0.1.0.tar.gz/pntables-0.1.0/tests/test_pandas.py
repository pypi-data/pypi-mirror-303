import pandas as pd
from panel import Column
from panel.widgets import Tabulator
from pntables.pandas import PandasTabulator

def test_display_dataframe():
    app = PandasTabulator()

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    widget = app.display_dataframe_as_tabulator(df)
    assert widget is not None
    assert isinstance(widget, Column)

def test_custom_repr_html():
    tabulator = PandasTabulator()

    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    html = df._repr_html_()
    assert '<div' in html
