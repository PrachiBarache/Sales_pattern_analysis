from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "rfm_table.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    rfm = pd.read_csv(DATA_PATH)

    # 1. Recency distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(rfm["recency"], bins=50)
    plt.title("Recency Distribution (Days Since Last Purchase)")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "rfm_recency.png")
    plt.close()

    # 2. Frequency distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(rfm["frequency"], bins=50)
    plt.title("Purchase Frequency Distribution")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "rfm_frequency.png")
    plt.close()

    # 3. Monetary distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(rfm["monetary"], bins=50)
    plt.title("Customer Monetary Value Distribution")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "rfm_monetary.png")
    plt.close()

    print("Visuals for rfm_table.csv generated.")

if __name__ == "__main__":
    main()
