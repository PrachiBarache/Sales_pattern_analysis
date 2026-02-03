from pathlib import Path
import pandas as pd

from datacleaning import data_load_to_clean
from featureengineering import compute_rfm
from anlysisbasket import prepare_basket, generate_rules

RAW_PATH = Path("/data/online_retail.csv")
PROCESSED_DIR = Path("data/processed")

def main():
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Clean data
    df = data_load_to_clean(RAW_PATH)
    df.to_csv(PROCESSED_DIR / "clean_transactions.csv", index=False)

    # Step 2: RFM
    rfm = compute_rfm(df)
    rfm.to_csv(PROCESSED_DIR / "rfm_table.csv", index=False)

    # Step 3: Basket analysis
    basket = prepare_basket(df)
    rules = generate_rules(basket)
    rules.to_csv(PROCESSED_DIR / "basket_rules.csv", index=False)

    print("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
