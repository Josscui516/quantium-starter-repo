import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

files = [
    DATA_DIR / "daily_sales_data_0.csv",
    DATA_DIR / "daily_sales_data_1.csv",
    DATA_DIR / "daily_sales_data_2.csv",
]

df_list = [pd.read_csv(file) for file in files]
df = pd.concat(df_list, ignore_index=True)

df = df[df["product"] == "pink morsel"]

df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

df["sales"] = df["price"] * df["quantity"]

final_df = df[["sales", "date", "region"]]

output_path = DATA_DIR / "processed_sales_data.csv"
final_df.to_csv(output_path, index=False)

print(f"Processed data saved to {output_path}")
