---
title: 'What Drives Economic Growth Across Countries in 2026? '

---

# What will Drive Economic Growth Across Countries in 2026?

## Background 
Economic growth is one of the most influential drivers in our lives. As the economy grows, the employees' salaries increase, leading to higher tax revenue. As a result, the government will invest more in education, healthcare services, and other key areas. However, some countries that grow faster than others, while some are still struggling even after overcoming the worst of the post-COVID slump.

## Why this Topic?
I explore this topic because I want to understand which factors facilitate quicker economic recovery and growth after major crises, including the Global Financial Crisis in 2008 and the coronavirus outbreak in the early 2020s. I also want to determine which potential factors can contribute to economic growth. I also found significant disparities between countries in terms of GDP (Gross Domestic  Product) growth after conducting a detailed empirical analysis. Some of the findings also surprised me. 

Currently, this topic is also quite relevant. By 2026, many countries will still be burdened by excessive national debt. For instance, the debt-to-GDP ratios of Italy and Japan already exceed 130%. They are also influenced by other economic and environmental factors, such as the consequences of pandemics, climate change, as well as technological and environmental transitions. Therefore, the identification of the most effective determinants of GDP growth will be useful for allocating necessary financial resources correctly.

Apart from its practical value, the problem itself is also extremely interesting to study. Economic determinants of growth differ in their characteristics and depend on time, while new World Bank data allows me to estimate the modern trends. Therefore, I grabbed the data from the World Bank to do such an empirical analysis to find out the answer.

## Definition of Data
This analysis is based on a panel dataset that is built using the World Bank’s World Development Indicators (WDI). It contains information about 139 countries from 2000 to 2024.

* **Main outcome variable:** GDP growth (annual %)
* **Unit of observation:** Country-year
* **Total observations:** 2,159 after cleaning
* **Sources:** I used 8 indicators CSV files which obtained from the World Bank database. All data were cleaned, transformed from wide to long format, combined, and filtered to exclude regional aggregates and missing values.

All the variables used in this research are based on the definitions from the World Bank and are consistent across all the countries. This makes them suitable to do the empirical comparisons across countries over time. 

## Used Indicators
My analysis is based on the GDP growth as the dependent variable. My independent variables include the following factors: 
* **Trade (% of GDP)**
* **Inflation (annual %)**
* **Investment (gross fixed capital formation as % of GDP)**
* **School enrolment (secondary, gross %)**
* **Unemployment (% of total labour force)**
* **Foreign direct investment (net inflows as % of GDP)**
* **Broad money (% of GDP)**

