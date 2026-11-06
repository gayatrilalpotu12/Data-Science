
import pandas as pd

print("=" * 55)
print("           SALES DATA ANALYSIS PROJECT")
print("=" * 55)

# STEP 1: Load Dataset
df = pd.read_csv("sales_data.csv")

print("\n1. DATASET LOADED SUCCESSFULLY")
print("-" * 55)

# STEP 2: Display First 5 Rows
print("\n2. FIRST 5 RECORDS")
print(df.head().to_string(index=False))

# STEP 3: Dataset Information
print("\n3. DATASET INFORMATION")
print("-" * 55)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Column Names:", list(df.columns))

# STEP 4: Check Data Types
print("\n4. DATA TYPES")
print(df.dtypes.to_string())

# STEP 5: Check Missing Values
print("\n5. MISSING VALUES")
print(df.isnull().sum().to_string())

# STEP 6: Remove Duplicate Records
old_count = len(df)
df = df.drop_duplicates()
duplicates_removed = old_count - len(df)

# STEP 7: Data Cleaning
df["Date"] = pd.to_datetime(
    df["Date"],
    format="%Y-%m-%d",
    errors="coerce"
)

for col in ["Quantity", "Price", "Total_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(
    subset=[
        "Date", "Product", "Customer_ID",
        "Region", "Quantity", "Price"
    ]
)

df = df[
    (df["Quantity"] >= 0) &
    (df["Price"] >= 0)
].copy()

# Calculate Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\n6. DATA CLEANING COMPLETED")
print("-" * 55)
print("Remaining Records:", len(df))
print("Duplicate Records Removed:", duplicates_removed)

# STEP 8: Calculate Sales Metrics
total_sales = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Total_Sales"].mean()
maximum_sales = df["Total_Sales"].max()
minimum_sales = df["Total_Sales"].min()

# STEP 9: Best Selling Product
product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()

# STEP 10: Highest Revenue Product
revenue_product = df.groupby("Product")["Total_Sales"].sum()
top_revenue_product = revenue_product.idxmax()

# STEP 11: Region Analysis
region_sales = df.groupby("Region")["Total_Sales"].sum()
best_region = region_sales.idxmax()

# STEP 12: Monthly Sales Analysis
monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)
monthly_sales.index = monthly_sales.index.astype(str)

# STEP 13: Display Final Report
print("\n")
print("=" * 55)
print("               FINAL SALES REPORT")
print("=" * 55)

print(f"\nTotal Revenue          : Rs. {total_sales:,.2f}")
print(f"Total Quantity Sold    : {total_quantity}")
print(f"Average Sales          : Rs. {average_sales:,.2f}")
print(f"Highest Transaction    : Rs. {maximum_sales:,.2f}")
print(f"Lowest Transaction     : Rs. {minimum_sales:,.2f}")
print(f"Best Selling Product   : {best_product}")
print(f"Highest Revenue Product: {top_revenue_product}")
print(f"Best Performing Region : {best_region}")

print("\n" + "=" * 55)
print("             PRODUCT-WISE SALES")
print("=" * 55)
print(revenue_product.sort_values(ascending=False).to_string())

print("\n" + "=" * 55)
print("             QUANTITY-WISE SALES")
print("=" * 55)
print(product_sales.sort_values(ascending=False).to_string())

print("\n" + "=" * 55)
print("              REGION-WISE SALES")
print("=" * 55)
print(region_sales.sort_values(ascending=False).to_string())

print("\n" + "=" * 55)
print("              MONTHLY SALES")
print("=" * 55)
print(monthly_sales.to_string())

# STEP 14: Save Analysis Report
report = f"""
# SALES DATA ANALYSIS REPORT

## Dataset Information
Total Records: {len(df)}
Total Columns: {len(df.columns)}

## Sales Metrics
Total Revenue: Rs. {total_sales:,.2f}
Total Quantity: {total_quantity}
Average Sales: Rs. {average_sales:,.2f}
Highest Sale: Rs. {maximum_sales:,.2f}
Lowest Sale: Rs. {minimum_sales:,.2f}

## Key Findings
Best Selling Product: {best_product}
Highest Revenue Product: {top_revenue_product}
Best Performing Region: {best_region}

## Product Revenue
{revenue_product.to_string()}

## Quantity-Wise Sales
{product_sales.to_string()}

## Regional Revenue
{region_sales.to_string()}

## Monthly Sales
{monthly_sales.to_string()}

## Conclusion
Sales data was analyzed successfully using Python Pandas.
Data cleaning, grouping, calculations and reporting
were completed successfully.
"""

with open("analysis_report.md", "w", encoding="utf-8") as f:
    f.write(report)

# Save Cleaned Dataset
df.to_csv("cleaned_sales_data.csv", index=False)

# STEP 15: Project Completion
print("\n")
print("=" * 55)
print("       PROJECT COMPLETED SUCCESSFULLY!")
print("       Report: analysis_report.md")
print("       Clean Data: cleaned_sales_data.csv")
print("=" * 55)
