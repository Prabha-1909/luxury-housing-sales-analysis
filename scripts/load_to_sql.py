import pandas as pd
from sqlalchemy import create_engine, text

# 🔹 1. Create connection
engine = create_engine(
    "postgresql://postgres:1909@localhost:5432/realestate"
)

# 🔹 2. Load cleaned CSV
df = pd.read_csv("data/processed/luxury_housing_cleaned.csv")

# 🔹 3. Create table
create_table_query = """
CREATE TABLE IF NOT EXISTS luxury_housing (
    project_id VARCHAR(50),
    micro_market VARCHAR(100),
    builder VARCHAR(100),
    ticket_price_cr FLOAT,
    configuration VARCHAR(20),
    possession_status VARCHAR(50),
    amenity_score FLOAT,
    booking_status VARCHAR(50),
    purchase_quarter VARCHAR(20),
    sales_channel VARCHAR(50),
    buyer_type VARCHAR(50),
    buyer_comments TEXT,
    price_per_sqft FLOAT,
    booking_flag INT
);
"""

with engine.connect() as conn:
    conn.execute(text(create_table_query))
    conn.commit()

# 🔹 4. Insert data
df.to_sql("luxury_housing", engine, if_exists="replace", index=False)

print("✅ Data successfully loaded!")

# 🔹 5. Validate
with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM luxury_housing;"))
    for row in result:
        print("Total rows in table:", row[0])