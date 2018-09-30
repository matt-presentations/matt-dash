
from .readers import *
import typing 
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

class Handler(object):
    
    def __init__(self):
        self.values: typing.List[typing.Tuple[str, int]] = [] 
        self.readers: typing.List[Reader] = []
    
    def add_series(self, value: str, reader: Reader):
        self.values.append((value, len(self.readers)))
        self.readers.append(reader)

    def run_app(self):
        app = dash.Dash()
        default = self.values[0][1]
        app.layout = html.Div([
            html.H1('Stock Tickers'),
            dcc.Dropdown(
                id='my-dropdown',
                options=[
                    {"label": k, "value": v} for k,v in self.values
                ],
                value=default
            ),
            dcc.Graph(id='my-graph')
        ])
        
        @app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
        def update_graph(selected_dropdown_value: Reader):
            return {
                'data': [{
                    'x': self.readers[selected_dropdown_value].get_x(),
                    'y': self.readers[selected_dropdown_value].get_y()
                }]
            }
        
        app.run_server()
