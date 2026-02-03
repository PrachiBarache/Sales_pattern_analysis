import pandas as pd

def data_load_to_clean(path:str)->pd.DataFrame:
    df = pd.read_csv(path, encoding="ISO-8859-1")
    # Standardise column names
    df.columns = df.columns.str.strip()

    # Drop rows with missing customer IDs
    df = df.dropna(subset=["CustomerID"])

    # Convert date
    df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

    # Remove cancelled transactions
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

    # Remove negative or zero quantities
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

    # Create total price
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df
