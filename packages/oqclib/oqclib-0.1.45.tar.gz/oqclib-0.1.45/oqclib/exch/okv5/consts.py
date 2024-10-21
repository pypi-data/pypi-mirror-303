# This is translated from Rust to Python.

# Constants for rate limit and API endpoints
RATE_LIMIT_SLEEP_20_PER_2 = 100  # Milliseconds
HOST = "https://www.okx.com"
REST_TICKER = "/api/v5/market/ticker?instId={}"
REST_INSTRUMENTS = "/api/v5/public/instruments?instType={}"
REST_FUNDING_RATE = "/api/v5/public/funding-rate?instId={}"
REST_CANDLE_STICK = "/api/v5/market/mark-price-candles?limit=100&instId={instId}&bar={bar}"
