from __future__ import annotations

import numpy as np
import pandas as pd
from sqlalchemy import text

from src.database.connection import engine


def load_adjusted_prices() -> pd.DataFrame:
    """Load adjusted closing prices from PostgreSQL."""

    query = """
        SELECT
            asset_id,
            price_date,
            adjusted_close
        FROM historical_prices
        WHERE adjusted_close IS NOT NULL
        ORDER BY asset_id, price_date;
    """

    with engine.connect() as connection:
        return pd.read_sql(text(query), connection)


def calculate_returns(data: pd.DataFrame) -> pd.DataFrame:
    """Calculate simple and logarithmic daily returns."""

    if data.empty:
        raise ValueError("No historical price data available.")

    data = data.copy()

    data["price_date"] = pd.to_datetime(data["price_date"])

    data = data.sort_values(
        ["asset_id", "price_date"]
    )

    data["daily_return"] = (
        data.groupby("asset_id")["adjusted_close"]
        .pct_change()
    )

    data["log_return"] = (
        data.groupby("asset_id")["adjusted_close"]
        .transform(
            lambda prices: np.log(prices / prices.shift(1))
        )
    )

    returns = data[
        [
            "asset_id",
            "price_date",
            "daily_return",
            "log_return",
        ]
    ].copy()

    returns = returns.rename(
        columns={"price_date": "return_date"}
    )

    returns = returns.dropna(
        subset=["daily_return", "log_return"]
    )

    return returns


def load_returns(data: pd.DataFrame) -> None:
    """Load calculated returns into PostgreSQL."""

    query = """
        INSERT INTO returns (
            asset_id,
            return_date,
            daily_return,
            log_return
        )
        VALUES (
            :asset_id,
            :return_date,
            :daily_return,
            :log_return
        )
        ON CONFLICT (asset_id, return_date)
        DO UPDATE SET
            daily_return = EXCLUDED.daily_return,
            log_return = EXCLUDED.log_return;
    """

    records = data.to_dict(orient="records")

    with engine.begin() as connection:
        connection.execute(
            text(query),
            records,
        )


def run_returns_pipeline() -> None:
    """Calculate and store asset returns."""

    prices = load_adjusted_prices()

    returns = calculate_returns(prices)

    load_returns(returns)

    print(
        f"{len(returns)} return observations loaded."
    )


if __name__ == "__main__":
    run_returns_pipeline()
