# Makefile for "What will Drive Economic Growth Across Countries in 2026?"

.PHONY: all clean help

# Default target - runs the full pipeline
all: output/figures/graph4.png

# Create directories if they don't exist
data/clean output/tables output/figures:
	mkdir -p $@

# 1. Clean and merge raw World Bank data
data/clean/gdp_panel.csv: src/01_load_and_clean.py data/raw/ | data/clean
	python src/01_load_and_clean.py

# 2. Exploratory Data Analysis (Table 1 + Graph 1)
output/tables/summary_stats.csv: src/02_eda.py data/clean/gdp_panel.csv | output/tables
	python src/02_eda.py

# 3. Regression Analysis (Table 2)
output/tables/regression_results.csv: src/03_analysis.py data/clean/gdp_panel.csv | output/tables
	python src/03_analysis.py

# 4. Generate all visualizations (Graph 1 to 4)
output/figures/graph4.png: src/04_visualizations.py data/clean/gdp_panel.csv | output/figures
	python src/04_visualizations.py

# Clean all generated files
clean:
	rm -rf data/clean/*
	rm -rf output/tables/*
	rm -rf output/figures/*

# Help command - shows available options
help:
	@echo "=== GDP Growth 2026 Analysis Pipeline ==="
	@echo "make all      → Run the complete analysis pipeline"
	@echo "make clean    → Remove all generated files"
	@echo "make help     → Show this help message"
