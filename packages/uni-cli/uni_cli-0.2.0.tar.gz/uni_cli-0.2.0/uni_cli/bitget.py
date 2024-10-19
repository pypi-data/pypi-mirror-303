import typer

from crypto.bitget import mix_tickers, spot_tickers

app = typer.Typer()


@app.command()
def spot(symbols: str):
    """
    从bitget获取加密货币现货价格.

    参数:
    symbols:加密货币符号,可以是多个,用逗号分隔,例如:"BTCUSDT,ETHUSDT"
    """
    spot_tickers(symbols.split(","))


@app.command()
def mix(symbols: str):
    """
    从bitget获取加密货币合约价格.

    参数:
    symbols:加密货币符号,可以是多个,用逗号分隔,例如:"BTCUSDT,ETHUSDT"
    """
    mix_tickers(symbols.split(","))
