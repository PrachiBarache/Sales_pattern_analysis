from pathlib import Path

from datacleaning import data_load_to_clean
from featureengineering import compute_rfm
from anlysisbasket import prepare_basket, generate_rules

# Project root = parent of src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_PATH = PROJECT_ROOT / "data" / "online_retail.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
# Project root = parent of src/
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_PATH = PROJECT_ROOT / "data" / "online_retail.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    df = data_load_to_clean(RAW_PATH)
    df = data_load_to_clean(RAW_PATH)
    df.to_csv(PROCESSED_DIR / "clean_transactions.csv", index=False)

    rfm = compute_rfm(df)
    rfm.to_csv(PROCESSED_DIR / "rfm_table.csv", index=False)

    basket = prepare_basket(df)
    rules = generate_rules(basket)
    rules.to_csv(PROCESSED_DIR / "basket_rules.csv", index=False)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
