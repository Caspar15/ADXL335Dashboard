import dash
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from data import fetch_filtered_data, clear_cache
from plots import plot_time_series, plot_frequency_spectrum, plot_3d_surface, create_combined_plot
from layout import create_layout
from dash import dcc, html
import urllib.parse
import base64
import flask

# 初始化應用
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
     Output('real-time-data-table', 'data'),
     Output('alarm-output', 'children'),
     Output('alarm-output', 'style')],
    [Input('interval-component', 'n_intervals'),
     Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('submit-val', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_output(n_intervals, start_date, end_date, n_clicks, state_start_date, state_end_date):
    clear_cache()  # 清除緩存，為了接收即時資訊
    df_accel = fetch_filtered_data(state_start_date, state_end_date, 'AccelerometerData')
    df_stats = fetch_filtered_data(state_start_date, state_end_date, 'StatisticsData')

    if df_accel.empty or df_stats.empty:
        print("No data available for the selected date range")
        raise PreventUpdate

    print("df_accel columns:", df_accel.columns)  # 調試輸出
    print("df_stats columns:", df_stats.columns)  # 調試輸出

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
    peak_freq_z = plot_frequency_spectrum(df_stats, 'RECORDED_TIME', 'PEAK_FREQ_Z', 'bars')

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

    # alarm
    alarms = []
    if not df_accel.empty:
        if df_accel['XOUT'].iloc[0] > 9 or df_accel['XOUT'].iloc[0] < -9:
            alarms.append("XOUT 超過範圍！")
        if df_accel['YOUT'].iloc[0] > 9 or df_accel['YOUT'].iloc[0] < -9:
            alarms.append("YOUT 超過範圍！")
        if df_accel['ZOUT'].iloc[0] > 9 or df_accel['ZOUT'].iloc[0] < -9:
            alarms.append("ZOUT 超過範圍！")

    alarm_style = {'display': 'block'} if alarms else {'display': 'none'}
    alarm_message = html.Div(alarms, className='alarm') if alarms else None

    return [
        time_series_x, time_series_y, time_series_z,
        mse_x, mse_y, mse_z,
        std_x, std_y, std_z,
        peak_freq_x, peak_freq_y, peak_freq_z,
        plot3d_xyz, plot3d_mse, plot3d_std, plot3d_peak,
        real_time_data, alarm_message, alarm_style
    ]

@app.callback(
    [Output('week-comparison-dropdown', 'options'),
     Output('week-comparison-dropdown', 'value')],
    [Input('submit-val', 'n_clicks')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_week_options(n_clicks, start_date, end_date):
    clear_cache()  # 清除緩存
    df_accel = fetch_filtered_data(start_date, end_date, 'AccelerometerData')

    if df_accel.empty:
        print(f"No data available for the selected date range: {start_date} to {end_date}")
        return [], []

    df_accel['WEEK'] = df_accel['RECORDED_TIME'].dt.to_period('W').apply(lambda r: r.start_time)

    weeks = df_accel['WEEK'].drop_duplicates().sort_values()
    options = [{'label': f'Week starting {week}', 'value': str(week)} for week in weeks]

    return options, []

@app.callback(
    Output('combined-plot', 'children'),
    [Input('week-comparison-dropdown', 'value'),
     Input('data-type-dropdown', 'value')],
    [State('date-picker-range', 'start_date'),
     State('date-picker-range', 'end_date')]
)
def update_combined_plot(selected_weeks, selected_data_type, start_date, end_date):
    clear_cache()  # 清除緩存
    if not selected_weeks or not selected_data_type:
        raise PreventUpdate

    plots = []
    for week in selected_weeks:
        start_of_week = pd.to_datetime(week)
        end_of_week = start_of_week + pd.DateOffset(days=7)
        if selected_data_type in ['XOUT', 'YOUT', 'ZOUT']:
            df_week = fetch_filtered_data(start_of_week, end_of_week, 'AccelerometerData')
        else:
            df_week = fetch_filtered_data(start_of_week, end_of_week, 'StatisticsData')
        df_week['WEEK'] = week

        print(f"Week: {week}, Columns: {df_week.columns}")  # 調試輸出

        plot_title = f"{selected_data_type} for Week {week}"
        plot = create_combined_plot(df_week, 'RECORDED_TIME', [selected_data_type], plot_title)
        plots.append(dcc.Graph(figure=plot))

    return plots

@app.callback(
    Output('theme', 'children'),
    [Input('dark-theme-button', 'n_clicks'),
     Input('light-theme-button', 'n_clicks')]
)
def switch_theme(dark_clicks, light_clicks):
    ctx = dash.callback_context

    if not ctx.triggered:
        theme = dbc.themes.LUX
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'dark-theme-button':
            theme = dbc.themes.SLATE
        else:
            theme = dbc.themes.LUX

    return [html.Link(href=theme, rel='stylesheet')]

@app.callback(
    Output('download-link', 'href'),
    [Input('export-data', 'n_clicks')],
    [State('date-picker-range', 'start_date'), 
     State('date-picker-range', 'end_date')]
)
def update_download_link(n_clicks, start_date, end_date):
    if n_clicks is None or start_date is None or end_date is None:
        return dash.no_update
    
    df = fetch_filtered_data(start_date, end_date, 'AccelerometerData')
    if df.empty:
        return dash.no_update

    csv_string = df.to_csv(index=False, encoding='utf-8')
    b64 = base64.b64encode(csv_string.encode()).decode()
    
    return f"/downloadCSV?data={b64}"

@app.server.route('/downloadCSV')
def download_csv():
    data = flask.request.args.get('data')
    csv_string = base64.b64decode(data).decode('utf-8')
    return flask.Response(
        csv_string,
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=sensor_data.csv"}
    )

if __name__ == '__main__':
    app.run_server(debug=True)
