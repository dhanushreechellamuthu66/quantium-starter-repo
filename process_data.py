import pandas as pd
from pathlib import Path

data_path = Path("data")
files = list(data_path.glob("*.csv"))

dataframes = []

for file in files:
    df = pd.read_csv(file)

    df["product"] = df["product"].str.strip().str.lower()

  
    df = df[df["product"] == "pink morsel"]

  
    df["price"] = (
        df["price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .astype(float)
    )

   
    df["quantity"] = df["quantity"].astype(int)

  
    df["sales"] = df["quantity"] * df["price"]

    
    df = df[["sales", "date", "region"]]

    dataframes.append(df)

final_df = pd.concat(dataframes, ignore_index=True)

final_df.to_csv("output.csv", index=False)

print("✅ Data processing complete. Rows:", len(final_df))
