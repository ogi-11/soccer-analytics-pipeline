# Soccer Analytics & Match Outcome Prediction Pipeline

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.5-blue?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.2-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Lab-orange?style=for-the-badge&logo=jupyter&logoColor=white)

## Project Overview

This project represents a complete, end-to-end data science workflow for soccer analytics. It demonstrates skills in automated web scraping, data engineering, exploratory data analysis (EDA), feature engineering, and predictive modeling.

The pipeline automates the acquisition of granular player-level data and team-level league standings from [fbref.com](https://fbref.com/) across multiple seasons. This raw data is then systematically cleaned, processed, standardized, and integrated into a single, master analysis-ready dataset. Finally, machine learning models are trained and evaluated to predict match outcomes based on the engineered features.

---

## Project Workflow & Key Features

The project is structured as a sequential pipeline, with each notebook and script performing a distinct task.

*   **1. Automated Data Acquisition (`scripts/`):**
    *   A robust Python scraper using `requests` and `BeautifulSoup4` to gather detailed player and team statistics for multiple seasons.
    *   Intelligently handles varying page structures and league statuses.

*   **2. Data Cleaning and Engineering (`notebooks/03_...`):**
    *   A systematic data processing pipeline built with `pandas` to handle missing values, correct data types, standardize naming conventions, and merge disparate data sources.
    *   Creates a single, unified `MASTER.csv` file that serves as the "single source of truth" for all subsequent analysis.

*   **3. Exploratory Data Analysis (EDA) (`notebooks/04_...`):**
    *   In-depth analysis using `matplotlib` and `seaborn` to uncover statistical properties, distributions, and key relationships within the data.
    *   Identifies key trends and potential predictive features.

*   **4. Feature Engineering (`notebooks/04_...`):**
    *   Creation of time-aware "lag" features to represent team form and player performance over recent matches.
    *   Development of composite team-level metrics aggregated from individual player data.

*   **5. Predictive Modeling & Simulation (`notebooks/05_...`):**
    *   Development and rigorous evaluation of machine learning models (e.g., Logistic Regression, XGBoost) using `scikit-learn`.
    *   Implementation of a walk-forward validation structure to simulate real-world prediction scenarios and prevent look-ahead bias.
    *   Final presentation of model performance, including accuracy, ROC AUC, classification reports, and feature importance analysis.

---

## Tech Stack

*   **Language:** Python 3.11+
*   **Core Libraries:** `pandas`, `numpy` for data manipulation.
*   **Web Scraping:** `requests`, `beautifulsoup4`
*   **Machine Learning:** `scikit-learn`, `xgboost`
*   **Data Visualisation:** `matplotlib`, `seaborn`
*   **Development Environment:** Jupyter Notebooks

---

## How to Run This Project

To reproduce this analysis, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/soccer-analytics-pipeline.git
    cd soccer-analytics-pipeline
    ```

2.  **Install dependencies:**
    It is recommended to create a virtual environment first. Then, install the required packages.
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file by running `pip freeze > requirements.txt` in your terminal.)*

3.  **Run the pipeline in order:**
    *   Execute the scraper in `scripts/01_player_data_scraper.py` to gather the raw player data.
    *   Run the notebooks in the `notebooks/` directory sequentially from `02` to `05`.
    *   *Note: The scraping steps may take a significant amount of time to complete.*

---

## Key Results & Findings

*(This is where you would showcase your final result. You would replace the bracketed text with your actual findings from notebook 05)*

The final predictive model achieved an out-of-sample **[Accuracy of XX.X%]** and an **[ROC AUC of 0.XX]**. The feature importance analysis revealed that **[Your Most Important Feature, e.g., 'recent_team_form']** was the most significant predictor of match outcomes.

*(Optional: You can embed one of your key result images here, for example, the feature importance plot)*

![Feature Importance Plot](path/to/your/feature_importance_plot.png)
