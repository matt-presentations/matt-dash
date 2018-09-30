
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt

app = dash.Dash()


app.layout = html.Div([
    html.H1('Stock Tickers'),
    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'Coke', 'value': 1},
            {'label': 'Tesla', 'value': 2},
            {'label': 'Apple', 'value': 3}
        ],
        value='COKE'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('my-dropdown', 'value')])
def update_graph(selected_dropdown_value):
    return {
        'data': [{
            'x': [1,2,3],
            'y': [ selected_dropdown_value * x for x in [5,2,3]]
        }]
    }

app.run_server()
