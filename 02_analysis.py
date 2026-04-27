# Import all needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import statsmodels.formula.api as smf

# Read the cleaned data file in the desktop
desktop  = os.path.join(os.path.expanduser("~"), "Desktop")
filepath = os.path.join(desktop, "cleaned_data.csv")

df = pd.read_csv(filepath)

# Select the variables we want to use
corr_vars = ["gdp_growth", "trade", "inflation", "investment","school_enrolment", "unemployment", "fdi", "broad_money"]

# Rename all variables
corr_labels = {"gdp_growth": "GDP Growth (%)", "trade": "Trade (% GDP)", "inflation": "Inflation (%)", "investment": "Investment (% GDP)",
               "school_enrolment": "School Enrolment (%)", "unemployment": "Unemployment (%)", "fdi": "FDI (% GDP)", "broad_money": "Broad Money (% GDP)"}

# Compute the statistical summary 
summary = (df[corr_vars].rename(columns = corr_labels) .describe() .T .round(2))

# Rename each column and 
summary.columns = ["Count", "Mean", "Std Dev", "Min", "25%", "50%", "75%", "Max"]

# Display the output 1
print("Table 1: Statistical Summary for 139 countries between 2000 and 2024")
print(summary.to_string(justify = "center"))

# Run the regression
model = smf.ols("gdp_growth ~ investment + fdi + school_enrolment + trade + inflation + unemployment + broad_money", data = df).fit()

# Display the results (output 4)
print("Table 2: OLS Regression for all Potential Drivers of GDP Growth (2000–2024)")
print(model.summary())