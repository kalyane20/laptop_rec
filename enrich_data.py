import pandas as pd
import re

def extract_details(text):
    brand_match = re.match(r'^(\w+)', text)
    brand = brand_match.group(1) if brand_match else None

    ram_match = re.search(r'(\d+\s?GB)', text)
    ram = ram_match.group(1) if ram_match else None

    if 'Thin and Light' in text:
        weight = 'Thin and Light'
    else:
        weight_match = re.search(r'(\d+\.\d+\s?kg)', text, re.IGNORECASE)
        weight = weight_match.group(1) if weight_match else None

    return pd.Series([brand, ram, weight])

def extract_price_info(text):
    text = text.replace(',', '')
    price_matches = re.findall(r'₹(\d+)', text)
    selling_price = int(price_matches[0]) if len(price_matches) > 0 else None
    original_price = int(price_matches[1]) if len(price_matches) > 1 else None
    discount_match = re.search(r'(\d+)%\s*off', text.lower())
    discount = int(discount_match.group(1)) if discount_match else None
    return pd.Series([selling_price, original_price, discount])

def enrich_and_save_csv(input_path="flipkart_laptops_dataset.csv", output_path="flipkart_laptops_enriched.csv"):
    df = pd.read_csv(input_path)
    df[['Brand', 'RAM', 'Weight']] = df['Product Name'].apply(extract_details)
    df[['Selling_Price', 'Original_Price', 'Discount_Percent']] = df['Price'].apply(extract_price_info)
    df['text'] = df.apply(lambda row: f"Model: {row['Product Name']}, RAM: {row['RAM']}, Specs: {row['Specifications']}, Price: {row['Selling_Price']}, Rating: {row['Rating']}", axis=1)
    df.columns = df.columns.str.strip()
    df.to_csv(output_path, index=False)
    print(f"✅ Enriched CSV saved to: {output_path}")

if __name__ == "__main__":
    enrich_and_save_csv()
