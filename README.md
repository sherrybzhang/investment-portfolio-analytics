# Investment Portfolio Analytics

An investment performance analytics platform that tracks portfolio value over time, compares results to benchmarks, and surfaces allocation and drawdown insights. The focus is analytics and reporting (not trading or alpha generation), modeled after asset/wealth management workflows.

## Features
- Portfolio performance tracking (value, returns)
- Benchmark comparison and relative performance
- Allocation and concentration analysis
- Drawdown analysis (peak-to-trough)
- Analytics-ready data models for reporting

## Technologies
- **Languages**: Python 3.11, SQL
- **Libraries**: pandas, numpy, SQLAlchemy, psycopg
- **Database**: PostgreSQL
- **Analytics Engineering**: dbt
- **Visualization**: Streamlit

## Architecture
Layered analytics architecture:
1. **Ingestion** (Python): load holdings, prices, benchmarks into Postgres
2. **Storage** (PostgreSQL): central analytical database
3. **Transformation** (dbt): clean/transform raw data into analytics-ready tables
4. **Analytics & Visualization** (Streamlit): dashboards for performance insights

## Project Structure
```text
investment-portfolio-analytics/
├── ingestion/    # Data ingestion scripts
├── db/           # Database schema
├── dbt/          # dbt models
├── dashboard/    # Streamlit app
├── data/         # Raw data files (gitignored)
├── requirements.txt
└── README.md
```

## Setup (in progress)
High-level steps:
1. Create and activate a virtual environment
2. Install dependencies from `requirements.txt`
3. Set up PostgreSQL locally
4. Create the database and tables
5. Run ingestion scripts to load data

Detailed, step-by-step setup will be added as the project evolves.

## Usage (current)
- Load CSVs into Postgres with the ingestion scripts
- Confirm data is in the `prices`, `holdings`, and `benchmarks` tables

## Roadmap
- Add dbt models for returns and performance metrics
- Build Streamlit dashboards
- Add multi-benchmark support
- Add cash flow handling (contributions/withdrawals)

## Disclaimer
This project is for educational purposes only and does not constitute financial advice.
