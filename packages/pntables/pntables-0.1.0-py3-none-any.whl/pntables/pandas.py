import pandas as pd
import numpy as np
import panel as pn
import param
from panel.widgets import Tabulator

class PandasTabulator(pn.viewable.Viewer):
    rows_per_page = param.Integer(default=10, bounds=(1, 20))

    def __init__(self, all_interactive=True, max_bound=10, **params):
        super().__init__(**params)
        self.all_interactive = all_interactive
        self.max_bound = max_bound
        self.original_repr_html = pd.DataFrame._repr_html_
        self.tabulator = None
        self._override_pandas_repr()

    @param.depends('rows_per_page', watch=True)
    def _update_tabulator(self):
        """
        Updates the Tabulator instance with the new rows_per_page value.
        """
        if self.tabulator is not None:
            self.tabulator.page_size = self.rows_per_page

    def display_dataframe_as_tabulator(self, df):
        """
        Converts a pandas DataFrame to a Panel Tabulator widget for interactive display.

        Parameters
        ----------
        df : pd.DataFrame
            The pandas DataFrame to be displayed as a Tabulator.

        Returns
        -------
        pn.viewable.Viewable
            The Panel Tabulator widget for the DataFrame.
        """
        adj_max_bound = min(df.shape[0], self.max_bound)
        self.param.rows_per_page.bounds = (1, adj_max_bound)
        
        self.tabulator = Tabulator(
            df,
            sizing_mode="stretch_width",
            theme="midnight",
            pagination="local",
            page_size=self.rows_per_page,
            header_filters=True,
        )
        
        slider = pn.widgets.IntSlider.from_param(
            self.param.rows_per_page,
            name="Rows Per Page",
        )
        slider.end = adj_max_bound
        
        self.table_app = pn.Column(
            slider,
            self.tabulator,
        )
        return self.table_app

    def _custom_repr_html_(self, df):
        """
        Custom HTML representation for pandas DataFrames to use Tabulator
        when `all_interactive` is enabled.
        """
        if self.all_interactive:
            self.display_dataframe_as_tabulator(df)
            panel_obj = pn.panel(self.table_app)
            mimebundle = panel_obj._repr_mimebundle_()
            html = mimebundle[0].get('text/html', '')
            return html
        else:
            return self.original_repr_html(df)

    def _override_pandas_repr(self):
        """
        Overrides the pandas DataFrame HTML representation method with a custom method
        that uses Panel's Tabulator.
        """
        pd.DataFrame._repr_html_ = lambda df: self._custom_repr_html_(df)

# Default instance that sets up pandas integration automatically
pandas_tabulator = PandasTabulator()
