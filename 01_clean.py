# Import all needed libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import statsmodels.formula.api as smf

# Read 1 of the 9 files to see what it looks like 
# Start from the most important data, which is the GDP Growth
desktop  = os.path.join(os.path.expanduser("~"), "Desktop")
filepath = os.path.join(desktop, "API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_260.csv")

df_gdp = pd.read_csv(filepath, skiprows = 4)

# Check how many rows and columns it contains
print("Shape:", df_gdp.shape)

# Look at the first 5 rows to understand the structure of the data
df_gdp.head()

# See all column names
print(df_gdp.columns.tolist())

# Keep the country columns and year columns only
year_cols = [str(y) for y in range(1960, 2026)]

df_gdp = df_gdp[["Country Name", "Country Code"] + year_cols]

# Rename country name and code
df_gdp = df_gdp.rename(columns = {"Country Name": "country", "Country Code": "country_code"})

# Check the data set after making such changes
print("Structure of the data:", df_gdp.shape)
print(df_gdp.head(5))

# Change the format of the data
df_gdp = df_gdp.melt(id_vars = ["country_code", "country"], var_name = "year", value_name = "gdp_growth")

# Convert year to an integer because this helps us to filter the values more conveniently
df_gdp["year"] = df_gdp["year"].astype(int)
df_gdp["gdp_growth"] = pd.to_numeric(df_gdp["gdp_growth"], errors = "coerce")

print("Number of rows and columns of the data set:", df_gdp.shape)
print(df_gdp.head(3))

# Check year range
print("Year range:", df_gdp["year"].min(), "to", df_gdp["year"].max())

# Load all 8 files
all_files = [("API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_260.csv", "gdp_growth"), ("API_NE.TRD.GNFS.ZS_DS2_en_csv_v2_101.csv", "trade"),
    ("API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_287.csv", "inflation"), ("API_NE.GDI.TOTL.ZS_DS2_en_csv_v2_698.csv", "investment"),
    ("API_SE.SEC.ENRR_DS2_en_csv_v2_758.csv", "school_enrolment"), ("API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_36.csv", "unemployment"),("API_BX.KLT.DINV.WD.GD.ZS_DS2_en_csv_v2_13.csv", "fdi"),
    ("API_FM.LBL.BMNY.GD.ZS_DS2_en_csv_v2_5797.csv", "broad_money")]

dfs = []

for filename, varname in all_files:
    filepath = os.path.join(desktop, filename)
    df_temp = pd.read_csv(filepath, skiprows = 4)
    
    df_temp = df_temp[["Country Name", "Country Code"] + year_cols]
    df_temp = df_temp.rename(columns = {"Country Name": "country", "Country Code": "country_code"})
    
    df_temp = df_temp.melt(id_vars = ["country_code", "country"], var_name = "year", value_name = varname)
    
    df_temp["year"] = df_temp["year"].astype(int)
    df_temp[varname] = pd.to_numeric(df_temp[varname], errors="coerce")

    dfs.append(df_temp)

dfs = []

# Start with the first dataframe as the base
for filename, varname in all_files:
    filepath = os.path.join(desktop, filename)
    df_temp = pd.read_csv(filepath, skiprows = 4)
    
    df_temp = df_temp[["Country Name", "Country Code"] + year_cols]
    df_temp = df_temp.rename(columns = {"Country Name": "country", "Country Code": "country_code"})
    
    df_temp = df_temp.melt(id_vars = ["country_code", "country"], var_name = "year", value_name = varname)
    
    df_temp["year"] = df_temp["year"].astype(int)
    df_temp[varname] = pd.to_numeric(df_temp[varname], errors="coerce")

    dfs.append(df_temp)

# Check the year range for all variable
print("gdp_growth year range:", df["year"].min(), "to", df["year"].max())
print("trade year range:", df["year"].min(), "to", df["year"].max())
print("inflation year range:", df["year"].min(), "to", df["year"].max())
print("investment year range:", df["year"].min(), "to", df["year"].max())
print("school_enrolment year range:", df["year"].min(), "to", df["year"].max())
print("unemployment year range:", df["year"].min(), "to", df["year"].max())
print("fdi year range:", df["year"].min(), "to", df["year"].max())

# Save the merged file to Desktop so we can open it in Excel
out_path = os.path.join(desktop, "pre_cleaned_data.csv")

df.to_csv(out_path, index = False)

# Check the structure of the data after merging all variables into one data frame. 
print(df.info())

# Check if there are any duplicate data
duplicates = df.duplicated(subset = ["country_code", "year"])

print("Duplicate rows:", duplicates.sum())

# Drop the rows with missing values
df_clean = df.dropna() 

# Check how many rows we have before and after
print("Rows before dropping missing:", df.shape)
print("Rows after dropping missing:", df_clean.shape)

# Keep only rows where the year is between 2000 and 2024 because not all the countries contain data between 1960 and 2024. Therefore, we need to narrow down the time frame.
df_clean = df_clean.query("year >= 2000 and year <= 2024")

# Check the result
print("Year range:", df_clean["year"].min(), "to", df_clean["year"].max())
print("Shape:", df_clean.shape)
print("First 3 rows:")
print(df_clean.head(3))

# AFE (Africa Eastern and Southern) is a regional code, not a real country. Therefore, we need to remove it from the data.
df_clean = df_clean.query("country_code != 'AFE'")

# Check the result
print("Countries remaining:", df_clean["country_code"].nunique())
print("Shape:", df_clean.shape)

# Save the final cleaned file to the Desktop
out_path = os.path.join(desktop, "cleaned_data.csv")

df_clean.to_csv(out_path, index = False)
print("broad_money year range:", df["year"].min(), "to", df["year"].max())