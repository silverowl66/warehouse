import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Market Dashboard",
    layout="wide"
)

st.title("Market Dashboard")
st.write("간단 가격확인용 대시보드")
st.info("ver0.0 : No API. Using TradingView Widget only")


# -----------------------------
# TradingView Widgets
# -----------------------------

def tradingview_single_quote(symbol: str):
    html = f"""
    <!-- TradingView Single Quote Widget BEGIN -->
    <div class="tradingview-widget-container">
      <div class="tradingview-widget-container__widget"></div>
      <script type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-single-quote.js"
        async>
      {{
        "symbol": "{symbol}",
        "width": "100%",
        "isTransparent": false,
        "colorTheme": "dark",
        "locale": "en"
      }}
      </script>
    </div>
    <!-- TradingView Single Quote Widget END -->
    """
    components.html(html, height=120, scrolling=False)


def tradingview_chart(symbol: str, height: int = 500):
    html = f"""
    <!-- TradingView Advanced Chart Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:{height}px;width:100%">
      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
      <div class="tradingview-widget-copyright">
        <a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank">
          <span class="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
      <script type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
        async>
      {{
        "autosize": true,
        "symbol": "{symbol}",
        "interval": "D",
        "timezone": "Asia/Seoul",
        "theme": "dark",
        "style": "1",
        "locale": "en",
        "allow_symbol_change": true,
        "calendar": false,
        "support_host": "https://www.tradingview.com"
      }}
      </script>
    </div>
    <!-- TradingView Advanced Chart Widget END -->
    """
    components.html(html, height=height + 50, scrolling=False)


# -----------------------------
# Symbols
# -----------------------------

symbols = {
    "USD/KRW": "FX_IDC:USDKRW",
    "BTC/USD": "BITSTAMP:BTCUSD",
    "Gold": "OANDA:XAUUSD",
    "Silver": "OANDA:XAGUSD",
}


# -----------------------------
# Simple Price Summary
# -----------------------------

st.subheader("가격 요약")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.caption("USD/KRW")
    tradingview_single_quote(symbols["USD/KRW"])

with col2:
    st.caption("BTC/USD")
    tradingview_single_quote(symbols["BTC/USD"])

with col3:
    st.caption("Gold")
    tradingview_single_quote(symbols["Gold"])

with col4:
    st.caption("Silver")
    tradingview_single_quote(symbols["Silver"])


st.divider()


# -----------------------------
# Main Charts
# -----------------------------

st.header("USD/KRW")
tradingview_chart(symbols["USD/KRW"], height=2000)

st.divider()

st.header("BTC/USD")
tradingview_chart(symbols["BTC/USD"], height=2000)

st.divider()

st.header("Gold / Silver")

gold_col, silver_col = st.columns(2)

with gold_col:
    st.subheader("Gold")
    tradingview_chart(symbols["Gold"], height=700)

with silver_col:
    st.subheader("Silver")
    tradingview_chart(symbols["Silver"], height=700)
