# Financial Market Analytics

> Financial analysis and prediction project based on Python, PostgreSQL, Data Science, and Machine Learning.

---

##  Project Overview

**Financial Market Analytics** is a financial data analysis and prediction project designed to progressively build a complete platform for collecting, storing, processing, analyzing, and modeling financial market data.

The project aims to combine:

- Financial data collection and preparation
- Structured data storage using PostgreSQL
- Exploratory and statistical analysis
- Financial data visualization
- Financial indicator development
- Feature engineering
- Machine Learning model development
- Model performance evaluation
- Interactive dashboard development
- Data pipeline automation
- Reproducible and maintainable workflows

The project is being developed in a **WSL 2 / Ubuntu** environment using **Python**, **PostgreSQL**, **Git**, and **Visual Studio Code**.

---

##  Current Project Status

> ** WORK IN PROGRESS — PROJECT NOT YET COMPLETED**

This repository represents a project that is **still under active development**.

The technical infrastructure is currently being established, while several components of the project still need to be designed, implemented, tested, integrated, and documented.

The project is therefore **not yet considered complete or production-ready**.

This README will be **updated regularly throughout the development process** to reflect:

- New features
- Completed milestones
- Technical changes
- Database evolution
- New analyses
- New Machine Learning models
- Dashboard development
- Test coverage
- Project results
- Remaining tasks

> **This documentation is a living document and will evolve together with the project.**

---

##  Project Objectives

The main objectives of the project are to:

1. Build a robust financial data analysis infrastructure.
2. Collect and organize financial market data.
3. Design and implement a PostgreSQL database.
4. Develop Python modules for data collection and processing.
5. Perform exploratory financial data analysis.
6. Calculate financial and statistical indicators.
7. Analyze market trends, returns, volatility, and correlations.
8. Develop relevant financial features.
9. Experiment with Machine Learning models.
10. Evaluate and compare model performance.
11. Develop an interactive dashboard.
12. Build a reproducible and maintainable data pipeline.
13. Document the entire workflow and technical architecture.

---

#  Project Architecture

The project is progressively organized around the following architecture:

    Financial_Market_Analytics/
    │
    ├── .venv/                         # Python virtual environment
    │
    ├── data/
    │   ├── raw/                       # Raw financial data
    │   ├── processed/                 # Cleaned and transformed data
    │   └── external/                  # External data sources
    │
    ├── notebooks/
    │   ├── exploration/               # Exploratory data analysis
    │   ├── analysis/                  # Financial analysis
    │   └── modeling/                  # Machine Learning experiments
    │
    ├── src/
    │   ├── data/                      # Data collection and preparation
    │   ├── features/                  # Feature engineering
    │   ├── analysis/                  # Financial analysis
    │   ├── models/                    # Statistical and ML models
    │   └── utils/                     # Utility functions
    │
    ├── database/
    │   ├── schema/                    # PostgreSQL database schema
    │   ├── migrations/                # Database migrations
    │   └── queries/                   # SQL queries
    │
    ├── dashboard/                     # Interactive dashboard
    │
    ├── tests/
    │   ├── unit/                      # Unit tests
    │   └── integration/               # Integration tests
    │
    ├── docs/
    │   └── images/                    # Documentation images and screenshots
    │
    ├── requirements.txt               # Python dependencies
    ├── .gitignore                     # Git ignored files
    └── README.md                      # Project documentation

> The project structure is not final and may be modified as development progresses.

---

#  Technical Environment

## Operating System

- Windows
- WSL 2
- Ubuntu 24.04 LTS

## Programming Language

- Python 3.12+

## Database Management System

- PostgreSQL 18
- Default port: `5432`

## Version Control

- Git
- GitHub

## Development Environment

- Visual Studio Code

## Data Science and Machine Learning

The project may use the following Python libraries depending on the requirements of each development stage:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter
- SQLAlchemy

## Dashboard

- Streamlit *(planned)*

---

#  Database

The project uses **PostgreSQL** as its relational database management system.

The planned project database is:

    financial_market_analytics

