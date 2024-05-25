import plotly.graph_objs as go
import numpy as np
from plotly.subplots import make_subplots
from scipy.fft import fft, fftfreq
from scipy.interpolate import griddata
import pandas as pd

# 自定義顏色和樣式
colors = {
    'background': '#f9f9f9',
    'text': '#2c3e50',
    'grid': '#bdc3c7',
    'primary': '#3498db',
    'secondary': '#2ecc71',
    'tertiary': '#e74c3c'
}

def plot_frequency_spectrum(df, x_column, y_column, title, plot_type='bars'):
    if df.empty:
        print(f"Missing data for frequency spectrum plot: {title}")
        return go.Figure()

    t = pd.to_datetime(df[x_column])
    sample_intervals = (t - t.shift()).dt.total_seconds().dropna()
    mean_interval = sample_intervals.mean()
    sampling_rate = 1.0 / mean_interval
    signal = df[y_column].to_numpy()
    N = len(signal)
    yf = fft(signal)
    xf = fftfreq(N, 1 / sampling_rate)
    
    # 考慮正頻率的部分，xf > 0。
    mask = xf >= 0
    xf = xf[mask]
    yf = yf[mask]
    amplitude = np.abs(yf) * 2.0 / N

    fig = go.Figure()
    if plot_type == 'bars':
        fig.add_trace(go.Bar(
            x=xf, y=amplitude, 
            marker_color=colors['primary'], 
            marker_line_color=colors['text'], 
            marker_line_width=1.5
        ))
    else:
        fig.add_trace(go.Scatter(
            x=xf, y=amplitude, mode='lines',
            line=dict(color=colors['primary'], width=2)
        ))

    fig.update_layout(
        title=title, 
        xaxis_title='Frequency (Hz)', 
        yaxis_title='Magnitude',
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color=colors['text']),
        margin=dict(l=40, r=20, t=40, b=30),
        hovermode='closest',
        xaxis=dict(gridcolor=colors['grid']),
        yaxis=dict(gridcolor=colors['grid'])
    )
    return fig

def plot_time_series(df, x_column, y_column, title):
    if df.empty:
        return go.Figure()
    
    fig = go.Figure()
    fig.add_trace(go.Scattergl(
        x=df[x_column], y=df[y_column], 
        mode='lines+markers',
        marker=dict(color=colors['primary'], size=5, line=dict(width=1)),
        line=dict(color=colors['primary'], width=2)
    ))
    fig.update_layout(
        title=title,
        xaxis=dict(tickformat='%b %d %Y', gridcolor=colors['grid']),
        yaxis=dict(title=y_column, gridcolor=colors['grid']),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color=colors['text']),
        margin=dict(l=40, r=20, t=40, b=30),
        hovermode='closest'
    )
    return fig

def plot_3d_surface(df, x_column, y_column, z_column, title):
    if df.empty:
        print(f"Missing data for 3D surface plot: {title}")
        return go.Figure()

    x = df[x_column]
    y = df[y_column]
    z = df[z_column]
    xi = np.linspace(x.min(), x.max(), 100)
    yi = np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)
    zi = griddata((x, y), z, (xi, yi), method='cubic')

    fig = go.Figure()
    fig.add_trace(go.Surface(
        x=xi, y=yi, z=zi,
        colorscale='Viridis',
        colorbar=dict(title='Z value'),
        contours=dict(
            z=dict(show=True, usecolormap=True, highlightcolor="limegreen", project=dict(z=True))
        )
    ))
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title=x_column,
            yaxis_title=y_column,
            zaxis_title=z_column,
            bgcolor=colors['background']
        ),
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color=colors['text']),
        margin=dict(l=40, r=20, t=40, b=30),
        hovermode='closest'
    )
    return fig

def create_combined_plot(df, x_column, y_columns, title):
    if df.empty:
        return go.Figure()

    fig = make_subplots(rows=1, cols=len(y_columns), shared_xaxes=True, subplot_titles=y_columns)
    for i, y_column in enumerate(y_columns, 1):
        fig.add_trace(go.Scatter(
            x=df[x_column], y=df[y_column], 
            mode='lines+markers', 
            name=y_column,
            marker=dict(color=colors['primary'], size=5, line=dict(width=1)),
            line=dict(color=colors['primary'], width=2)
        ), row=1, col=i)

    fig.update_layout(
        title_text=title, 
        showlegend=False,
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font=dict(family="Helvetica, Arial, sans-serif", size=12, color=colors['text']),
        margin=dict(l=40, r=20, t=40, b=30),
        hovermode='closest'
    )
    return fig
