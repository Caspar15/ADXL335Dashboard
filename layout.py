import dash_bootstrap_components as dbc
from dash import dcc, html
from datetime import date
from dash import dash_table

def create_layout():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("感測器數據監控", href="#", className="font-weight-bold"),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("主頁", href="#", className="nav-link-icon", external_link=True)),
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("更多資訊", header=True),
                                    dbc.DropdownMenuItem("官方文檔", href="https://plotly.com/dash/"),
                                    dbc.DropdownMenuItem("其他項目", href="#"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="探索",
                            ),
                            dbc.DropdownMenu(
                                [
                                    dbc.DropdownMenuItem("深色主題", id="dark-theme-button"),
                                    dbc.DropdownMenuItem("淺色主題", id="light-theme-button"),
                                ],
                                nav=True,
                                in_navbar=True,
                                label="主題切換",
                            ),
                        ],
                        className="ml-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    navbar=True,
                ),
            ]
        ),
        color="dark",
        dark=True,
        className="mb-5",
    )
    
    date_picker = dcc.DatePickerRange(
        id='date-picker-range',
        start_date=date.today(),
        end_date=date.today(),
        display_format='YYYY-MM-DD',
        start_date_placeholder_text='開始日期',
        end_date_placeholder_text='結束日期',
        minimum_nights=0,
        className="mb-3"
    )

    layout = dbc.Container([
        navbar,
        dbc.Row([
            dbc.Col([
                date_picker,
                html.Button('提交', id='submit-val', n_clicks=0, className="btn btn-primary mb-3"),
                html.Button('導出數據', id='export-data', n_clicks=0, className="btn btn-secondary mb-3"),
                html.A('下載數據', id='download-link', download="data.csv", href="", target="_blank", className="btn btn-info mb-3")
            ], width=12, className="d-flex justify-content-center")
        ]),
        dcc.Interval(
            id='interval-component',
            interval=60000,  # 60 seconds
            n_intervals=0
        ),
        dbc.Row(dbc.Col(html.H1("感測器數據監控", className="text-center text-primary mb-4 fade-in"), width=12)),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='XYZ 數據', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("X 軸數據", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-x', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Y 軸數據", className="bg-success text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-y', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Z 軸數據", className="bg-info text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-z', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D XYZ 軸數據", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-xyz', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12)
                ]),
            ]),
            dcc.Tab(label='MSE 數據', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error X", className="bg-warning text-dark text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-x', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error Y", className="bg-danger text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-y', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error Z", className="bg-info text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-z', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D MSE 數據", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-mse', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12)
                ]),
            ]),
            dcc.Tab(label='STD 數據', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation X", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-std-x', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation Y", className="bg-primary text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-std-y', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation Z", className="bg-success text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-std-z', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D STD 數據", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-std', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12)
                ]),
            ]),
            dcc.Tab(label='峰值頻率數據', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency X", className="bg-info text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-x', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency Y", className="bg-warning text-dark text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-y', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency Z", className="bg-danger text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-z', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D Peak Frequency 數據", className="bg-dark text-white text-center"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-peak', config={'displayModeBar': False}, className="fade-in"))
                    ], className="mb-4 shadow-sm"), width=12)
                ]),
            ]),
            dcc.Tab(label='實時數據', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("實時數據", className="bg-primary text-white text-center"),
                        dbc.CardBody([
                            dash_table.DataTable(
                                id='real-time-data-table',
                                columns=[
                                    {"name": "Parameter", "id": "parameter"},
                                    {"name": "Value", "id": "value"},
                                ],
                                data=[],
                                style_table={'height': '300px', 'overflowY': 'auto'},
                                style_cell={'textAlign': 'left'},
                            ),
                            html.Div(id='alarm-output', className='alarm text-center mt-3', style={'display': 'none'})  # 初始設置為隱藏
                        ], className="fade-in")
                    ], className="mb-4 shadow-sm"), width=12, lg=4)
                ]),
            ]),
            dcc.Tab(label='周數比較', children=[
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(
                            id='week-comparison-dropdown',
                            options=[],
                            multi=True,
                            placeholder="選擇要比較的周數"
                        )
                    ], width=12, className="mb-4")
                ]),
                dbc.Row([
                    dbc.Col([
                        dcc.Dropdown(
                            id='data-type-dropdown',
                            options=[
                                {'label': 'XOUT', 'value': 'XOUT'},
                                {'label': 'YOUT', 'value': 'YOUT'},
                                {'label': 'ZOUT', 'value': 'ZOUT'},
                                {'label': 'MSE_X', 'value': 'MSE_X'},
                                {'label': 'MSE_Y', 'value': 'MSE_Y'},
                                {'label': 'MSE_Z', 'value': 'MSE_Z'},
                                {'label': 'STD_X', 'value': 'STD_X'},
                                {'label': 'STD_Y', 'value': 'STD_Y'},
                                {'label': 'STD_Z', 'value': 'STD_Z'},
                                {'label': 'PEAK_FREQ_X', 'value': 'PEAK_FREQ_X'},
                                {'label': 'PEAK_FREQ_Y', 'value': 'PEAK_FREQ_Y'},
                                {'label': 'PEAK_FREQ_Z', 'value': 'PEAK_FREQ_Z'}
                            ],
                            placeholder="選擇要比較的數據類型",
                            className="mb-4"
                        )
                    ], width=12)
                ]),
                dbc.Row([
                    dbc.Col([
                        html.Div(id='combined-plot', className="mb-4 fade-in")
                    ], width=12)
                ])
            ])
        ]),
        html.Footer([
            html.Div("機械故障診斷與預測功能研究。", className="text-center text-muted"),
        ], className="footer mt-5 pt-3 pb-3"),
        html.Div(id='theme')
    ], fluid=True)
    
    return layout
