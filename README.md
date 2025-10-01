# Job Prospects for Mathematics PhDs in the EU: A Data-Driven Analysis

## About This Project

As a recent PhD graduate in Mathematics, I created this project to explore a question of both personal and professional interest: what are the real job prospects for mathematics PhDs in the European Union? This analysis is my attempt to answer that question using a data-driven approach, and to share my findings with the broader academic and professional community.

This project goes beyond a simple analysis of employment rates. It delves into the nuances of the job market, exploring career paths, salary expectations, gender disparities, and the impact of different policy scenarios. My hope is that this work will be a valuable resource for current and future PhD students, as well as for anyone interested in the career trajectories of highly-skilled individuals in the EU.

## Key Findings

This analysis reveals a generally positive outlook for mathematics PhDs in the EU, but also highlights some important challenges and variations across countries and sectors.

*   **High Employability:** The average employment rate for mathematics PhDs is **95.7%** within one year of graduation, rising to **97.6%** within three years.
*   **Diverse Career Paths:** While academia is still the most common path (69%), a significant number of PhDs are finding opportunities in industry (21%) and government (10%).
*   **The Industry Advantage:** The industry sector offers a substantial **47% salary premium** compared to academia, with an average monthly salary of €4,158 versus €2,849.
*   **Gender Gap:** A persistent gender gap of **1.8 percentage points** in employment rates exists, favoring men.
*   **Skills in Demand:** A high percentage of PhDs (**77.5%**) report that their doctoral skills are used extensively in their jobs.

## Project Highlights

This project demonstrates a comprehensive data analysis workflow, including:

*   **Data Collection and Integration:** Gathering data from multiple sources, including the Eurostat API, and integrating them into a cohesive dataset.
*   **Exploratory Data Analysis:** A deep dive into the data to uncover trends and insights, visualized through a comprehensive dashboard.
*   **Predictive Modeling:** Using machine learning models (Linear Regression, Random Forest, Gradient Boosting) to predict employment outcomes and perform scenario analysis.
*   **Policy Recommendations:** Providing evidence-based policy recommendations based on the analysis.

## How to Run This Project

To run this analysis, you will need Python and Jupyter Notebook. You can install the required libraries using pip:

```bash
pip install pandas numpy matplotlib seaborn plotly folium scikit-learn statsmodels requests beautifulsoup4 eurostat
```

Once the dependencies are installed, you can run the notebook:

```bash
jupyter notebook EU_PhDs_Data_Analysis.ipynb
```

## Data Sources

This analysis uses data from a variety of sources to provide a comprehensive view of the job market:

*   **Eurostat:** For PhD graduation data.
*   **AlmaLaurea:** For employment outcomes and salaries of Italian PhDs.
*   **OECD Careers of Doctorate Holders (CDH) project:** For international career data.
*   **ESF Career Tracking:** For European-wide PhD employment and mobility patterns.
*   **OECD Employment Database:** For broader labor market indicators.