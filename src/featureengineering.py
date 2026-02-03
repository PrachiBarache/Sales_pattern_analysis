import pandas as pd
from datetime import datetime

def compute_rfm(df: pd.DataFrame) -> pd.DataFrame:
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

    rfm = (
        df.groupby("CustomerID")
        .agg(
            recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
            frequency=("InvoiceNo", "nunique"),
            monetary=("TotalPrice", "sum")
        )
        .reset_index()
    )

    return rfm


def assign_rfm_scores(rfm: pd.DataFrame) -> pd.DataFrame:
    rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
    rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
    rfm["M"] = pd.qcut(rfm["monetary"], 5, labels=[1,2,3,4,5])

    rfm["RFM_Score"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)

    return rfm
