# Investment Portfolio Analytics
This project is an end-to-end investment analytics platform built with Python and SQL to analyze portfolio performance and evaluate results relative to market benchmarks. It ingests portfolio holdings and market price data, models analytics-ready tables, and delivers professional insights. 

The goal of this project is to mirror how investment performance is reviewed in asset management and wealth management contexts.

## Features
- Portfolio performance tracking over time  
- Market benchmark comparison and relative performance  
- Asset allocation and holdings concentration analysis  
- Drawdown visualization for downside risk context  
- Analytics-ready data models for reporting and analysis  

## Motivation & Scope
Motivated by growing interest in portfolio management, mutual funds, and financial services analytics, this project builds an investment performance reporting workflow using modern data tooling.
### In scope:
- Investment portfolio performance analysis
- Benchmark comparison and relative performance
- Asset allocation and concentration analysis
- Clear, interpretable investment reporting
### Out of scope:
- Trading or execution systems
- Alpha generation or strategy optimization
- Advanced quantitative or derivative pricing models

## Financial Concepts Covered
- **Portfolio Performance**: Evaluating how a portfolio's value and returns change over time
- **Benchmarking**: Comparing portfolio performance relative to market indices
- **Relative Performance**: Measuring outperformance or underperformance versus a benchmark
- **Asset Allocation**: Understanding how capital is distributed across holdings
- **Drawdowns**: Analyzing peak-to-trough losses and recovery behavior 
- **Risk vs Return (Conceptual)**: Interpreting performance in the context of variability and downside risk

## Technical Architecture
The project follows a layered analytics architecture:
- **Data Ingestion**: Python scripts ingest portfolio holdings and market price data
- **Storage**: PostgreSQL serves as the central analytical database
- **Transformation**: dbt models clean, transform, and structure data for analytics
- **Analytics & Visualization**: Streamlit dashboards present portfolio insights and performance summaries

## Technology Stack
- **Python**: pandas, numpy, SQLAlchemy
- **SQL**: PostgreSQL
- **Analytics Engineering**: dbt
- **Visualization**: Streamlit
- **Version Control**: Git & GitHub

## Tooling Rationale
- **Python**: Used for data ingestion and analysis due to its strong ecosystem for financial and analytical workflows
- **PostgreSQL**: Serves as the central analytical database, well-suited for structured time-series and relational data
- **SQLAlchemy**: Provides a clean interface between Python and PostgreSQL, enabling maintainable database interactions
- **dbt**: Used to model and transform raw data into analytics-ready tables with testing and documentation
- **Streamlit**: Enables rapid development of interactive dashboards for investment performance reporting

## Project Structure
```text
investment-portfolio-analytics/
├── ingestion/    # Data ingestion scripts
├── dbt/          # dbt models and transformations
├── dashboard/    # Streamlit application
├── data/         # Raw data files (gitignored)
└── README.md
```

## Setup & Installation
This project uses a Python virtual environment and a local PostgreSQL database.

High-level setup steps:
1. Install Python 3.11
2. Create and activate a virtual environment
3. Install Python dependencies
4. Configure PostgreSQL connection

Detailed setup instructions will be added as the project evolves

## Usage
Typical workflow:
1. Ingest portfolio and market data into the database
2. Run dbt transformations to produce analytics-ready tables
3. Launch the Streamlit dashboard to review portfolio performance and insights

## Future Enhancements
- Add support for multiple benchmarks (SPY, AGG, etc.)
- Add transaction-based cash flows (contributions/withdrawals)
- Automated refresh (Prefect) + scheduled report generation

## Disclaimer
This project is for educational and informational purposes only. It does not constitute financial or investment advice.