from decimal import Decimal

import requests


def tickers(url: str, symbols: list):
    response = requests.get(url)
    resp_json = response.json()
    symbols_list = [
        s.lower() + "usdt" if not s.lower().endswith("usdt") else s.lower()
        for s in symbols
    ]
    if response.status_code == 200 and resp_json.get("code") == "00000":
        data = resp_json.get("data", [])
        results = []
        for item in data:
            if item["symbol"].lower() in symbols_list:
                price = Decimal(item["lastPr"])
                results.append(
                    f"{item['symbol'].upper().rstrip('USDT')}:{format(price, 'f')}"
                )
        print(f"[{','.join(results)}]")
    else:
        print(
            f"📌 请求失败,状态码:{response.status_code},错误信息:{resp_json.get('msg')}"
        )


def mix_tickers(symbols: list):
    url = "https://api.bitget.com/api/v2/mix/market/tickers?productType=USDT-FUTURES"
    tickers(url, symbols)


def spot_tickers(symbols: list):
    url = "https://api.bitget.com/api/v2/spot/market/tickers"
    tickers(url, symbols)
