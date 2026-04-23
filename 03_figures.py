# Import all needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import statsmodels.formula.api as smf

# Calculate the average GDP growth across all countries
growth_by_year = (df.groupby("year")["gdp_growth"].mean().reset_index().round(2))

# Plot the output 2
plt.figure(figsize = (10, 5))

plt.plot(growth_by_year["year"], growth_by_year["gdp_growth"], marker = "o", linewidth = 2, color = "#2196F3", label = "Average GDP Growth")
plt.axhline(0, color = "red", linewidth = 1, linestyle = "--", label = "Zero Growth Line")
for x, y in zip(growth_by_year["year"], growth_by_year["gdp_growth"]):
    plt.text(x, y + 0.2, f"{y:.1f}", ha = "center", va = "bottom", fontsize = 6, color = "#000000")

plt.title("Graph 1: Average GDP Growth Across 139 Countries (2000–2024)", fontsize = 13, fontweight = "bold")
plt.xlabel("Year")
plt.ylabel("GDP Per Capita Growth (%)")
plt.legend()

plt.tight_layout() 
plt.show()

# Compute the correlation matrix
df_corr = (df[corr_vars].rename(columns = corr_labels).corr(numeric_only = True))

print("Correlation matrix:")
print(df_corr.round(2))

# Plot the correlation heatmap (Output 3)
plt.figure(figsize = (9, 7))

sns.heatmap(df_corr, annot = True, fmt = ".2f", cmap = "coolwarm", center = 0,  vmin = - 1, vmax = 1, linewidths = 0.5)
plt.title("Graph 2: GDP Growth and Other Drivers (2000–2024)", fontsize = 13, fontweight = "bold", pad = 15)

plt.tight_layout() 
plt.show()

# Compute average Investment and FDI across all countries by year
drivers_by_year = (df.groupby("year")[["investment", "fdi"]].mean().reset_index().round(2))

print(drivers_by_year)

# Plot the overall trend of Investment and FDI over time (output 5)
plt.subplots(figsize = (10, 5))

plt.plot(drivers_by_year["year"], drivers_by_year["investment"], marker = "o", linewidth = 2, color = "#0000FF", label = "Investment (% of GDP)")
plt.plot(drivers_by_year["year"], drivers_by_year["fdi"], marker = "o", linewidth = 2, color = "#008000", label = "FDI (% of GDP)")
for x, inv, fdi in zip(drivers_by_year["year"], drivers_by_year["investment"], drivers_by_year["fdi"]):
    plt.text(x, inv + 0.4, f"{inv}", ha = 'center', va = 'bottom', fontsize = 6, color = "#000000")
    plt.text(x, fdi - 0.4, f"{fdi}", ha = 'center', va = 'top', fontsize = 6, color = "#000000")
    
plt.title("Graph 3: Trends in Average Investment and FDI over time (2000–2024)", fontsize = 13, fontweight = "bold")
plt.xlabel("Year")
plt.ylabel("% of GDP")
plt.legend(loc = "center right")

plt.tight_layout() 
plt.show()

# Average per country for recent years
recent = df[df["year"] >= 2000]
country_avg = recent.groupby(["country_code", "country"])[["gdp_growth", "school_enrolment",]].mean().round(2)

# Plot the School Enrolment vs GDP Growth graph (output 6)
plt.figure(figsize = (10, 6))
country_avg.plot(kind = "scatter", x = "school_enrolment", y = "gdp_growth", s = 50, alpha = 0.7, color = "#FF5722", label = "average school enrolment", 
ax = plt.gca())

plt.title("Graph 4: Relationship Between Secondary School Enrolment and Average GDP Growth (2000–2024)", fontsize = 13, fontweight ="bold")
plt.xlabel("School Enrolment (%)")
plt.ylabel("Average GDP Growth (%)")
plt.grid(True)
plt.legend(loc = "lower right")

plt.tight_layout() 
plt.show()