The PostgreSQL role used for the project is:

    guerin_anangmo

The database layer will progressively include:

- Database schema
- Financial asset tables
- Market data tables
- Historical price data
- Financial indicators
- Relationships between entities
- Constraints
- Indexes
- SQL queries
- Database migrations
- Data integrity checks

The database architecture will evolve as the data requirements become clearer.

---

#  Python Environment

The project uses a dedicated Python virtual environment to isolate project dependencies.

## Create the virtual environment

    python3 -m venv .venv

## Activate the virtual environment

    source .venv/bin/activate

## Upgrade pip

    python -m pip install --upgrade pip

## Install project dependencies

    pip install -r requirements.txt

---

#  Financial Data Pipeline

The planned data workflow is:

    Financial Data Sources
            │
            ▼
    Data Collection
            │
            ▼
    Raw Data
            │
            ▼
    Data Cleaning
            │
            ▼
    Data Transformation
            │
            ▼
    Feature Engineering
            │
            ▼
    PostgreSQL
            │
            ├─────────────────────┐
            ▼                     ▼
    Financial Analysis      Machine Learning
            │                     │
            └──────────┬──────────┘
                       ▼
                 Visualization
                       │
                       ▼
                   Dashboard

The pipeline will be progressively automated and improved throughout the project.

---

#  Financial Analysis

The project may include the following financial analyses:

- Price analysis
- Return analysis
- Volatility analysis
- Trend analysis
- Correlation analysis
- Descriptive statistics
- Technical indicators
- Asset comparison
- Performance analysis
- Risk analysis
- Historical market analysis
- Statistical analysis
- Model result analysis

The final analytical scope will depend on the available data and the results obtained during the exploratory phase.

---

#  Feature Engineering

Feature engineering will be used to transform raw financial data into variables that can be used for statistical analysis and Machine Learning.

Potential features may include:

- Historical returns
- Rolling returns
- Volatility
- Moving averages
- Momentum indicators
- Price changes
- Trading volume features
- Lagged variables
- Rolling statistics
- Technical indicators
- Other market-derived variables

The final feature set will be determined during the analysis and modeling stages.

---

#  Machine Learning

A major component of the project will focus on investigating the use of Machine Learning for financial prediction.

The planned workflow is:

    Raw Data
       │
       ▼
    Data Cleaning
       │
       ▼
    Feature Engineering
       │
       ▼
    Dataset Preparation
       │
       ▼
    Train / Validation / Test Split
       │
       ▼
    Model Training
       │
       ▼
    Model Evaluation
       │
       ▼
    Model Comparison
       │
       ▼
    Model Selection
       │
       ▼
    Prediction

Potential approaches may include:

- Linear models
- Tree-based models
- Ensemble methods
- Time-series approaches
- Other Machine Learning methods identified during experimentation

The final models will be selected based on the characteristics of the data and their evaluation results.

>  The Machine Learning models developed in this project are intended for **academic, educational, and experimental purposes**. They do not constitute financial advice or a guarantee of future performance.

---

#  Dashboard

An interactive dashboard is planned for a later stage of the project.

The dashboard may provide access to:

- Market data
- Asset information
- Historical prices
- Returns
- Volatility
- Financial indicators
- Statistical analysis
- Model performance
- Predictions
- Interactive charts
- Other relevant project results

The dashboard will be developed after the underlying data and analytical pipeline have reached a sufficient level of stability.

---

#  Testing

Testing will progressively be implemented throughout the project.

The testing strategy may include:

## Unit Tests

Testing individual Python functions and modules.

## Integration Tests

Testing interactions between:

- Python
- PostgreSQL
- Data pipelines
- Other project components

## Data Validation

Checking:

- Missing values
- Invalid values
- Duplicates
- Data types
- Database integrity
- Data consistency

## Model Evaluation

Machine Learning models will be evaluated using appropriate metrics depending on the prediction task.

---

#  Remaining Work

The project is **not yet completed**.

The following tasks remain to be implemented or finalized.

## Infrastructure