## Findings
![Table 1](https://hackmd.io/_uploads/Sk1bcMuaWe.png)

My analysis starts with a descriptive overview of the variables in the dataset. Table 1 shows the statistical summary for  2,159 country-year observations in 139 countries between 2000 and 2024. In the table, the mean  of GDP growth rate is about 3.85% and shows high variability, with a standard deviation (SD) of 4.89% and a range from -54.40% to 75.31%. This volatility implies that many countries are sensitive to the external shocks and domestic policy challenges, any of these have a large impact on the entire economy.

On average, investment is around 24.79%, while trade is around 81.60%. The high level of both variables highlights to the crucial role of capital accumulation and international integration during this period. These high values of both variables also indicate that many countries relied heavily on capital formation and integration into the international market for economic growth.

Moreover, the mean secondary school enrolment rate was estimated to be 79.08%, with certain countries exceeding 100%, implying decent access to education. However, its wide range (6.23% to 159.11%) demonstrates the persistence of human capital disparities between countries. 

Additionally, Foreign Direct Investment (FDI) shows an average of 3.96% of GDP, while broad money is estimated at 79.7%. However, the extremely high SD of broad money (463.27) indicates that the data are widely dispersed. These high values come from financial hubs and offshore centres, such as Singapore and Hong Kong. These places have large banking  and financial service industries relative to the size of their economies. As a result, the data exhibit such unusually wide dispersion.

Lastly, inflation and unemployment rate are also dispersed. While the mean inflation rate stands at 5.70% with an SD of 8.45%, it ranged between deflation (-16.86%) and an extremely high level of inflation (133.49%), such as Argentina and Lesotho. This large gap is because of the currency crises and changes in commodities price, along with inconsistent monetary policy in some emerging and developing countries. Meanwhile, the mean unemployment rate stands at 7.39%, while the SD was estimated at 5.91%. The range of unemployment went down to 0.10% and went up to 37.32%. This indicates that there is a large variation in the labour market structure, including skill mismatches, and economics shocks experienced by some countries.

Overall, the above data reveals that while physical and human capital accumulation, economic globalisation, and financial development facilitate economic expansion, the effectiveness of these factors is limited by excessive macroeconomic instability. 

![Graph 1](https://hackmd.io/_uploads/Syh-5GdTZl.png)

After analysing the statistical summary, I now examine the trend of the GDP growth rate over year. Graph 1 illustrates the fluctuation in average GDP growth between 2000 and 2024 for 139 countries. It shows that the GDP growth rate was increasing until 2004, reaching a peak value of 6.9%, and remained relatively stable until the Great Recession in 2009. It fell to 0.5%, but quickly recovered in the following year and returned to 5.1%. In 2020, there was an unprecedented decline in the GDP growth rate due to the COVID-19 pandemic. It dropped to -4.9%, but rebounded to 6.7% in just one year.

These results suggest that external shocks have an immediate negative impact, but they are difficult to prevent. Nevertheless, it is apparent that the world economy is extremely vulnerable to external shocks. This vulnerability emphasises the importance of improving economic resilience by adopting various measures, such as diversified production structures. However, a question arises: What drives GDP growth recovery during such period? This is explored in more detail below.

![Graph 2](https://hackmd.io/_uploads/S1Iz5G_abe.png)

Having considered trends in GDP growth, Graph 2 analyses the relationships between GDP growth and other potential indicators of growth in a correlation heatmap.

As we can see, there are no strong correlations between GDP growth and most indicators (e.g. inflation and trade), meaning that other factors may drive GDP growth. What we need to note is that investment is the most positively correlated with GDP growth, around 0.13. This means that an increase in domestic investment can lead to an increase in economic growth. This is because increase in investment can improve the productivity through machinery, and technological upgrades. This also aligns with the neoclassical economic growth theory, which states that an increase in physical capital accumulation is a determinant of economic growth. 

Furthermore, FDI also shows a positive correlation with GDP growth, around 0.08. However, the impact is slightly weaker than investment. This is because FDI is more volatile and influenced by global economic conditions, making it less reliable as an indicator for the GDP growth. Moreover, the benefits of FDI for the GDP growth also rely on a country's absorptive capacity of new technologies and foreign firms' participation in domestic economic processes. Therefore, if countries do not have such condition, the FDI may have limited impact on the growth.

Meanwhile, there is a negative correlation between GDP growth and school enrolment, which is around -0.16. These unexpected findings are likely due to the school enrolment variable is measured using gross secondary school enrolment ratio, which can exceed 100% when many students repeat classes and enrol late. In most developing countries, including Argentina and Brazil, high values of gross enrolments may indicate low quality of education and grade repetition rather than strong human capital development. Therefore, higher enrolment rate may suggest that there are issues with the quality of education, which could hinder economic growth.

![Table 2](https://hackmd.io/_uploads/rJ175GdpZe.png)

Following Graph 2, I create a regression model to examine the variables further. From Table 2, investment has a positive and significant impact on GDP growth (coef = 0.0814, p < 0.01). This means that 1% increase in investment, the GDP growth will increase 0.0814%. Furthermore, FDI also has a positive and significant relationship with GDP growth (coef = 0.0505, p < 0.01). This means that 1% percentage increase in FDI, leading to 0.0505% increase in GDP growth. Lastly, schooling is negatively correlated with GDP growth (coef = -0.0286, p < 0.01). This means that 1% in school enrolment will cause a 0.0286% decrease in GDP growth. All variables are statistically significant but economically modest effect. 

However, the regression model can only explain a small part of GDP growth since the R² is 0.054, meaning that only 5.4% of the variation in GDP growth can be explained by this model. This means the variables in the model have limited explanatory power and only can explain a small picture of GDP growth. This is because GDP growth is complex, there are many other factors that can influence it, such as political stability. Therefore, the regression results provide important insights into the determinants of growth, but we need to interpret them carefully. I will also explain the mechanism and rationale behind the relationships between investment, FDI, school enrolment, and GDP growth in detail below. 

![Graph 3](https://hackmd.io/_uploads/ryDm5Mu6-g.png)

After analysing the regression model, we can focus on the overall trends in investment and FDI (graph 3) over time to identify the similarities and differences with the GDP growth trends. 

From Graph 3, investment is relatively stable with a steady range of 21.6% and 27.9% over the 2000 - 2024 period. It peaked at 27.92% in 2008, just before the Global Financial Crisis, and it is still notable for its resilience even in difficult times, rarely falling below 23%. However, the trend of FDI is much less volatile but still sensitive to shocks. It increased from 2.81% in 2000 and peaked at 6.74% in 2007. It also experienced drops of more than 30% due to the 2008 financial crisis and the 2020 COVID-19 pandemic.

When comparing with Graph 1, we can identify similarities and differences between the graphs. For example, the major crises in 2009 and 2020 also reduced both investment and FDI, which reinforces the positive correlations we have identified earlier. On the other hand, the biggest difference is in stability. GDP growth is highly volatile, which experienced a large drop after the external shocks, but investment and FDI are less volatile. This is because consumer expenditure and exports will collapse sharply once the crisis takes place, resulting in a decrease in GDP growth. However, investments decisions are made with a long-term perspective and takes many years to achieve. This makes them difficult to stop immediately. Many countries will continue to invest during the crisis to build the foundation of future growth and recovery. Furthermore, FDI is  more sensitive than investment, but it is less volatile than GDP since foreign investors tend to sustain their existing ventures. Therefore, this suggests that both investment and FDI are more stable than  GDP growth itself, which is largely affected by short-term shocks.

![Graph 4](https://hackmd.io/_uploads/B1z4cf_pWg.png)

Having considered the trends in investment and FDI in Graph 3, Graph 4 shows the correlation between secondary school enrolment and average GDP growth.

As we can observe, there is a weak but slightly negative relationship in the graph. From the graph, most countries are distributed in the range of 60% - 110% in secondary enrolment, with the average GDP growth between 1% and 7%. Interestingly, countries with above 100% enrolment rates do not perform better than those at moderate levels, such as Libya. Furthermore, those that exceed a 110% enrolment rate experience a below-average GDP growth rate. 

One possible reason is the lag between educational investment and economic growth. The increased number of students enrolled in schools does not result in a proportional increase in productivity immediately since they are still studying and do not enter the labour force yet. In the short run, GDP growth in countries mainly depends on the existing workforce and capital stock, rather than future capabilities. 

On the other hand, increasing enrolment rates might have some temporary negative effects on measured GDP growth, especially in developing countries. This is because the labour force will be reduced as many people are still studying. This creates a trade-off between investment in human capital and current economic performance. It is only later that positive effects emerge as graduates join the workforce, such as productivity increases and innovation. Therefore, the observed negative relationship between GDP growth and education can be explained by the fact that the costs of education are reflected in the data, while the benefits are not.

## Key Takeaways
What can we conclude from the findings?

* The GDP growth is extremely volatile. Unexpected shocks, such as the 2008 recession and the pandemic, have reduced the GDP growth significantly in many countries. This demonstrates  that its vulnerability to global events.

* Investment is one of several factors associated with GDP growth. Higher investment is associated with higher growth. Not only does the foreign investment contribute to it, but domestic investment also contributes. However, the impact is weak and less reliable as it depends on the global conditions.

* The relation between GDP growth and school enrolment is negative in the findings. But the short-term negative association does not necessarily reflect the true long-term impact.

* The volatility of GDP growth and other long-term drivers is different. While GDP growth volatility is high, investment and FDI are relatively stable.

## Limitations and Future Research
* Some key indicators  that are likely to influence GDP growth are missing in the analysis, including political stability and technological innovation. The exclusion of these variables may lead to misleading findings. This led to our understanding of the drivers of GDP growth becoming  incomplete and may not be accurate. Future research should expand the model by adding more determinants, including political stability. This can increase the explanatory power of the model and help us have a better understanding of all these complicated determinants of GDP growth.

## Conclusion
In conclusion, GDP growth is highly volatile which is easily influenced by external shocks, including financial crisis and pandemics. Furthermore, investment and FDI are positively correlated with GDP growth which can contribute to the economic growth in 2026, although the impact is weak and depends on macroeconomic conditions. On the other hand, the findings also show that an increase in school enrolment can slow down economic growth or even lead to a decrease due to the time lag and certain structural problems. However, our model can only explain a small part of economic growth. In reality, the determinants of GDP growth are far more complex.
