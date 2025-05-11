import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of Mission Bio's Tapestri Platform page
url = "https://missionbio.com/product/"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Pull text from paragraphs
paragraphs = soup.find_all("p")
text_blocks = [p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50]

# Preview text to manually verify what’s coming in
print("🔍 Sample Mission Bio content:")
for t in text_blocks[:5]:
    print("-", t)

# For now, enter key details manually based on what we know
data = {
    "Company": ["Mission Bio"],
    "Product Name": ["Tapestri Platform"],
    "Cell Throughput": ["10,000+ cells/sample"],
    "Protocol Time": ["1 day (library prep)"],
    "Chemistry": ["DNA and protein multi-omics"],
    "Price (est.)": ["~$600/sample"]
}

df = pd.DataFrame(data)

# Save to CSV
df.to_csv("products_missionbio.csv", index=False)
print("✅ Data saved to products_missionbio.csv")
