# Zomato Data Analysis Using Python

This project performs exploratory data analysis (EDA) on a Zomato restaurant dataset using Python libraries such as Pandas and Seaborn. The analysis includes data cleaning, visualization, and insights extraction to understand trends in restaurant ratings, costs, cuisines, and more.

---

## Project Overview

- Load and clean the Zomato dataset.
- Handle missing values and duplicates.
- Rename and format columns for easier analysis.
- Convert relevant columns to appropriate data types.
- Generate multiple visualizations:
  - Bar plots for popular restaurants and cuisines.
  - Count plots for online ordering availability.
  - Histograms for cost distribution.
  - Scatter plots to study relationship between cost and rating.
  - Pie charts showing distribution of restaurant types.
  - Bar charts for restaurant locations.
- Export the cleaned dataset as a CSV file for further use.

---

## Dataset

The dataset used (`zomato.csv`) contains restaurant details including:

- Restaurant ID and name
- Location and city
- Types of cuisine offered
- Cost for two people
- Online ordering and table booking availability
- Ratings and votes
- Other restaurant metadata

---

## Requirements

Make sure to have the following Python libraries installed:

- pandas
- seaborn
- matplotlib (usually required by seaborn)

You can install them using pip:

```bash
pip install pandas seaborn matplotlib
