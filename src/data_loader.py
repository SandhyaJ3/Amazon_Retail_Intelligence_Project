from pathlib import Path
import pandas as pd

print("===== DEBUGGING PATHS =====")
print("__file__ =", __file__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
print("PROJECT_ROOT =", PROJECT_ROOT)

DATA_DIR = PROJECT_ROOT / "data" / "raw"
print("DATA_DIR =", DATA_DIR)
print("DATA_DIR exists?", DATA_DIR.exists())

print("amazon file exists?", (DATA_DIR / "amazon_retail_data.csv").exists())
print("===========================")


def load_data():
    orders = pd.read_csv(DATA_DIR / "amazon_retail_data.csv")
    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")

    df = (
        orders
        .merge(customers, on="customer_id", how="left")
        .merge(products, on="product_id", how="left")
    )

    return df