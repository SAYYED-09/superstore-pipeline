-- Sales and Profit by Region
SELECT 
    Region,
    ROUND(SUM(Sales), 2)  AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_data
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Top 5 States by Profit
SELECT 
    State,
    ROUND(SUM(Sales), 2)  AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_data
GROUP BY State
ORDER BY Total_Profit DESC
LIMIT 5;

-- Bottom 5 States by Profit
SELECT 
    State,
    ROUND(SUM(Sales), 2)  AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_data
GROUP BY State
ORDER BY Total_Profit ASC
LIMIT 5;