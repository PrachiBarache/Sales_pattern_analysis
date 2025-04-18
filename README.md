---
# Online Retail Sales Patterns
---

##  Project Overview

This project leverages **visual analytics** to explore and understand **sales patterns, customer behavior, product performance**, and the **impact of order cancellations** using a real-world online retail dataset from Kaggle.

The primary goals are:
- To analyze temporal purchasing patterns and seasonality.
- To examine product sales variations and correlations.
- To identify frequently bought or recommended products.
- To attempt basic sales prediction modelling.


##  Research Questions

1. What is the sales pattern? Is there any seasonality?
2. How do individual product sales vary? Is there a correlation between quantity and price?
3. Can products be classified as frequently bought or most recommended?
4. Is it possible to predict the likelihood of purchasing a product?


##  Dataset

- **Source**: [Kaggle - Online Retail Transaction Data](https://www.kaggle.com/)
- **Provider**: Dr. Daqing Chen, London South Bank University
- **Scope**: 
  - Retail company based in the UK selling unique all-occasion gifts
  - Period: December 2010 to December 2011
  - ~25,900 transactions by 5,941 customers
  - 4,070 products

### important Columns:
- `InvoiceNo` – Transaction ID (cancellations start with 'C')
- `InvoiceDate` – Date & time of purchase
- `StockCode` – Product ID
- `Description` – Product name
- `Quantity` – Items purchased
- `UnitPrice` – Price per item



##  Methodology

### Using Visual Analytics Approach:
1. **Data Understanding** – Structure, data types, and distribution
2. **Data Preparation** – Handling missing values, type conversions, feature engineering
3. **Data Exploration** – EDA with Python visualizations
4. **Analytical Reasoning** – Deriving meaning from visuals
5. **Predictive Modeling** – Linear regression for basic forecasting
6. **Conclusion** – Insights drawn and limitations identified


##  Key Analyses & Findings

### Sales Pattern & Seasonality:
- Highest sales occurred in **Q4 2011** (holiday season).
- Monthly spike from **July to November**.
- Sales peak **during the morning**, with **less activity at month start and end**.

### Product Analysis:
- **Top 10 most and least sold products** identified.
- Least sold items often tagged as **damaged or defective** — valuable for inventory decisions.

###  Customer & Order Cancellations:
- No strong trend in customer purchase frequency.
- **1.72% of transactions were cancelled**, mostly between **11 AM to 2 PM** on **Thursdays**.

### Sales Prediction:
- Implemented **linear regression** to predict `Quantity` using `UnitPrice` and `CustomerID`.
- Model yielded:
  - MAE: 12.7
  - RMSE: 41.5
- **High error due to limited features** in the dataset.


##  libraries Used

- **Python**
  - `pandas`, `numpy` – Data manipulation
  - `matplotlib`, `seaborn` – Data visualization
  - `sklearn` – Predictive modeling
- **Jupyter Notebook**



## Critical Reflections

- Visual analytics helped uncover **actionable insights** (seasonality, product popularity, cancellation patterns).
- The dataset lacked **rich features** needed for robust predictive modeling.
- Visualizations provided direction for **inventory planning**, **marketing timing**, and **customer engagement strategies**.



##  References

1. Pang, S. (2022). *Retail Sales Forecast Based on Machine Learning Methods.*
2. Kaggle (2014). *Walmart Recruiting - Store Sales Forecasting.*
3. Jiang, Q. & Jiang, Y. (2022). *E-commerce customer data mining with Apriori optimization.*
4. Abdulla, H., Letizia, P., Souza, G. (2023). *Order Cancellation Behavior in Online Retailing.*
5. Keim, D., et al. (2010). *Mastering the Information Age: Solving Problems with Visual Analytics.*


