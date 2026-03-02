--Total Row Count
SELECT COUNT(*) AS total_rows
FROM luxury_housing;

--Null Check (Important Columns)
SELECT COUNT(*) 
FROM luxury_housing
WHERE "Ticket_Price_Cr" IS NULL;

--Duplicate Check
SELECT "Property_ID", COUNT(*)
FROM luxury_housing
GROUP BY "Property_ID"
HAVING COUNT(*) > 1;

--Booking Status Distribution (Basic sanity check)
SELECT "Transaction_Type", COUNT(*)
FROM luxury_housing
GROUP BY "Transaction_Type";