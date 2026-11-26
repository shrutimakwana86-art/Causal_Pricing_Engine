import numpy as np
import pandas as pd
import os
# Create the data directory if it does not exist
os.makedirs("data", exist_ok=True)
np.random.seed(42)
# 100 days of data (Days 1 to 70 = Pre-treatment, Days 71 to 100 = Post-treatment)
days = np.arange(1, 101)
cities = ["Vadodara", "Ahmedabad", "Surat", "Rajkot"]
records = []
for day in days:
    # Seasonal trend and baseline market demand
    base_demand = 1000 + 5 * day + 50 * np.sin(day / 7)
    competitor_price = 110 + np.random.normal(0, 3)
    for city in cities:
        # Apply price intervention in Vadodara starting from Day 71 (Treatment = 1)
        if city == "Vadodara" and day > 70:
            treatment = 1
            our_price = 125.0  # Price increased to 125
            price_effect = -120  # Demand drop due to price hike
        else:
            treatment = 0
            our_price = 110.0 + np.random.normal(0, 1)
            price_effect = 0    
        city_factor = {"Vadodara": 1.1, "Ahmedabad": 1.3, "Surat": 1.2, "Rajkot": 0.9}[city]
        units_sold = int((base_demand * city_factor) + price_effect + (competitor_price - our_price) * 4 + np.random.normal(0, 25))
        revenue = round(units_sold * our_price, 2)
        period = "Post-Treatment" if day > 70 else "Pre-Treatment"
        records.append({
            "day": day,
            "city": city,
            "period": period,
            "treatment": treatment,
            "our_price": round(our_price, 2),
            "competitor_price": round(competitor_price, 2),
            "units_sold": units_sold,
            "revenue": revenue
        })
df = pd.DataFrame(records)
df.to_csv("data/market_pricing_data.csv", index=False)
print("Data successfully saved to 'data/market_pricing_data.csv'!")
print(df.head())