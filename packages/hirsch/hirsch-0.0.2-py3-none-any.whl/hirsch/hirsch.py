
from numpy import linspace, interp
from collections.abc import Callable, Iterable

def hirsch(
    populations: Iterable[float],
    x_min: float = 0.0,
    x_max: float | None = None,
    precision: int = 1,
    sort: bool = True,
    plot: bool = False,
) -> float:

    """Takes a list of populations and returns the continuous Hirsch-index. 
    
    :param populations: Iterable of populations
    :x_min: minimum x-value
    :x_max: maximum x-value, defaults to number of data points
    :precision: number of interpolation points between data points
    :sort: sort the populations, set to False if populations is already sorted
    """

    if sort:
        y = sorted(populations, reverse=True)
    else:
        y = populations

    x_max = x_max or len(populations)

    x = linspace(x_min, x_max, len(populations))
    q = linspace(x_min,x_max,len(populations)*(1/precision))
    
    y_smooth = interp(q, x, y)   
    
    last_a = q[0]
    for a,b in zip(q,y_smooth):
        if a >= b:
            break
        last_a = a
    h = last_a

    if plot:
        import plotly.graph_objects as go
        fig = go.Figure()
        trace = go.Scatter(x=x, y=y, name="populations", mode="markers")
        fig.add_trace(trace)
        
        trace = go.Scatter(mode="lines", x=[0,0,h,h,0], y=[0,h,h,0,0], name="h_box")
        fig.add_trace(trace)

        trace = go.Scatter(x=q, y=y_smooth, name="interpolated")
        fig.add_trace(trace)

        return fig, h

    return h
