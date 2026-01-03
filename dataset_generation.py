import numpy as np
import pandas as pd

np.random.seed(42)

# ----------------------------
# Configuration
# ----------------------------
N_PRODUCTS = 10
DAYS = 365
START_DATE = "2023-01-01"

products = [f"P{i+1}" for i in range(N_PRODUCTS)]

# Product-specific parameters
base_prices = np.random.uniform(80, 200, N_PRODUCTS)
base_demands = np.random.uniform(50, 200, N_PRODUCTS)
elasticities = np.random.uniform(-2.5, -0.3, N_PRODUCTS)  # realistic range

dates = pd.date_range(start=START_DATE, periods=DAYS)

data = []

# ----------------------------
# Simulation Loop
# ----------------------------
for pid, base_price, base_demand, elasticity in zip(
    products, base_prices, base_demands, elasticities
):
    for date in dates:
        
        # Seasonality (weekly + yearly)
        weekly = 1 + 0.1 * np.sin(2 * np.pi * date.dayofweek / 7)
        yearly = 1 + 0.2 * np.sin(2 * np.pi * date.dayofyear / 365)
        seasonality = weekly * yearly
        
        # Competitor pricing
        competitor_price = base_price * np.random.normal(1.0, 0.05)
        
        # Discount logic
        discount_pct = np.random.choice([0, 0.05, 0.1, 0.2], p=[0.6, 0.15, 0.15, 0.1])
        price = base_price * (1 - discount_pct)
        
        # Promotion boost
        promo_multiplier = 1 + (discount_pct * 1.5)
        
        # Demand calculation
        demand = (
            base_demand
            * (price / base_price) ** elasticity
            * seasonality
            * promo_multiplier
            * np.random.normal(1.0, 0.1)
        )
        
        demand = max(0, int(demand))
        revenue = price * demand
        
        data.append([
            date, pid, base_price, price, competitor_price,
            discount_pct, seasonality, demand, revenue, elasticity
        ])

# ----------------------------
# Final DataFrame
# ----------------------------
df = pd.DataFrame(
    data,
    columns=[
        "date", "product_id", "base_price", "price", "competitor_price",
        "discount_pct", "seasonality", "demand", "revenue", "true_elasticity"
    ]
)

print(df.head())
print(df.describe())

# Save to CSV
df.to_csv("simulated_product_sales.csv", index=False)