-- Total Sales and Profit by Category
SELECT 
    Category,
    ROUND(SUM(Sales), 2)  AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Profit) * 100.0 / (SELECT SUM(Profit) FROM sales_data), 2) AS Profit_Pct
FROM sales_data
GROUP BY Category
ORDER BY Total_Profit DESC;

-- Top 10 Sub-Categories by Profit
SELECT 
    "Sub-Category",
    ROUND(SUM(Sales), 2)  AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM sales_data
GROUP BY "Sub-Category"
ORDER BY Total_Profit DESC
LIMIT 10;