# Kenya Inflation Dynamics Dashboard and Data Pipeline

An automated data engineering pipeline tracking core consumer cost-of-living indicators across official COICOP divisions in Kenya from 2021 to 2026.

## Data Engineer Scope of Work
This repository tracks backend code configurations managed to satisfy the following project requirements:
1. Source Datasets: Programmatic downloading of multi-year macroeconomic matrices live from remote server layers.
2. Clean and Structure Data: Time-series alignment indexing and linear timeline interpolation to eliminate data gaps.
3. Create Data Pipelines: Engineering single-execution operations mapping raw inputs cleanly to presentation charts.
4. Maintain Project Repository: Isolating workspace packages via venv, configurations via requirements.txt, and file hierarchies.

## Core Target Analytics Profile (The Necessary Pillars)
* Division 01: Food and Non-Alcoholic Beverages (32.91% Basket Weight)
* Division 04: Housing, Fuel and Utilities (14.61% Basket Weight)
* Division 07: Transport Services (9.65% Basket Weight)
* Other Sectors Combined (42.83% Combined Weight) - Calculated column mean tracking all minor divisions.

## Execution Manual
1. Activate virtual environment: venv\Scripts\activate
2. Sync application requirements: pip install -r requirements.txt
3. Execute pipeline logic: python src/pipeline.py
4. Review quality and slide calculations: python src/test_pipeline.py

