from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "clean_transactions.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(DATA_PATH, parse_dates=["InvoiceDate"])

    # 1. Revenue distribution per customer
    customer_revenue = df.groupby("CustomerID")["TotalPrice"].sum()

    plt.figure(figsize=(8, 5))
    sns.histplot(customer_revenue, bins=50)
    plt.title("Customer Revenue Distribution")
    plt.xlabel("Total Revenue")
    plt.ylabel("Number of Customers")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "transactions_customer_revenue.png")
    plt.close()

    # 2. Basket size distribution
    basket_size = df.groupby("InvoiceNo")["Quantity"].sum()

    plt.figure(figsize=(8, 5))
    sns.histplot(basket_size, bins=50)
    plt.title("Basket Size Distribution")
    plt.xlabel("Items per Order")
    plt.ylabel("Number of Orders")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "transactions_basket_size.png")
    plt.close()

    # 3. Monthly revenue trend
    df["Month"] = df["InvoiceDate"].dt.to_period("M")
    monthly_revenue = df.groupby("Month")["TotalPrice"].sum()

    plt.figure(figsize=(10, 5))
    monthly_revenue.plot()
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "transactions_monthly_revenue.png")
    plt.close()

    print("Visuals for clean_transactions.csv generated.")

if __name__ == "__main__":
    main()
