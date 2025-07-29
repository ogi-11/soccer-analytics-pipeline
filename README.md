# Premier League Predictive Analytics Pipeline

A comprehensive data pipeline and modeling project designed to scrape, clean, and analyse player and team statistics from the English Premier League, with the ultimate goal of building a predictive model for team performance.

---

## Project Overview

This project represents an end-to-end data science workflow, demonstrating skills in web scraping, data engineering, exploratory data analysis (EDA), and machine learning. It automates the acquisition of granular player-level data and team-level league standings from [fbref.com](https://fbref.com/) over multiple seasons. The raw data is then systematically cleaned, processed, standardised, and integrated into a single, master dataset.

### Key Features

*   **Automated Data Acquisition:** A robust Python scraper using `requests` and `BeautifulSoup` to gather player and team data, intelligently handling multiple seasons and varying league statuses.
*   **Rigorous Data Engineering:** A systematic data processing pipeline built with `pandas` to handle missing values, correct data types, standardise naming conventions, and merge disparate data sources.
*   **In-Depth EDA:** Exploratory Data Analysis using `matplotlib` and `seaborn` to uncover statistical properties, distributions, and key relationships within the data.
*   **(In Progress) Feature Engineering:** Creation of time-aware "lag" features and composite team-level metrics from player data.
*   **(Planned) Predictive Modeling:** Development of machine learning models using `scikit-learn` and `Pytorch` to predict season outcomes based on the engineered features.

---

## Tech Stack

*   **Language:** Python 3.11+
*   **Core Libraries:** pandas, NumPy
*   **Web Scraping:** requests, BeautifulSoup4
*   **Data Visualisation:** matplotlib, seaborn
*   **Development Environment:** Jupyter Notebooks
