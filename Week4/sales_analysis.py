import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 60)
print("       COMPLETE SALES DATA ANALYSIS PROJECT")
print("=" * 60)

# STEP 1: Create Folders

os.makedirs("data", exist_ok=True)
os.makedirs("report/visualization", exist_ok=True)

# STEP 2: Load Dataset

try:
    file_path = "data/sales_data (1).csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError("Sales CSV file not found!")

    df = pd.read_csv(file_path)

    print("\nDataset loaded successfully!")

except Exception as e:
    print("Error:", e)
    raise SystemExit

# STEP 3: Dataset Information

print("\n1. DATASET INFORMATION")
print("-" * 60)

print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("Column Names:", list(df.columns))

print("\nFirst 5 Records:")
print(df.head().to_string(index=False))

# STEP 4: Validate Columns

required_columns = [
    "Date", "Product", "Customer_ID",
    "Region", "Quantity", "Price"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    print("\nMissing Columns:", missing_columns)
    raise SystemExit("Please check your CSV dataset.")

if df.empty:
    raise SystemExit("Dataset is empty!")

# STEP 5: Missing Values

print("\n2. MISSING VALUES")
print("-" * 60)
print(df.isnull().sum())

# STEP 6: Remove Duplicates

old_count = len(df)

df = df.drop_duplicates()

duplicates_removed = old_count - len(df)

# STEP 7: Data Cleaning

df["Date"] = pd.to_datetime(
    df["Date"], errors="coerce"
)

for col in ["Quantity", "Price"]:
    df[col] = pd.to_numeric(
        df[col], errors="coerce"
    )

df["Product"] = df["Product"].astype("string").str.strip()
df["Region"] = df["Region"].astype("string").str.strip()

df = df.dropna(
    subset=required_columns
).copy()

df = df[
    (df["Quantity"] >= 0) &
    (df["Price"] >= 0) &
    (df["Product"] != "") &
    (df["Region"] != "")
].copy()

if df.empty:
    raise SystemExit("No valid records after cleaning!")

# Calculate Total Sales

df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\n3. DATA CLEANING COMPLETED")
print("-" * 60)

print("Original Records:", old_count)
print("Duplicates Removed:", duplicates_removed)
print("Clean Records:", len(df))

# STEP 8: Sales Analysis

total_sales = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sales = df["Total_Sales"].mean()
maximum_sales = df["Total_Sales"].max()
minimum_sales = df["Total_Sales"].min()

product_sales = df.groupby("Product")["Total_Sales"].sum()

quantity_sales = df.groupby("Product")["Quantity"].sum()

region_sales = df.groupby("Region")["Total_Sales"].sum()

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))["Total_Sales"]
    .sum()
)

best_product = quantity_sales.idxmax()
top_revenue_product = product_sales.idxmax()
best_region = region_sales.idxmax()

# STEP 9: Final Sales Report

print("\n" + "=" * 60)
print("               FINAL SALES REPORT")
print("=" * 60)

print(f"Total Revenue: Rs. {total_sales:,.2f}")
print(f"Total Quantity: {total_quantity}")
print(f"Average Sales: Rs. {average_sales:,.2f}")
print(f"Highest Transaction: Rs. {maximum_sales:,.2f}")
print(f"Lowest Transaction: Rs. {minimum_sales:,.2f}")

print("Best Selling Product:", best_product)
print("Highest Revenue Product:", top_revenue_product)
print("Best Performing Region:", best_region)

# STEP 10: Bar Chart

plt.figure(figsize=(10, 6))

product_sales.sort_values(ascending=False).plot(
    kind="bar",
    title="Product Wise Sales Analysis",
    xlabel="Products",
    ylabel="Total Sales (Rs.)"
)

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("report/visualization/bar_chart.png")
plt.show()
plt.close()

print("\nBar Chart Created Successfully!")

# STEP 11: Line Chart

plt.figure(figsize=(10, 6))

monthly_sales.index = monthly_sales.index.astype(str)

monthly_sales.plot(
    kind="line",
    marker="o",
    title="Monthly Sales Trend",
    xlabel="Month",
    ylabel="Total Sales (Rs.)"
)

plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("report/visualization/line_chart.png")
plt.show()
plt.close()

print("Line Chart Created Successfully!")

# STEP 12: Pie Chart

if region_sales.sum() > 0:

    plt.figure(figsize=(8, 8))

    region_sales.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        title="Region Wise Sales Distribution"
    )

    plt.ylabel("")
    plt.tight_layout()

    plt.savefig("report/visualization/pie_chart.png")
    plt.show()
    plt.close()

    print("Pie Chart Created Successfully!")

else:
    print("Pie Chart skipped: No positive sales.")

# STEP 13: Generate Insights

insights = [
    f"{best_product} is the best-selling product.",
    f"{top_revenue_product} generates the highest revenue.",
    f"{best_region} is the best-performing region.",
    f"Total revenue is Rs. {total_sales:,.2f}.",
    f"Total quantity sold is {total_quantity}."
]

print("\n4. KEY INSIGHTS")
print("-" * 60)

for item in insights:
    print("-", item)

# STEP 14: Save Cleaned Dataset

df.to_csv(
    "data/cleaned_sales_data.csv",
    index=False
)

# STEP 15: Generate Report

report = f"""
# SALES DATA ANALYSIS REPORT

## Dataset Information

Total Records: {len(df)}
Total Columns: {len(df.columns)}
Duplicates Removed: {duplicates_removed}

## Sales Metrics

Total Revenue: Rs. {total_sales:,.2f}
Total Quantity: {total_quantity}
Average Sales: Rs. {average_sales:,.2f}
Highest Transaction: Rs. {maximum_sales:,.2f}
Lowest Transaction: Rs. {minimum_sales:,.2f}

## Key Findings

Best Selling Product: {best_product}
Highest Revenue Product: {top_revenue_product}
Best Performing Region: {best_region}

## Product Wise Sales

{product_sales.to_string()}

## Quantity Wise Sales

{quantity_sales.to_string()}

## Region Wise Sales

{region_sales.to_string()}

## Monthly Sales

{monthly_sales.to_string()}

## Important Insights

""" + "\n".join("- " + item for item in insights) + """

## Visualizations

1. Product Wise Bar Chart
2. Monthly Sales Line Chart
3. Region Wise Pie Chart

## Conclusion

Sales data was successfully loaded, cleaned,
analyzed and visualized using Python, Pandas
and Matplotlib.

The project provides meaningful insights
into products, regions and monthly sales.

Project Completed Successfully!
"""

with open(
    "report/analysis_report.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(report)

# STEP 16: Completion

print("\n" + "=" * 60)
print("       PROJECT COMPLETED SUCCESSFULLY!")
print("=" * 60)

print("Generated Files:")
print("1. data/cleaned_sales_data.csv")
print("2. report/visualization/bar_chart.png")
print("3. report/visualization/line_chart.png")
print("4. report/visualization/pie_chart.png")
print("5. report/analysis_report.md")

print("=" * 60)
