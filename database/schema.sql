CREATE TABLE IF NOT EXISTS assets (
    id BIGSERIAL PRIMARY KEY,
    ticker VARCHAR(20) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    asset_type VARCHAR(50) NOT NULL,
    exchange VARCHAR(100),
    currency VARCHAR(10),
    sector VARCHAR(100),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS historical_prices (
    id BIGSERIAL PRIMARY KEY,
    asset_id BIGINT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    price_date DATE NOT NULL,
    open NUMERIC(18, 6),
    high NUMERIC(18, 6),
    low NUMERIC(18, 6),
    close NUMERIC(18, 6),
    adjusted_close NUMERIC(18, 6),
    volume BIGINT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT uq_historical_prices_asset_date
        UNIQUE (asset_id, price_date)
);

CREATE TABLE IF NOT EXISTS returns (
    id BIGSERIAL PRIMARY KEY,
    asset_id BIGINT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    return_date DATE NOT NULL,
    daily_return NUMERIC(18, 10),
    log_return NUMERIC(18, 10),

    CONSTRAINT uq_returns_asset_date
        UNIQUE (asset_id, return_date)
);

CREATE TABLE IF NOT EXISTS portfolios (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS portfolio_assets (
    portfolio_id BIGINT NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    asset_id BIGINT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    weight NUMERIC(18, 10) NOT NULL,

    PRIMARY KEY (portfolio_id, asset_id),

    CONSTRAINT portfolio_asset_weight_non_negative
        CHECK (weight >= 0)
);

CREATE TABLE IF NOT EXISTS risk_metrics (
    id BIGSERIAL PRIMARY KEY,
    portfolio_id BIGINT NOT NULL REFERENCES portfolios(id) ON DELETE CASCADE,
    metric_date DATE NOT NULL,
    volatility NUMERIC(18, 10),
    sharpe_ratio NUMERIC(18, 10),
    value_at_risk NUMERIC(18, 10),
    conditional_var NUMERIC(18, 10),
    max_drawdown NUMERIC(18, 10),

    CONSTRAINT uq_risk_metrics_portfolio_date
        UNIQUE (portfolio_id, metric_date)
);

CREATE TABLE IF NOT EXISTS predictions (
    id BIGSERIAL PRIMARY KEY,
    asset_id BIGINT NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    prediction_date DATE NOT NULL,
    target_date DATE NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    predicted_value NUMERIC(18, 10),
    actual_value NUMERIC(18, 10),
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_historical_prices_asset_date
    ON historical_prices(asset_id, price_date);

CREATE INDEX IF NOT EXISTS idx_returns_asset_date
    ON returns(asset_id, return_date);

CREATE INDEX IF NOT EXISTS idx_predictions_asset_date
    ON predictions(asset_id, prediction_date);
