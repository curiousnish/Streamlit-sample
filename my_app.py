import pandas as pd
import datetime as dt
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas_datareader.data as web

st.write("""
# Simple WEB App
""")
start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()

Stock_name = st.text_input("Ticker", 'AAPL')

df = web.DataReader(Stock_name, "yahoo", start, end)
df.reset_index(inplace=True)

fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
fig.add_trace(go.Scatter(x=df.Date, y=df['Adj Close'], mode='lines'), row=1, col=1)
fig.add_trace(go.Bar(
    x=df.Date, y=df['Volume']), row=2, col=1)

st.plotly_chart(fig)
