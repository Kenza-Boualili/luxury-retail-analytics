-- ============================================================
-- LUXURY RETAIL ANALYTICS — EXECUTIVE QUERIES
-- ============================================================

-- 1. Revenue & Average Order Value (AOV) by Flagship Boutique
SELECT 
    store_name,
    COUNT(transaction_id) AS total_transactions,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS average_order_value
FROM transactions
GROUP BY store_name
ORDER BY total_revenue DESC;

-- 2. Top 5 Revenue-Generating Product Identifiers (Corrigé avec SUM(quantity))
SELECT 
    product_id,
    category,
    SUM(quantity) AS units_sold,
    ROUND(SUM(total_amount), 2) AS total_revenue
FROM transactions
GROUP BY product_id, category
ORDER BY total_revenue DESC
LIMIT 5;

-- 3. Revenue Distribution by Client Loyalty Tier (VIP / VIC / Standard)
SELECT 
    tier,
    COUNT(DISTINCT customer_id) AS total_customers,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(SUM(total_amount) * 100.0 / (SELECT SUM(total_amount) FROM transactions), 2) AS revenue_percentage
FROM transactions
GROUP BY tier
ORDER BY total_revenue DESC;
