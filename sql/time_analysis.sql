-- Monthly Sales Trend
SELECT 
    Year,
    Month,
    ROUND(SUM(Sales), 2)  AS Monthly_Sales,
    ROUND(SUM(Profit), 2) AS Monthly_Profit
FROM sales_data
GROUP BY Year, Month
ORDER BY Year, Month;

-- Best and Worst Quarter by Profit
SELECT 
    Year,
    Quarter,
    ROUND(SUM(Sales), 2)  AS Quarterly_Sales,
    ROUND(SUM(Profit), 2) AS Quarterly_Profit
FROM sales_data
GROUP BY Year, Quarter
ORDER BY Quarterly_Profit DESC;