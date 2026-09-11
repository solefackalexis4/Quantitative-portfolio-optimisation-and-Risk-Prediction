from __future__ import annotations

import pandas as pd
from sqlalchemy import text

from src.database.connection import engine
from src.data.market_data import download_market_data


def get_assets() -> pd.DataFrame:
    """Retrieve the assets available in the database."""
    query = """
        SELECT id, ticker
        FROM assets
        ORDER BY id;
    """

    with engine.connect() as connection:
        return pd.read_sql(text(query), connection)


def clean_market_data(
    data: pd.DataFrame,
    asset_id: int,
) -> pd.DataFrame:
    """Validate and transform downloaded market data."""

    required_columns = [
        "price_date",
        "Open",
        "High",
        "Low",
        "Close",
        "Adj Close",
        "Volume",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in data.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    cleaned = data[
        [
            "price_date",
            "Open",
            "High",
            "Low",
            "Close",
            "Adj Close",
            "Volume",
        ]
    ].copy()

    cleaned = cleaned.rename(
        columns={
            "Open": "open",
            "High": "high",
            "Low": "low",
            "Close": "close",
            "Adj Close": "adjusted_close",
            "Volume": "volume",
        }
    )

    cleaned["asset_id"] = asset_id

    cleaned["price_date"] = pd.to_datetime(
        cleaned["price_date"]
    ).dt.date

    numeric_columns = [
        "open",
        "high",
        "low",
        "close",
        "adjusted_close",
        "volume",
    ]

    for column in numeric_columns:
        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="coerce",
        )

    cleaned = cleaned.dropna(
        subset=[
            "price_date",
            "close",
            "adjusted_close",
        ]
    )

    cleaned = cleaned.drop_duplicates(
        subset=["asset_id", "price_date"]
    )

    cleaned = cleaned[
        [
            "asset_id",
            "price_date",
            "open",
            "high",
            "low",
            "close",
            "adjusted_close",
            "volume",
        ]
    ]

    return cleaned


def load_market_data(data: pd.DataFrame) -> None:
    """Insert validated market data into PostgreSQL."""

    query = """
        INSERT INTO historical_prices (
            asset_id,
            price_date,
            open,
            high,
            low,
            close,
            adjusted_close,
            volume
        )
        VALUES (
            :asset_id,
            :price_date,
            :open,
            :high,
            :low,
            :close,
            :adjusted_close,
            :volume
        )
        ON CONFLICT (asset_id, price_date)
        DO UPDATE SET
            open = EXCLUDED.open,
            high = EXCLUDED.high,
            low = EXCLUDED.low,
            close = EXCLUDED.close,
            adjusted_close = EXCLUDED.adjusted_close,
            volume = EXCLUDED.volume;
    """

    records = data.to_dict(orient="records")

    with engine.begin() as connection:
        connection.execute(
            text(query),
            records,
        )


def run_etl(
    start: str = "2024-01-01",
    end: str = "2025-01-01",
) -> None:
    """Run the complete market-data ETL pipeline."""

    assets = get_assets()

    if assets.empty:
        raise ValueError(
            "No assets found in the database."
        )

    for _, asset in assets.iterrows():
        asset_id = int(asset["id"])
        ticker = asset["ticker"]

        print(f"Downloading {ticker}...")

        raw_data = download_market_data(
            ticker=ticker,
            start=start,
            end=end,
        )

        cleaned_data = clean_market_data(
            raw_data,
            asset_id=asset_id,
        )

        load_market_data(cleaned_data)

        print(
            f"{ticker}: "
            f"{len(cleaned_data)} rows loaded."
        )


if __name__ == "__main__":
    run_etl()
