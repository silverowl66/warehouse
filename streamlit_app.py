import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Market Dashboard",
    layout="wide"
)

# -----------------------------
# Page style
# -----------------------------
st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1500px;
    }

    h1 {
        margin-bottom: 0.2rem;
    }

    div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0.2rem;
    }

    .chart-title {
        font-size: 1.45rem;
        font-weight: 700;
        margin-top: 0.5rem;
        margin-bottom: 0.15rem;
    }

    .mini-title {
        font-size: 1.05rem;
        font-weight: 700;
        margin-top: 0.2rem;
        margin-bottom: 0.1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Basic text
# -----------------------------
st.title("Market Dashboard")
st.write("간단 가격확인용 대시보드")
st.caption("ver0.0 : No API. Using TradingView Widget only")


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
# TradingView widgets
# -----------------------------
def tradingview_single_quote(symbol: str, height: int = 90):
    html = f"""
    <div class="tradingview-widget-container" style="width:100%; height:{height}px;">
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
    """
    components.html(html, height=height, scrolling=False)


def tradingview_chart(symbol: str, height: int = 720):
    html = f"""
    <div class="tradingview-widget-container" style="width:100%; height:{height}px;">
      <div class="tradingview-widget-container__widget" style="width:100%; height:{height}px;"></div>
      <script type="text/javascript"
        src="https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js"
        async>
      {{
        "width": "100%",
        "height": {height},
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
    """
    components.html(html, height=height, scrolling=False)


def chart_block(title: str, symbol: str, height: int):
    st.markdown(f"<div class='chart-title'>{title}</div>", unsafe_allow_html=True)
    tradingview_chart(symbol, height=height)


# -----------------------------
# Price summary
# -----------------------------
st.markdown("### 가격 요약")

col1, col2, col3, col4 = st.columns(4, gap="small")

with col1:
    st.markdown("<div class='mini-title'>USD/KRW</div>", unsafe_allow_html=True)
    tradingview_single_quote(symbols["USD/KRW"])

with col2:
    st.markdown("<div class='mini-title'>BTC/USD</div>", unsafe_allow_html=True)
    tradingview_single_quote(symbols["BTC/USD"])

with col3:
    st.markdown("<div class='mini-title'>Gold</div>", unsafe_allow_html=True)
    tradingview_single_quote(symbols["Gold"])

with col4:
    st.markdown("<div class='mini-title'>Silver</div>", unsafe_allow_html=True)
    tradingview_single_quote(symbols["Silver"])


# -----------------------------
# Main charts
# -----------------------------
chart_block("USD/KRW", symbols["USD/KRW"], height=780)
chart_block("BTC/USD", symbols["BTC/USD"], height=780)

st.markdown("<div class='chart-title'>Gold / Silver</div>", unsafe_allow_html=True)

gold_col, silver_col = st.columns(2, gap="small")

with gold_col:
    st.markdown("<div class='mini-title'>Gold</div>", unsafe_allow_html=True)
    tradingview_chart(symbols["Gold"], height=580)

with silver_col:
    st.markdown("<div class='mini-title'>Silver</div>", unsafe_allow_html=True)
    tradingview_chart(symbols["Silver"], height=580)
