from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "basket_rules.csv"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    rules = pd.read_csv(DATA_PATH)

    # 1. Lift distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(rules["lift"], bins=50)
    plt.title("Lift Distribution of Association Rules")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "basket_lift_distribution.png")
    plt.close()

    # 2. Confidence distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(rules["confidence"], bins=50)
    plt.title("Confidence Distribution of Association Rules")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "basket_confidence_distribution.png")
    plt.close()

    print("Visuals for basket_rules.csv generated.")

if __name__ == "__main__":
    main()