- [x] Set up WSL 2
- [x] Install Ubuntu
- [x] Install Python
- [x] Install Git
- [x] Install Visual Studio Code
- [x] Install PostgreSQL
- [x] Configure the PostgreSQL environment
- [ ] Finalize the Python virtual environment
- [ ] Finalize Python ↔ PostgreSQL connectivity
- [ ] Finalize the complete development environment

## Database

- [ ] Create and validate the `financial_market_analytics` database
- [ ] Design the relational database schema
- [ ] Create database tables
- [ ] Define relationships
- [ ] Define constraints
- [ ] Add indexes where appropriate
- [ ] Create SQL queries
- [ ] Implement migrations
- [ ] Test database integrity

## Data Collection

- [ ] Identify reliable financial data sources
- [ ] Define the required financial datasets
- [ ] Implement data collection scripts
- [ ] Import raw data
- [ ] Validate collected data
- [ ] Handle missing values
- [ ] Handle duplicates
- [ ] Clean and transform the data
- [ ] Load processed data into PostgreSQL

## Financial Analysis

- [ ] Perform exploratory data analysis
- [ ] Calculate descriptive statistics
- [ ] Calculate returns
- [ ] Analyze volatility
- [ ] Analyze correlations
- [ ] Develop financial indicators
- [ ] Compare financial assets
- [ ] Create financial visualizations
- [ ] Document analytical results

## Feature Engineering

- [ ] Define relevant features
- [ ] Create lagged variables
- [ ] Create rolling statistics
- [ ] Create technical indicators
- [ ] Validate feature quality
- [ ] Prepare Machine Learning datasets

## Machine Learning

- [ ] Define prediction objectives
- [ ] Define target variables
- [ ] Prepare training datasets
- [ ] Split datasets appropriately
- [ ] Train baseline models
- [ ] Train additional models
- [ ] Evaluate model performance
- [ ] Compare models
- [ ] Tune model parameters
- [ ] Validate selected models
- [ ] Document the final modeling approach

## Dashboard

- [ ] Define dashboard requirements
- [ ] Design the dashboard structure
- [ ] Develop the Streamlit application
- [ ] Connect the dashboard to PostgreSQL
- [ ] Add financial visualizations
- [ ] Add analytical results
- [ ] Add Machine Learning results
- [ ] Add prediction outputs
- [ ] Test the dashboard

## Testing and Quality

- [ ] Add unit tests
- [ ] Add integration tests
- [ ] Add data validation tests
- [ ] Improve test coverage
- [ ] Refactor the codebase
- [ ] Improve project organization

## Documentation

- [ ] Document installation
- [ ] Document database architecture
- [ ] Document data sources
- [ ] Document data processing
- [ ] Document financial analyses
- [ ] Document Machine Learning models
- [ ] Document the dashboard
- [ ] Add project screenshots
- [ ] Finalize technical documentation
- [ ] Keep README updated

---

#  Development Roadmap

The project will be developed progressively through several major stages.

    ┌──────────────────────────────────┐
    │  1. Development Environment      │
    │  WSL / Python / Git / PostgreSQL │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  2. Database                     │
    │  Schema / Tables / SQL            │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  3. Data Pipeline                │
    │  Collection / Cleaning / Storage │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  4. Financial Analysis           │
    │  Statistics / Indicators         │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  5. Feature Engineering          │
    │  Financial Features              │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  6. Machine Learning             │
    │  Training / Evaluation / Models  │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  7. Dashboard                    │
    │  Visualization / Interaction     │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  8. Testing & Documentation      │
    │  Quality / Reproducibility       │
    └────────────────┬─────────────────┘
                     │
                     ▼
    ┌──────────────────────────────────┐
    │  9. First Complete Version       │
    │  Version 1.0.0                   │
    └──────────────────────────────────┘

---

#  Version Roadmap

| Version | Status | Description |
|--------:|--------|-------------|
| 0.1.0 |  In Progress | Development environment |
| 0.2.0 |  Planned | Database implementation |
| 0.3.0 |  Planned | Data collection and pipeline |
| 0.4.0 |  Planned | Financial analysis |
| 0.5.0 |  Planned | Feature engineering |
| 0.6.0 |  Planned | Machine Learning |
| 0.7.0 |  Planned | Dashboard |
| 0.8.0 |  Planned | Testing and documentation |
| 1.0.0 |  Planned | First complete version |

