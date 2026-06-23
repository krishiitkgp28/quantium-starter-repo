import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load and process data
df = pd.read_csv('formatted_output.csv')
df['Date'] = pd.to_datetime(df['Date'])
daily_sales = df.groupby('Date', as_index=False)['Sales'].sum()

# Initialize Dash app
app = Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Over Time", style={'textAlign': 'center'}),
    dcc.Graph(
        figure=px.line(
            daily_sales,
            x='Date',
            y='Sales',
            title='Daily Sales of Pink Morsels'
        ).update_layout(
            xaxis_title='Date',
            yaxis_title='Sales (USD)'
        )
    )
])

if __name__ == '__main__':
    app.run(debug=True)   