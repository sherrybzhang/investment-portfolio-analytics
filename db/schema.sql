/*
  prices: daily closing price per asset symbol
  e.g. 2024-01-02 | AAPL  | 185.64
*/
CREATE TABLE IF NOT EXISTS prices (
  date DATE NOT NULL,
  symbol TEXT NOT NULL,
  close_price NUMERIC(18,6) NOT NULL
);

/*
  holdings: how many shares you own per symbol on each date
  e.g. 2024-01-02 | AAPL  | 10.00
*/
CREATE TABLE IF NOT EXISTS holdings (
  date DATE NOT NULL,
  symbol TEXT NOT NULL,
  quantity NUMERIC(18, 6) NOT NULL
);

/*
  benchmarks: daily closing price per benchmark symbol (e.g., SPY, VTI)
  e.g. 2024-01-02 | SPY | 470.10
*/
CREATE TABLE IF NOT EXISTS benchmarks (
  date DATE NOT NULL,
  symbol TEXT NOT NULL,
  close_price NUMERIC(18,6) NOT NULL
);

-- Indexes: speed up searches by date + symbol
CREATE INDEX IF NOT EXISTS idx_prices_date_symbol ON prices(date, symbol);
CREATE INDEX IF NOT EXISTS idx_holdings_date_symbol ON holdings(date, symbol);
CREATE INDEX IF NOT EXISTS idx_benchmarks_date_symbol ON benchmarks(date, symbol);