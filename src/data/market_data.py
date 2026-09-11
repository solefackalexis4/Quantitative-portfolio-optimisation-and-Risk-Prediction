from datetime import datetime

import pandas as pd
import yfinance as yf


def download_market_data(
    ticker: str,
    start: str,
    end: str | None = None,
) -> pd.DataFrame:
    """
    Download historical market data for a financial asset.

    Parameters
    ----------
    ticker : str
        Yahoo Finance ticker symbol.
    start : str
        Start date in YYYY-MM-DD format.
    end : str, optional
        End date in YYYY-MM-DD format.

    Returns
    -------
    pandas.DataFrame
        Historical OHLCV market data.
    """

    data = yf.download(
        ticker,
        start=start,
        end=end,
        auto_adjust=False,
        progress=False,
    )

    if data.empty:
        raise ValueError(f"No market data found for ticker: {ticker}")

    data = data.copy()

    # Handle yfinance MultiIndex columns when present.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data.index.name = "price_date"
    data = data.reset_index()

    data["ticker"] = ticker
    data["downloaded_at"] = datetime.utcnow()

    return data


if __name__ == "__main__":
    df = download_market_data(
        ticker="AAPL",
        start="2024-01-01",
        end="2025-01-01",
    )

    print(df.head())
    print()
    print(df.info())
