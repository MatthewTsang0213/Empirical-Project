# What will Drive Economic Growth Across Countries in 2026?

## Motivation
Entering the year 2026, many countries are experiencing the long-term effects of external shocks, such as the global pandemic. While some countries recover fast enough, others are still struggling. Public debt remains a serious concern for them. For example, the debt-to-GDP ratios of Japan and Italy already exceed 130%. Therefore, I want to determine what could drive economic growth and resilience post-crisis. 

In this project, I set 2 questions to guide my analysis: 1) Which variable is the most important for sustained GDP growth? 2) Which variables can harm the GDP growth? The answers are explored in the analysis step-by-step. 

I used the data from the World Bank covering 139 countries from 2000 to 2024 and discovered significant differences in growth performance. Some findings also surprised me. 

Beyond the academic purpose, I also want to provide some useful insights to policymakers on how to allocate resources in an environment with high debt, climate change, and technological transitions.

## Libraries used
pandas - use for doing the data manipulation and data cleaning

os - use for handling file paths

matplotlib - use for creating graphs and plots

seaborn - use for creating graphs and plots

statsmodels - use for creating a regression model

## Variables Used

**Dependent Variable** 

- GDP growth (%) 

**Independent Variables**

- Investment (% of GDP)

- FDI (% of GDP)

- Trade (% of GDP)

- Inflation (%)

- School Enrolment (%)

- Unemployment (%)

- Broad Money (% of GDP)

## Procedure

- Download all 8 data files from the directory and save to **the desktop** **(do not create a folder to put them into the folder)**

- Download the blog.ipynb and save to **the desktop**

- Open blog.ipynb in Jupyter Notebook and run the code

- After finishing the first data cleaning process, you need to save a file called "pre_cleaned_data.csv". You can check the data in that file

- After checking the data, you need to do a few more steps for data cleaning.

- After doing all the data cleaning, you need to save the file on **the desktop** and name it "cleaned_data.csv" (This is the final version of data)

- You need to reopen the "cleaned_data.csv" for the empirical analysis.

- Run all the cells in the blog.ipynb to do the analysis. You will get the 2 tables and 4 graphs

## Directory Structure
project/

├── README.md

├── blog.ipynb

├── data/

│   ├── raw/          

│   ├── ├── API_BX.KLT.DINV.WD.GD.ZS_DS2_en_csv_v2_13.csv

│   ├── ├── API_FM.LBL.BMNY.GD.ZS_DS2_en_csv_v2_5797.csv

│   ├── ├── API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_287.csv

│   ├── ├── API_NE.GDI.TOTL.ZS_DS2_en_csv_v2_698.csv

│   ├── ├── API_NE.TRD.GNFS.ZS_DS2_en_csv_v2_101.csv

│   ├── ├── API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_260.csv

│   ├── ├── API_SE.SEC.ENRR_DS2_en_csv_v2_758.csv

│   ├── └── API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_36.csv

│   └── clean/        

│   ├── cleaned_data.csv

├── src/

│   ├── 01_clean.py

│   ├── 02_analysis.py

│   └── 03_figures.py

├── output/

│   ├── tables/

│   ├── ├── table 1

│   ├── └── table 2

│   └── graphs/

│   ├── ├── Graph 1.png

│   ├── ├── Graph 2.png

│   ├── ├── Graph 3.png

│   ├── └── Graph 4.png




## Contact Detail
Name: Matthew Tsang

Email: ht527@exeter.ac.uk

## References

World Bank Group (2026). Unemployment, total (% of total labor force) (modeled ILO estimates). *World Bank Group*. https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS

World Bank Group (n.d.). Broad Money (% of GDP). *World Bank Group*. https://data.worldbank.org/indicator/FM.LBL.BMNY.GD.ZS

World Bank Group (2026). School Enrolment, secondary (% gross). *World Bank Group*. https://data.worldbank.org/indicator/SE.SEC.ENRR

World Bank Group (n.d.). Inflation, consumer prices (annual %). *World Bank Group*. https://data.worldbank.org/indicator/FP.CPI.TOTL.ZG

World Bank Group (n.d.). Foreign direct investment, net inflow (% of GDP). *World Bank Group*. https://data.worldbank.org/indicator/BX.KLT.DINV.WD.GD.ZS

World Bank Group (n.d.). Trade (% of GDP). *World Bank Group*. https://data.worldbank.org/indicator/NE.TRD.GNFS.ZS

World Bank Group (n.d.). GDP growth (annual %). *World Bank Group*. https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG

World Bank Group (n.d.). Gross capital formation(% of GDP). *World Bank Group*. https://data.worldbank.org/indicator/NE.GDI.TOTL.ZS



