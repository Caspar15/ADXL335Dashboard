import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from data import fetch_filtered_data
from plots import plot_time_series, plot_frequency_spectrum, plot_3d_surface
from layout import create_layout

# 使用 Bootstrap Lux 主題
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
server = app.server

app.layout = create_layout()

@app.callback(
    [Output('graph-x', 'figure'),
     Output('graph-y', 'figure'),
     Output('graph-z', 'figure'),
     Output('graph-mse-x', 'figure'),
     Output('graph-mse-y', 'figure'),
     Output('graph-mse-z', 'figure'),
     Output('graph-std-x', 'figure'),
     Output('graph-std-y', 'figure'),
     Output('graph-std-z', 'figure'),
     Output('graph-peak-x', 'figure'),
     Output('graph-peak-y', 'figure'),
     Output('graph-peak-z', 'figure'),
     Output('graph-3d-xyz', 'figure'),
     Output('graph-3d-mse', 'figure'),
     Output('graph-3d-std', 'figure'),
     Output('graph-3d-peak', 'figure'),
     Output('real-time-data-table', 'data')],
    [Input('interval-component', 'n_intervals'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('submit-val', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_output(n_intervals, start_date, end_date, n_clicks, state_start_date, state_end_date):
    df_accel = fetch_filtered_data(state_start_date, state_end_date, 'AccelerometerData')
    df_stats = fetch_filtered_data(state_start_date, state_end_date, 'StatisticsData')

    if df_accel.empty or df_stats.empty:
        raise PreventUpdate

    # 繪製時間序列數據
    time_series_x = plot_time_series(df_accel, 'RECORDED_TIME', 'XOUT', 'Time Series Data for XOUT')
    time_series_y = plot_time_series(df_accel, 'RECORDED_TIME', 'YOUT', 'Time Series Data for YOUT')
    time_series_z = plot_time_series(df_accel, 'RECORDED_TIME', 'ZOUT', 'Time Series Data for ZOUT')

    # 繪製MSE數據
    mse_x = plot_time_series(df_stats, 'RECORDED_TIME', 'MSE_X', 'Mean Squared Error (MSE) for X')
    mse_y = plot_time_series(df_stats, 'RECORDED_TIME', 'MSE_Y', 'Mean Squared Error (MSE) for Y')
    mse_z = plot_time_series(df_stats, 'RECORDED_TIME', 'MSE_Z', 'Mean Squared Error (MSE) for Z')

    # 繪製STD數據
    std_x = plot_time_series(df_stats, 'RECORDED_TIME', 'STD_X', 'Standard Deviation (STD) for X')
    std_y = plot_time_series(df_stats, 'RECORDED_TIME', 'STD_Y', 'Standard Deviation (STD) for Y')
    std_z = plot_time_series(df_stats, 'RECORDED_TIME', 'STD_Z', 'Standard Deviation (STD) for Z')

    # 使用直條圖繪製峰值頻率數據
    peak_freq_x = plot_frequency_spectrum(df_stats, 'RECORDED_TIME', 'PEAK_FREQ_X', 'Peak Frequency for X', 'bars')
    peak_freq_y = plot_frequency_spectrum(df_stats, 'RECORDED_TIME', 'PEAK_FREQ_Y', 'Peak Frequency for Y', 'bars')
    peak_freq_z = plot_frequency_spectrum(df_stats, 'RECORDED_TIME', 'PEAK_FREQ_Z', 'Peak Frequency for Z', 'bars')

    # 繪製3D圖表
    plot3d_xyz = plot_3d_surface(df_accel, 'XOUT', 'YOUT', 'ZOUT', '3D Scatter Plot for XYZ Axis')
    plot3d_mse = plot_3d_surface(df_stats, 'MSE_X', 'MSE_Y', 'MSE_Z', '3D Scatter Plot for MSE Data')
    plot3d_std = plot_3d_surface(df_stats, 'STD_X', 'STD_Y', 'STD_Z', '3D Scatter Plot for STD Data')
    plot3d_peak = plot_3d_surface(df_stats, 'PEAK_FREQ_X', 'PEAK_FREQ_Y', 'PEAK_FREQ_Z', '3D Scatter Plot for Peak Frequency Data')

    # 顯示實時數據
    real_time_data = [
        {"parameter": "XOUT", "value": df_accel['XOUT'].iloc[0] if not df_accel.empty else 'N/A'},
        {"parameter": "YOUT", "value": df_accel['YOUT'].iloc[0] if not df_accel.empty else 'N/A'},
        {"parameter": "ZOUT", "value": df_accel['ZOUT'].iloc[0] if not df_accel.empty else 'N/A'}
    ]

    return [
        time_series_x, time_series_y, time_series_z,
        mse_x, mse_y, mse_z,
        std_x, std_y, std_z,
        peak_freq_x, peak_freq_y, peak_freq_z,
        plot3d_xyz, plot3d_mse, plot3d_std, plot3d_peak,
        real_time_data
    ]

if __name__ == '__main__':
    app.run_server(debug=True)
