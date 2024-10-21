

def format_time_period(minutes:int) -> str:
    if minutes < 60:
        return f"{minutes}m"  # Minutes
    elif minutes == 60:
        return "1H"  # 1 Hour
    elif minutes < 1440:
        hours = minutes // 60
        return f"{hours}H"  # Hours
    elif minutes == 1440:
        return "1D"  # 1 Day
    elif minutes < 10080:
        days = minutes // 1440
        return f"{days}D"  # Days
    elif minutes < 43200:
        weeks = minutes // 10080
        return f"{weeks}W"  # Weeks
    else:
        months = minutes // 43200
        return f"{months}M"  # Months

import asyncio
import aiohttp
import time
from datetime import datetime

async def fetch_candlesticks(client, symbol, bar_period, look_back_minutes):
    result = []
    now_ms = int(time.time() * 1000)
    from_ms = now_ms - look_back_minutes * 1000 * 60

    while True:
        to_ms = from_ms + 1000 * 60 * 100
        # url = f"{HOST}{REST_CANDLE_STICK.replace('{instId}', symbol).replace('{bar}', bar_period)}&before={to_ms}&after={from_ms}"
        
        print(f"Requesting {url} from {datetime.fromtimestamp(from_ms/1000)} to {datetime.fromtimestamp(to_ms/1000)}")
        async with client.get(url) as response:
            response_data = await response.json()
            if response_data['code'] == '0':  # Assuming '0' indicates success
                response_data['data'].reverse()
                result.extend(response_data['data'])
        
        if to_ms >= now_ms:
            break
        from_ms = to_ms
        await asyncio.sleep(RATE_LIMIT_SLEEP_20_PER_2 / 1000)  # Convert milliseconds to seconds

    return result

# Example usage
async def main():
    async with aiohttp.ClientSession() as client:
        candles = await fetch_candlesticks(client, 'BTC-USD', '1m', 60)
        print(candles)

if __name__ == '__main__':
    asyncio.run(main())
