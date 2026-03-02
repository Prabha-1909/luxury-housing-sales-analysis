# 🏢 Luxury Housing Sales Analysis

## 📌 Project Overview

This project analyzes luxury housing sales data to generate business insights using a complete end-to-end data pipeline.

The goal is to:
- Clean and validate real estate sales data
- Store structured data in PostgreSQL
- Perform SQL-based business analysis
- Build a Power BI dashboard using DirectQuery
- Extract actionable insights for decision-makers

---

## 🛠️ Tech Stack

- **Python** – Data Cleaning & ETL
- **PostgreSQL** – Data Storage & SQL Analysis
- **Power BI (DirectQuery Mode)** – Interactive Dashboard
- **VS Code** – Development Environment

---

## 📂 Project Structure

LUXURY HOUSING SALES ANALYSIS
│
├── data/
│ ├── raw/ # Original dataset
│ └── processed/ # Cleaned dataset
│
├── scripts/
│ ├── data_cleaning.py
│ ├── data_inspection.py
│ └── load_to_sql.py
│
├── sql/
│ ├── 01_table_schema.sql
│ ├── 02_data_validation.sql
│ └── 03_aggregation_queries.sql
│
├── powerbi/
│ └── Luxury_Housing_DirectQuery.pbix
│
└── README.md


---

## 🔄 Data Pipeline Flow

Raw CSV Data  
→ Data Cleaning using Python  
→ Load Clean Data into PostgreSQL  
→ SQL Validation & Aggregation Queries  
→ Power BI DirectQuery Dashboard  
→ Business Insights Generation  

---

## 📊 Key Business Insights

- 📈 Top 5 Builders by Revenue
- 🏘️ Micro-Market Performance Analysis
- 💰 Average Ticket Price Trends
- 🌍 NRI vs Domestic Buyer Segmentation
- 🚦 Connectivity & Infrastructure Impact on Pricing
- 📦 Sales Channel Performance
- 🏗️ Possession Status Distribution

---

## 🧠 Example SQL Analysis

### Top Builders by Revenue

```sql
SELECT Developer_Name,
       SUM(Ticket_Price_Cr) AS Total_Revenue
FROM luxury_housing
GROUP BY Developer_Name
ORDER BY Total_Revenue DESC
LIMIT 5;

Average Price by Micro Market
SELECT Micro_Market,
       AVG(Ticket_Price_Cr) AS Avg_Price
FROM luxury_housing
GROUP BY Micro_Market
ORDER BY Avg_Price DESC;

📊 Power BI Dashboard Features

KPI Cards (Revenue, Avg Price, Units Sold)

Builder Performance Ranking

Buyer Segmentation Analysis

Interactive Filters (Quarter, Micro Market, Builder)

Geographic Visualization

DirectQuery live connection to PostgreSQL

🚀 How to Run This Project

Clone repository

Create PostgreSQL database

Run 01_table_schema.sql

Run Python scripts in /scripts

Execute validation queries

Open Power BI file and connect to PostgreSQL

🎯 Project Outcome

This project demonstrates:

End-to-end data pipeline development

SQL analytics expertise

ETL implementation

Business intelligence dashboard creation

Real-world real estate analytics use case

