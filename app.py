import dash
import os
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd
import joblib
from datetime import datetime

df = pd.read_csv('dataset.csv')

if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['month'] = df['Order Date'].dt.strftime('%Y-%m') 
else:

    df['month'] = '2023-01'

model = joblib.load('sales_model.pkl')
X = df[['Quantity', 'Discount', 'Profit']].fillna(0)
df['predicted_sales'] = model.predict(X)

app = dash.Dash(__name__)
app.title = "Sales Performance Dashboard"

app.layout = html.Div([
    html.H1("Sales Performance Dashboard"),
    
    html.Label("Select Month:"),
    dcc.Dropdown(
        id='month-dropdown',
        options=[{'label': m, 'value': m} for m in sorted(df['month'].dropna().unique())],
        value=sorted(df['month'].dropna().unique())[0]
    ),
    
    dcc.Graph(id='sales-graph'),
])

@app.callback(
    Output('sales-graph', 'figure'),
    Input('month-dropdown', 'value')
)
def update_graph(selected_month):
    filtered_df = df[df['month'] == selected_month]
   
    fig = go.Figure(data=[
        go.Bar(name='Actual Sales', x=filtered_df['Region'], y=filtered_df['Sales']),
        go.Bar(name='Predicted Sales', x=filtered_df['Region'], y=filtered_df['predicted_sales'])
    ])

    fig.update_layout(
        title=f'Sales Performance in {selected_month}',
        barmode='group',
        xaxis_title='Region',
        yaxis_title='Sales'
    )
    return fig

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',  # Must be 0.0.0.0 (not 127.0.0.1/localhost)
        port=int(os.environ.get('PORT', 8050)),  # Use Render's PORT env var
        debug=True
    )