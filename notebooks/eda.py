import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.datacleaning import data_load_to_clean

df = data_load_to_clean("data/raw/online_retail.csv")
# Revenue concentration
customer_revenue = df.groupby("CustomerID")["TotalPrice"].sum()
customer_revenue.describe()
sns.histplot(customer_revenue, bins=50)
plt.title("Customer Revenue Distribution")