> Version numbers are indicative and may be adjusted according to the actual development progress.

---

#  Screenshots

Screenshots will be added progressively as the project develops.

## Project Architecture

<!-- Insert project architecture screenshot here -->

![Project Architecture](docs/images/architecture.png)

---

## Development Environment

<!-- Insert WSL / VS Code environment screenshot here -->

![Development Environment](docs/images/development_environment.png)

---

## PostgreSQL Database

<!-- Insert PostgreSQL / pgAdmin / terminal screenshot here -->

![PostgreSQL Database](docs/images/postgresql.png)

---

## Exploratory Data Analysis

<!-- Insert exploratory analysis screenshot here -->

![Exploratory Data Analysis](docs/images/exploratory_analysis.png)

---

## Financial Visualizations

<!-- Insert financial visualization screenshot here -->

![Financial Visualizations](docs/images/visualizations.png)

---

## Machine Learning Results

<!-- Insert Machine Learning results screenshot here -->

![Machine Learning Results](docs/images/machine_learning_results.png)

---

## Dashboard

<!-- Insert dashboard screenshot here -->

![Dashboard](docs/images/dashboard.png)

---

#  Documentation

The documentation will progressively include:

- Installation guide
- Development environment configuration
- Database architecture
- Database schema
- Data sources
- Data collection process
- Data cleaning and transformation
- Financial analysis methodology
- Feature engineering methodology
- Machine Learning methodology
- Model evaluation
- Dashboard documentation
- Technical decisions
- Project results

---

#  Security

Sensitive information must **never** be committed to the GitHub repository.

The following information must not be published:

    - Database passwords
    - API keys
    - Authentication tokens
    - Private credentials
    - Sensitive personal information
    - .env files
    - Confidential datasets

Environment variables should be stored locally.

For example:

    .env

The `.gitignore` file must prevent sensitive files from being committed.

---

#  Updating the Project

As development progresses, this README should be updated whenever there are significant changes to:

- Project architecture
- Database structure
- Data sources
- Analytical methods
- Machine Learning models
- Dashboard functionality
- Installation procedures
- Project status
- Roadmap
- Results

The README is therefore considered a **living document**.

---

#  Development Workflow

Open the project from WSL:

    cd ~/Financial_Market_Analytics

Activate the Python environment:

    source .venv/bin/activate

Open the project in VS Code:

    code .

Check the Git status:

    git status

Add modified files:

    git add .

Create a commit:

    git commit -m "Describe the changes"

Push the changes to GitHub:

    git push

---

#  Installation

Clone the repository:

    git clone <REPOSITORY_URL>

Navigate to the project:

    cd Financial_Market_Analytics

Create the Python virtual environment:

    python3 -m venv .venv

Activate the environment:

    source .venv/bin/activate

Upgrade pip:

    python -m pip install --upgrade pip

Install dependencies:

    pip install -r requirements.txt

Configure PostgreSQL according to the project documentation.

---

# 👤 Author

**Alexis José Guerin Anangmo Solefack**

Financial Analysis and Prediction Project.

---

#  Disclaimer

This project is developed for **academic, educational, and experimental purposes**.

The analyses, indicators, statistical methods, Machine Learning models, and predictions produced by this project do not constitute:

- Investment advice
- Financial recommendations
- Trading recommendations
- Guarantees of future performance

Financial markets are inherently uncertain, and past performance does not guarantee future results.

---

#  License

The project license will be defined at a later stage.

---

#  Project Notice

> **Financial Market Analytics is an ongoing project.**
>
> The project is not yet complete and is continuously evolving.
>
> New features, analyses, datasets, models, tests, documentation, and improvements will be added progressively.
>
> This README will be updated regularly to accurately reflect the current state of the project.

---

**Financial Market Analytics — Work in Progress **
