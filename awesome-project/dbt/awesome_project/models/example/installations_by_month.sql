-- models/aggregate_sales.sql

{{ config(
    materialized='materialized_view'
) }}

SELECT 
	COUNT(id),
    DATE_TRUNC('month', installation_date) AS month
FROM installation 
GROUP BY month
ORDER BY month;
