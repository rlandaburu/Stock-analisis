import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)

m = folium.Map(width=340,height=580,location=[lat, lon], tiles='cartodbpositron', zoom_start=8)
import datapane as dp
from datetime import date
dp.login(token="your token from datapane")
dp.Report(
                f"""
            _Analysis built {date.today()}_
                """,
                dp.Group(
                    dp.Plot(m, caption='Geographical interest'),
                    columns=1
                ),
            ).publish(name="map3", open=True)



