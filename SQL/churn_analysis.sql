USE customer_churn_db;

-- 1. Total Customers
SELECT COUNT(*) AS Total_Customers
FROM customer_churn;


-- 2. Total Churned Customers
SELECT COUNT(*) AS Churned_Customers
FROM customer_churn;


-- 3. Churn Rate
SELECT
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn;

-- 4. Contract Type vs Churn
SELECT
    Contract_Type,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Contract_Type
ORDER BY Churn_Rate_Percent DESC;

-- 5. City vs Churn
SELECT
    City,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY City
ORDER BY Churn_Rate_Percent DESC;

-- 6. Payment Method vs Churn
SELECT
    Payment_Method,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Payment_Method
ORDER BY Churn_Rate_Percent DESC;

-- 7. Internet Service vs Churn
SELECT
    Internet_Service,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Internet_Service
ORDER BY Churn_Rate_Percent DESC;

-- 8. Churn Reasons
SELECT
    Churn_Reason,
    COUNT(*) AS Churned_Customers
FROM customer_churn
WHERE Churn = 'Yes'
GROUP BY Churn_Reason
ORDER BY Churned_Customers DESC;

-- 9. Revenue at Risk
SELECT
    ROUND(SUM(Monthly_Charges), 2) AS Revenue_at_Risk
FROM customer_churn
WHERE Churn = 'Yes';

-- 10. Satisfaction Score vs Churn
SELECT
    Satisfaction_Score,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Satisfaction_Score
ORDER BY Satisfaction_Score;

-- 11. Support Tickets vs Churn
SELECT
    Support_Tickets,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Support_Tickets
ORDER BY Support_Tickets;

-- 12. Tenure vs Churn
SELECT
    Tenure_Months,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Tenure_Months
ORDER BY Tenure_Months;

-- 13. Monthly Charges vs Churn
SELECT
    CASE
        WHEN Monthly_Charges < 600 THEN 'Low Charges'
        WHEN Monthly_Charges BETWEEN 600 AND 999 THEN 'Medium Charges'
        ELSE 'High Charges'
    END AS Charge_Category,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        100.0 * SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS Churn_Rate_Percent
FROM customer_churn
GROUP BY Charge_Category
ORDER BY Churn_Rate_Percent DESC;

