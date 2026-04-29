# Makefile for: What will Drive Economic Growth Across Countries in 2026?

# 1. Load and clean the raw World Bank data files
data/clean/gdp_panel.csv: src/01_clean.py data/raw/ | data/clean
	python src/01_clean.py

# 2. Exploratory Data Analysis (Table 1 and Graph 1)
output/tables/summary_stats.csv: src/02_analysis.py data/clean/gdp_panel.csv | output/tables
	python src/02_analysis.py

# 3. Regression Analysis (Table 2)
output/tables/regression_results.csv: src/02_analysis.py data/clean/gdp_panel.csv | output/tables
	python src/02_analysis.py

# 4. Generate all graphs (Graph 1 to Graph 4)
output/figures/Graph4.png: src/03_graphs.py data/clean/gdp_panel.csv | output/figures
	python src/03_graphs.py
