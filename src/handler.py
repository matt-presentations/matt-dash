
from .readers import *
import typing 
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

class Handler(object):
    
    def __init__(self):
        self.readers: typing.List[typing.Tuple[str, Reader]] = [] 
    
    def add_series(self, value: str, reader: Reader):
        self.readers.append((value, reader))

    def run_app(self):
        app = dash.Dash()
        default = self.readers[0][1]
        app.layout = html.Div([
            html.H1('Stock Tickers'),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {"label": k, "value": v} for k,v in self.readers
                ],
                value=default
            ),
            dcc.Graph(id='my-graph')
        ])
        
        @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
        def update_graph(selected_dropdown_value: Reader):
            return {
                'data': [{
                    'x': selected_dropdown_value.get_x(),
                    'y': selected_dropdown_value.get_y()
                }]
            }
        
        app.run_server()
