import numpy as np
from plotly import express as px
from plotly import graph_objects as go

from ..utils.ensure import ensure_2dims, ensure_npy


def plotly_signals(
    signals,
    srate=None,
    channels_name=None,
    fixed_y=False,
    colorscheme='Prism',
    colors: list = None,
    height=None,
    width=None,
    show=True,
):
    """使用 Plotly 可视化多通道信号


    Parameters
    ----------
    - `signals` : _type_
        - _description_
    - `srate` : _type_, optional
        - _description_, by default None
    - `channels_name` : _type_, optional
        - _description_, by default None
    - `fixed_y` : bool, optional
        - _description_, by default False
    - `colorscheme` : str, optional
        - _description_, by default 'Prism'
    - `colors` : list, optional
        - _description_, by default None
    - `height` : _type_, optional
        - _description_, by default None
    - `width` : _type_, optional
        - _description_, by default None
    - `show` : bool, optional
        - _description_, by default True

    Returns
    ----------
    - `_type_`
        - _description_
    """
    signals = ensure_npy(signals)
    signals = ensure_2dims(signals)

    ch_cnt, time_cnt = signals.shape
    if channels_name is None:
        channels_name = [f'Ch{i}' for i in range(ch_cnt)]

    x = np.arange(time_cnt)
    if srate:
        x = x / srate
    np.linspace(0, 1, ch_cnt + 1)
    y_part = np.linspace(0, 1, ch_cnt + 1)
    # y_part = list(reversed(np.linspace(0, 1, ch_cnt + 1)))

    if colors is None:
        colors = getattr(px.colors.qualitative, colorscheme)
    elif isinstance(colors, str):
        colors[colors] * ch_cnt

    fig = go.Figure()

    for ch in range(ch_cnt):
        y = signals[ch, :]
        name = channels_name[ch]
        fig.add_trace(
            go.Scatter(
                x=x,
                y=y,
                name=name,
                mode='lines',
                yaxis=f'y{ch + 1}',
                marker=dict(color=colors[ch]),
            )
        )
        yaxis_key = f'yaxis{ch + 1}'  # if ch > 0 else 'yaxis'
        yaxis = dict(
            automargin=True,
            showline=True,
            side='left',
            domain=[y_part[ch], y_part[ch + 1]],
            # domain=[y_part[ch + 1], y_part[ch]],
            fixedrange=fixed_y,
            title=name,
            mirror=True,
            type='linear',
            linecolor=colors[ch],
            # showticklabels=False,
            # nticks=3,
            tickfont={'color': colors[ch], 'size': 10},
            tickmode='auto',
            titlefont={'color': colors[ch]},
        )
        fig.update_layout(**{yaxis_key: yaxis})

    fig.update_traces(hoverinfo='x+name+y', showlegend=False)

    fig.update_xaxes(
        autorange=True,
        rangeslider=dict(autorange=True, visible=True),
        showticklabels=True,
        tickfont={'size': 12},
    )

    fig.update_layout(
        autosize=True,
        height=height,
        width=width,
        hovermode='x',
        template='plotly_white',
        legend=dict(traceorder='reversed'),
        margin=dict(t=0, b=0),
    )
    if show:
        fig.show()
    return fig
