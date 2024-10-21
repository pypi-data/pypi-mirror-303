import pandas as pd
from dataclasses import dataclass, field
from typing import List
import plotly.figure_factory as ff
import plotly.graph_objects as go

from .plotprotocol import PlotProtocol
from galileo_forecast.colors import PlotColors

@dataclass
class SingleInstancePlot(PlotProtocol):
    
    """
    Plot a single instance of a probabilities dataframe
    """

    # should pass in a dataframe with probabilities
    probabilities_df: pd.DataFrame

    # should pass a dataframe with greedy probabilities
    greedy_probabilities_df: pd.DataFrame

    # should pass in a dataframe with sampled probabilities
    sampled_probabilities_df: pd.DataFrame

    # index of the instance to plot
    index: int

    colors: PlotColors = field(default_factory=lambda: PlotColors())

    # should pass a dataframe with target
    def get_traces(self) -> List[dict]:
        # Create a histogram trace from the first row of probabilities_df
        histogram_trace = go.Histogram(
            x=self.probabilities_df.iloc[self.index], 
            name='Model Probabilities', 
            marker_color=self.colors.get_rgba("secondary_color", opacity=0.1),
            marker_line_color=self.colors.get_rgba("secondary_color"),
            marker_line_width=1.5,
            opacity=0.6
        )

        # Create a KDE (Kernel Density Estimation) trace for the distribution
        hist_data = [self.probabilities_df.iloc[self.index]]
        group_labels = ['Model Probabilities']
        distplot = ff.create_distplot(hist_data, group_labels, bin_size=0.02, show_hist=False, show_rug=False)

        # Extract the KDE trace from the distplot
        kde_trace = distplot['data'][0]
        kde_trace.update(name='Probability Distribution', yaxis='y2')

        # show vertical line at greedy_probabilities_df for same index
        greedy_trace = go.Scatter(x=[self.greedy_probabilities_df.iloc[self.index], self.greedy_probabilities_df.iloc[self.index]], 
                            y=[0, kde_trace.y.max()], 
                            name='Greedy Probability', 
                            mode='lines', 
                            line=dict(color=self.colors.get_rgba("primary_color"), width=2))
        
        # show vertical line at sampled_probabilities_df for same index
        sampled_trace = go.Scatter(x=[self.sampled_probabilities_df.iloc[self.index], self.sampled_probabilities_df.iloc[self.index]], 
                            y=[0, kde_trace.y.max()], 
                            name='Sampled Probability', 
                            mode='lines', 
                            line=dict(color=self.colors.get_grey_rgba(), width=2))
        
        # return traces
        return [{"trace": histogram_trace, "secondary_y": False},
                {"trace": kde_trace, "secondary_y": True},
                {"trace": greedy_trace, "secondary_y": True},
                {"trace": sampled_trace, "secondary_y": True}]

    def get_x_axes_layout(self, row: int, col: int) -> dict:
        return {
            "title_text": "Probability",
        }

    def get_y_axes_layout(self, row: int, col: int) -> dict:
        return {
            "title_text": "Count",
        }

    def get_secondary_y_axis_title(self):
        return "Density"