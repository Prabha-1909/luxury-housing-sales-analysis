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
