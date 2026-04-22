# Makefile for GDP Growth Drivers Analysis - BEE2041 Final Project

.PHONY: all clean data eda analysis visuals

all: output/figures/graph4_school.png

# Create necessary directories
data/clean output/tables output/figures: mkdir -p $@

# 1. Load and clean data from raw World Bank files
data/clean/gdp_panel.csv: src/01_load_and_clean.py data/raw/ | data/clean
	python src/01_load_and_clean.py

# 2. Exploratory Data Analysis + Graph 1
output/tables/summary_stats.csv: src/02_eda.py data/clean/gdp_panel.csv | output/tables
	python src/02_eda.py

# 3. Regression analysis
output/tables/regression_results.csv: src/03_analysis.py data/clean/gdp_panel.csv | output/tables
	python src/03_analysis.py

# 4. Generate all visualizations (Graph 1-4)
output/figures/graph4_school.png: src/04_visualizations.py data/clean/gdp_panel.csv | output/figures
	python src/04_visualizations.py

clean:
	rm -rf data/clean/* output/tables/* output/figures/*

help:
	@echo "=== GDP Growth Drivers Pipeline ==="
	@echo "make all      → Run the full reproducible pipeline"
	@echo "make clean    → Remove generated files"
	@echo "make help     → Show this message"
