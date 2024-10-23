from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import seaborn.objects as so
import pandas as pd
from typing import Tuple


def draw_components_and_line_chart(df: pd.DataFrame, 
                                   total_line_label: str | None = None, 
                                   component_design: str = "bar",
                                   ax: Axes | None = None,
                                   ) -> Tuple | None:
    """
    Generates a component chart using Seaborn for the dataframe provided.
    The dataframe needs to have all columns properly labelled, and both
    the main index and the column index need to have names, otherwise a runtime 
    warning will be generated.

    Args:
        df (pd.Dataframe): the original dataframe.
        total_line_label (str | None): the label to give to the total line or None
            if a total line is not desired; defaults to None.
        component_design (str): the component to represent the data. "bar" generates
            a stacked bar chart and "area" generates a stacked area chart; 
            defaults to "bar".
        ax (Axes | None): the axes over which to draw the chart or None if a new 
            figure and axes are required; defaults to None.

    Returns:
        Tuple | None: returns (fig, ax) if ax is not provided in input, else None.

    """
    assert(component_design in ["bar", "area"])

    if df.columns.name is None:
        raise RuntimeWarning("df.columns does not have a name, it will be auto-generated. Remove this warning by explicitly setting df.columns.name to something meaningful")
    if isinstance(df.index, pd.MultiIndex):
        if df.index.names is None:
            raise RuntimeWarning("df.index does not have level names, they will be auto-generated. Remove this warning by explicitly setting df.index.names to something meaningful")
    else:
        if df.index.name is None:
            raise RuntimeWarning("df.index does not have a name, it will be auto-generated. Remove this warning by explicitly setting df.index.name to something meaningful")

    # prepare the data
    dfs = df.stack()
    dfs.name = "values"
    dfc = dfs.reset_index()
    dfc_pos = dfc.loc[dfc["values"] >= 0.]
    dfc_neg = dfc.loc[dfc["values"] < 0.]
    x = dfs.index.names[0]
    y = dfs.name
    hue = dfs.index.names[1]

    # choose the component design
    if component_design == "bar":
        component = so.Bar(edgewidth=0)
    elif component_design == "area":
        component = so.Area(edgewidth=0)

    # prepare the chart adding positive and negative values 
    # separately and if required the total line
    pl = (
        so
        .Plot(data=dfc_pos, x=x, y=y, color=hue)
        .add(component, so.Stack())
        .add(component, so.Stack(), data=dfc_neg, x=x, y=y, color=hue)
        .label(x=x, y="")
    )

    if total_line_label is not None:
        total_data = df.sum(axis=1)
        total_data.name = total_line_label
        total_data_df = total_data.to_frame()
        total_data_df.columns.name = hue
        total_data_dfs = total_data_df.stack()
        total_data_dfs.name = y
        total_data_dfc = total_data_dfs.reset_index()
        pl = pl.add(so.Line(linewidth=3), data=total_data_dfc)

    # create a new figure if needed
    if ax is None:
        fig = plt.figure(figsize=(10,5));
        ax = fig.subplots();
        if total_line_label is not None:
            fig.suptitle(total_line_label + " - decomposition");

    # display the plot
    pl.on(ax).show()

    # return the new figure details if needed
    if ax is None:
        return fig, ax