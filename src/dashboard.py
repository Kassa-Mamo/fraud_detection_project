import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# Example visualization
df = pd.read_csv('data/Fraud_Data.csv')  # Assuming the data has relevant columns

# Plotting some basic visualizations
fig = px.histogram(df, x='Amount', color='Fraud', title='Fraudulent vs Non-Fraudulent Transactions')

# Define app layout
app.layout = html.Div([
    html.H1('Fraud Detection Dashboard'),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
