# ==============================================================================
# KENYA INFLATION DASHBOARD: AUTOMATED DATA QUALITY VALIDATION SUITE
# Checks for empty cells and prints exact 5-year point shifts.
# ==============================================================================

import os
import pandas as pd

def run_pipeline_data_validation():
    clean_data_path = "output/clean_kenya_inflation.csv"
    print("=== STARTING PIPELINE DATA INTEGRITY CHECKS ===")
    
    if not os.path.exists(clean_data_path):
        print("❌ VALIDATION ERROR: Clean database missing.")
        return
        
    df = pd.read_csv(clean_data_path, index_col='Date', parse_dates=True)
    missing_value_count = df.isnull().sum().sum()
    
    if missing_value_count > 0:
        print(f"❌ IMPUTATION FAULT: {missing_value_count} unhandled NaN placeholders found!")
    else:
        print("✅ DATA COMPLETENESS: Imputation check passed. 0 missing data cells remain.")

    print("\n=== FINAL GENERATED DATA INSIGHTS FOR PRESENTATION SLIDES ===")
    start_row = df.iloc[0]
    end_row = df.iloc[-1]
    
    target_pillars = {
        'Headline_CPI': 'National Headline Basket',
        '01_Food_NonAlc': 'Division 01: Food & Non-Alcoholic Beverages',
        '04_Housing_Utilities': 'Division 04: Housing, Fuel & Utilities',
        '07_Transport': 'Division 07: Transport Services',
        'Other_Sectors_Combined': 'Aggregated Minor COICOP Sectors'
    }
    
    for column, friendly_name in target_pillars.items():
        point_diff = end_row[column] - start_row[column]
        pct_change = (point_diff / start_row[column]) * 100
        print(f"📈 {friendly_name}:")
        print(f"   • Price Point Delta: +{point_diff:.2f} points (Jan 2021 Base: {start_row[column]:.2f} -> May 2026: {end_row[column]:.2f})")
        print(f"   • Total 5-Year Cumulative Increase: {pct_change:.2f}%")

if __name__ == "__main__":
    run_pipeline_data_validation()
