import dash_bootstrap_components as dbc
from dash import dcc, html, dash_table
from datetime import date

def create_layout():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarBrand("感測器數據監控", href="#", className="font-weight-bold"),
                dbc.NavbarToggler(id="navbar-toggler"),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("主頁", href="#")),
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
        start_date_placeholder_text='Start Date',
        end_date_placeholder_text='End Date',
        minimum_nights=0,
        className="mb-3"
    )

    layout = dbc.Container([
        navbar,
        dbc.Row([
            dbc.Col([
                date_picker,
                html.Button('Submit', id='submit-val', n_clicks=0, className="btn btn-primary mb-3"),
            ], width=12, className="d-flex justify-content-center")
        ]),
        dcc.Interval(
            id='interval-component',
            interval=60000,  # 60 seconds
            n_intervals=0
        ),
        dbc.Row(dbc.Col(html.H1("Sensor Data Monitoring", className="text-center text-primary mb-4"), width=12)),
        dcc.Tabs(id="tabs", children=[
            dcc.Tab(label='XYZ Axis Data', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("X Axis Data", className="bg-primary text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-x', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Y Axis Data", className="bg-success text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-y', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Z Axis Data", className="bg-info text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-z', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D XYZ Axis Data", className="bg-dark text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-xyz', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12,)
                ]),
            ]),
            dcc.Tab(label='MSE Data', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error X", className="bg-warning text-dark"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-x', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error Y", className="bg-danger text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-y', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Mean Squared Error Z", className="bg-secondary text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-mse-z', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D MSE Data", className="bg-dark text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-mse', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12),
                ]),
            ]),
            dcc.Tab(label='STD Data', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation X", className="bg-dark text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-std-x', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation Y", className="bg-primary text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-std-y', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Standard Deviation Z", className="bg-success text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-std-z', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D STD Data", className="bg-dark text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-std', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12),
                ]),
            ]),
            dcc.Tab(label='Peak Frequency Data', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency X", className="bg-info text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-x', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency Y", className="bg-warning text-dark"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-y', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Peak Frequency Z", className="bg-danger text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-peak-z', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("3D Peak Frequency Data", className="bg-dark text-white"),
                        dbc.CardBody(dcc.Graph(id='graph-3d-peak', config={'displayModeBar': False}))
                    ], className="mb-4 shadow-sm"), width=12),
                ]),
            ]),
            dcc.Tab(label='Real-time Data', children=[
                dbc.Row([
                    dbc.Col(dbc.Card([
                        dbc.CardHeader("Real-time Data", className="bg-primary text-white"),
                        dbc.CardBody(dash_table.DataTable(
                            id='real-time-data-table',
                            columns=[
                                {"name": "Parameter", "id": "parameter"},
                                {"name": "Value", "id": "value"},
                            ],
                            data=[],
                            style_table={'height': '300px', 'overflowY': 'auto'},
                            style_cell={'textAlign': 'left'},
                        ))
                    ], className="mb-4 shadow-sm"), width=12, lg=4),
                ]),
            ]),
        ]),
        dcc.Interval(
            id='interval-component',
            interval=60000, # 將刷新間隔調整為60秒
            n_intervals=0
        )
    ], fluid=True)
    
    return layout
