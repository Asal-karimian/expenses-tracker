import pandas as pd
import plotly.express as px

def plot_pie_chart(df):
    return px.pie(df, values='amount', names='category', title='Expense Distribution')

def plot_line_chart(df):
    df_time = df.groupby('date')['amount'].sum().reset_index()
    return px.line(df_time, x='date', y='amount', title='Spending Over Time')
