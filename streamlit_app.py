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
        max-width: 1600px;
    }

    h1 {
        margin-bottom: 0.2rem;
    }

    div[data-testid="stMarkdownContainer"] p {
        margin-bottom: 0.2rem;
    }

    .section-title {
        font-size: 1.55rem;
        font-weight: 800;
        margin-top: 0.9rem;
        margin-bottom: 0.25rem;
    }

    .chart-title {
        font-size: 1.15rem;
        font-weight: 700;
        margin-top: 0.25rem;
        margin-bottom: 0.1rem;
    }

    .mini-title {
        font-size: 0.95rem;
        font-weight: 700;
        margin-top: 0.15rem;
        margin-bottom: 0.05rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------
# Basic text
# -----------------------------
st.title("Market Dashboard")
st.write("간단 가격확인 대시보드")
st.caption("ver0.02 : No API. Using TradingView Widget only")


# -----------------------------
# Symbols
# -----------------------------
ASSETS = {
    # FX
    "USD/KRW": "FX_IDC:USDKRW",
    "JPY/KRW": "FX_IDC:JPYKRW",

    # Crypto
    "BTC/USD": "BITSTAMP:BTCUSD",
    "ETH/USD": "BITSTAMP:ETHUSD",
    "HYPE/USDT": "KUCOIN:HYPEUSDT",

    # Metals
    "Gold": "OANDA:XAUUSD",
    "Silver": "OANDA:XAGUSD",

    # US Indices
    "DJI": "TVC:DJI",
    "S&P 500": "TVC:SPX",
    "NASDAQ Composite": "NASDAQ:IXIC",

    # Asia Indices
    "KOSPI": "KRX:KOSPI",
    "KOSDAQ": "KRX:KOSDAQ",
    "NIKKEI 225": "TVC:NI225",
}


SUMMARY_ORDER = [
    "USD/KRW",
    "JPY/KRW",
    "BTC/USD",
    "ETH/USD",
    "HYPE/USDT",
    "Gold",
    "Silver",
    "DJI",
    "S&P 500",
    "NASDAQ Composite",
    "KOSPI",
    "KOSDAQ",
    "NIKKEI 225",
]


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


def tradingview_chart(symbol: str, height: int = 560):
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


def section_title(title: str):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)


def chart_title(title: str):
    st.markdown(f"<div class='chart-title'>{title}</div>", unsafe_allow_html=True)


def quote_card(asset_name: str):
    st.markdown(f"<div class='mini-title'>{asset_name}</div>", unsafe_allow_html=True)
    tradingview_single_quote(ASSETS[asset_name])


def chart_card(asset_name: str, height: int = 560):
    chart_title(asset_name)
    tradingview_chart(ASSETS[asset_name], height=height)


def render_quote_grid(asset_names, columns: int = 4):
    for i in range(0, len(asset_names), columns):
        row_assets = asset_names[i:i + columns]
        cols = st.columns(columns, gap="small")

        for col, asset_name in zip(cols, row_assets):
            with col:
                quote_card(asset_name)


def render_chart_grid(asset_names, columns: int = 2, height: int = 560):
    for i in range(0, len(asset_names), columns):
        row_assets = asset_names[i:i + columns]
        cols = st.columns(columns, gap="small")

        for col, asset_name in zip(cols, row_assets):
            with col:
                chart_card(asset_name, height=height)


# -----------------------------
# Price summary
# -----------------------------
section_title("가격 요약")
render_quote_grid(SUMMARY_ORDER, columns=4)


# -----------------------------
# Main charts
# -----------------------------
section_title("FX")
render_chart_grid(
    ["USD/KRW", "JPY/KRW"],
    columns=2,
    height=560
)

section_title("Crypto")
render_chart_grid(
    ["BTC/USD", "ETH/USD", "HYPE/USDT"],
    columns=3,
    height=540
)

section_title("Metals")
render_chart_grid(
    ["Gold", "Silver"],
    columns=2,
    height=540
)

section_title("US Market")
render_chart_grid(
    ["DJI", "S&P 500", "NASDAQ Composite"],
    columns=3,
    height=540
)

section_title("Korea / Japan Market")
render_chart_grid(
    ["KOSPI", "KOSDAQ", "NIKKEI 225"],
    columns=3,
    height=540
)
