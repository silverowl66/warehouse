import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Market Dashboard",
    layout="wide"
)

st.title("Market Dashboard")
st.write("KRW/USD, BTC/USD, Gold, Silver 가격 확인용 간단 대시보드")

st.info(
    "초기 버전에서는 별도 API 없이 TradingView 차트 위젯으로 가격과 차트를 확인."
)

symbols = {
    "KRW/USD": "FX_IDC:USDKRW",
    "BTC/USD": "BITSTAMP:BTCUSD",
    "Gold": "OANDA:XAUUSD",
    "Silver": "OANDA:XAGUSD",
}


def tradingview_chart(symbol: str):
    html = f"""
    <!-- TradingView Widget BEGIN -->
    <div class="tradingview-widget-container" style="height:500px;width:100%">
      <div class="tradingview-widget-container__widget" style="height:calc(100% - 32px);width:100%"></div>
      <div class="tradingview-widget-copyright">
        <a href="https://www.tradingview.com/" rel="noopener nofollow" target="_blank">
          <span class="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js" async>
      {{
        "autosize": true,
        "symbol": "{symbol}",
        "interval": "D",
        "timezone": "Asia/Seoul",
        "theme": "light",
        "style": "1",
        "locale": "en",
        "allow_symbol_change": true,
        "calendar": false,
        "support_host": "https://www.tradingview.com"
      }}
      </script>
    </div>
    <!-- TradingView Widget END -->
    """
    components.html(html, height=550, scrolling=False)


asset = st.selectbox(
    "확인할 자산을 선택하세요",
    list(symbols.keys())
)

st.subheader(asset)
st.write(f"TradingView symbol: `{symbols[asset]}`")

tradingview_chart(symbols[asset])
