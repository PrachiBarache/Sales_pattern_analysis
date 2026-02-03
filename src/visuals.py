from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from datacleaning import data_load_to_clean

# Paths
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "online_retail.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

def plot_revenue_distribution(df):
    customer_revenue = df.groupby("CustomerID")["TotalPrice"].sum()

    plt.figure(figsize=(8, 5))
    sns.histplot(customer_revenue, bins=50)
    plt.title("Customer Revenue Distribution")
    plt.xlabel("Total Revenue per Customer")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "revenue_distribution.png")
    plt.close()


def plot_top_customers(df):
    customer_revenue = (
        df.groupby("CustomerID")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 5))
    customer_revenue.plot(kind="bar")
    plt.title("Top 10 Customers by Revenue")
    plt.xlabel("Customer ID")
    plt.ylabel("Total Revenue")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "top_customers_revenue.png")
    plt.close()


def plot_monthly_revenue(df):
    df["Month"] = df["InvoiceDate"].dt.to_period("M")

    monthly_revenue = df.groupby("Month")["TotalPrice"].sum()

    plt.figure(figsize=(10, 5))
    monthly_revenue.plot()
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "monthly_revenue_trend.png")
    plt.close()


def plot_country_revenue(df):
    country_revenue = (
        df.groupby("Country")["TotalPrice"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(8, 5))
    country_revenue.plot(kind="bar")
    plt.title("Top 10 Countries by Revenue")
    plt.xlabel("Country")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "country_revenue.png")
    plt.close()


def plot_basket_size(df):
    basket_size = df.groupby("InvoiceNo")["Quantity"].sum()

    plt.figure(figsize=(8, 5))
    sns.histplot(basket_size, bins=50)
    plt.title("Basket Size Distribution")
    plt.xlabel("Items per Order")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "basket_size_distribution.png")
    plt.close()


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = data_load_to_clean(RAW_PATH)

    plot_revenue_distribution(df)
    plot_top_customers(df)
    plot_monthly_revenue(df)
    plot_country_revenue(df)
    plot_basket_size(df)

    print("EDA visuals generated successfully.")


if __name__ == "__main__":
    main()
