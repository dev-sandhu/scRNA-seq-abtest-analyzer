import pandas as pd

# Read all individual files
df_10x = pd.read_csv("products.csv")
df_parse = pd.read_csv("products_parsebio.csv")
df_mission = pd.read_csv("products_missionbio.csv")

# Merge into one
all_df = pd.concat([df_10x, df_parse, df_mission], ignore_index=True)

# Save merged file
all_df.to_csv("all_products.csv", index=False)
print("✅ Merged 10x, Parse Bio, and Mission Bio into all_products.csv")
