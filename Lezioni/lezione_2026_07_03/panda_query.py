import pandas as pd

# Load the dataset
df = pd.read_csv("tech_orders.csv", index_col='OrderID')

# Ensure date column is in datetime format for temporal queries
df["Data_Ordine"] = pd.to_datetime(df["Data_Ordine"])

# -----------------------------------------------------------------------------
# PROGRESSIVE "WHERE" QUERIES (FROM BASIC TO EXPERT)
# -----------------------------------------------------------------------------

# --- LEVEL 1: WARM-UP (Multi-conditions & String Methods) ---

# 1. Discounted Laptops in January
# Write a query to find all orders in the "Laptop" category placed in January 2026
# where a discount was actually applied (not NaN and greater than 0).



# 2. City pattern matching & Exclusion
# Write a query to find orders shipped to cities starting with "M" OR ending with "o",
# EXCLUDING orders paid via "Bonifico".



# 3. Regex / Multiple substring search
# Write a query to find orders where the "Prodotto" name contains either "Pro" OR "Max"
# (case-insensitive) AND the "Quantita" is strictly greater than 1.



# --- LEVEL 2: INTERMEDIATE (Calculated Filters & Dates) ---

# 4. Weekend cancellations
# Write a query to select all orders placed on a weekend (Saturday or Sunday)
# where the "Stato_Spedizione" is either "Annullato" or "Rimborsato".
# (Hint: use .dt.dayofweek or .dt.day_name())



# 5. On-the-fly math filtering
# Write a query to find orders where the total gross value (Prezzo_Unitario * Quantita)
# exceeds 2000 euros, but ONLY for customers whose ID starts with "C1" or "C2".



# 6. Above-average discounts
# Write a query to find all orders where the "Sconto_Applicato" is strictly higher
# than the overall average discount of the entire dataset.



# --- LEVEL 3: ADVANCED (Subqueries & Frequency-based filtering) ---

# 7. Loyal / Repeat customers only
# Write a query to filter and display ONLY the orders placed by "repeat customers"
# (customers who appear more than 3 times in the entire dataframe).
# (Hint: use .value_counts() and .isin(), or groupby with .transform())



# 8. Top-tier Accessories
# Write a query to find all orders involving the 2 most expensive distinct products
# within the "Accessori" category.



# --- LEVEL 4: EXPERT (Statistical thresholds & Category-level comparisons) ---

# 9. Outperforming category average
# Write a query to find orders where the "Quantita" purchased is higher than
# the average quantity purchased FOR THAT SPECIFIC CATEGORY.
# (Hint: requires combining groupby(), .transform("mean"), and boolean indexing)



# 10. High-value anomalies (Percentiles)
# Write a query to find "problematic high-value orders": orders where the net total
# after discount is in the top 5% of the entire dataset (above the 95th percentile using .quantile(0.95))
# AND the shipping status is NOT "Consegnato".