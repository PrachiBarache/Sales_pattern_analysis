import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def prepare_basket(df: pd.DataFrame) -> pd.DataFrame:
    basket = (
        df.groupby(["InvoiceNo", "Description"])["Quantity"]
        .sum()
        .unstack()
        .fillna(0)
    )
    return basket.applymap(lambda x: 1 if x > 0 else 0)


def generate_rules(basket: pd.DataFrame) -> pd.DataFrame:
    frequent_items = apriori(basket, min_support=0.02, use_colnames=True)
    rules = association_rules(frequent_items, metric="confidence", min_threshold=0.4)
    return rules.sort_values("lift", ascending=False)
