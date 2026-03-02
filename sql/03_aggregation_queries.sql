--Total Revenue by Builder
SELECT 
    "Builder",
    SUM("Ticket_Price_Cr") AS total_revenue_cr
FROM luxury_housing
GROUP BY "Builder"
ORDER BY total_revenue_cr DESC;

--Total Transactions by Developer
SELECT 
    "Developer_Name",
    COUNT(*) AS total_transactions
FROM luxury_housing
GROUP BY "Developer_Name"
ORDER BY total_transactions DESC;

--Average Ticket Price per Developer
SELECT 
    "Developer_Name",
    AVG("Ticket_Price_Cr") AS avg_ticket_price_cr
FROM luxury_housing
GROUP BY "Developer_Name"
ORDER BY avg_ticket_price_cr DESC;

--Revenue by Micro Market
SELECT 
    "Micro_Market",
    SUM("Ticket_Price_Cr") AS total_revenue_cr
FROM luxury_housing
GROUP BY "Micro_Market"
ORDER BY total_revenue_cr DESC;

--Booking / Transaction Type Distribution
SELECT 
    "Transaction_Type",
    COUNT(*) AS transaction_count
FROM luxury_housing
GROUP BY "Transaction_Type"
ORDER BY transaction_count DESC;

--Average Price Per Sqft by Micro Market
SELECT 
    "Micro_Market",
    AVG("Ticket_Price_Cr" / "Unit_Size_Sqft") AS avg_price_per_sqft
FROM luxury_housing
GROUP BY "Micro_Market"
ORDER BY avg_price_per_sqft DESC;