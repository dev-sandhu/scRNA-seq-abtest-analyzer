import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of product page
url = "https://www.10xgenomics.com/products/single-cell-gene-expression"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# For now, we use hardcoded details
data = {
    "Company": ["10x Genomics"],
    "Product Name": ["Chromium Single Cell 3’ Gene Expression"],
    "Cell Throughput": ["10,000 – 100,000 cells"],
    "Protocol Time": ["<1 day"],
    "Chemistry": ["3’ gene expression"],
    "Price (est.)": ["~$500/sample"]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("products.csv", index=False)
print("✅ Data saved to products.csv")
