
SELECT *
FROM dim_area;

SELECT *
FROM dim_procedure;

SELECT 
    year,
    COUNT(*) as total_transactions,
    ROUND(AVG(actual_worth)::numeric, 0) as avg_price,
    ROUND((SUM(actual_worth) / 1000000000)::numeric, 2) as total_value_billion_aed
FROM fact_transactions f
JOIN dim_date d ON f.date_id = d.date_id
GROUP BY year
ORDER BY year;

SELECT 
    a.area_name_en,
    COUNT(*) as total_transactions,
    ROUND((SUM(f.actual_worth) / 1000000000)::numeric, 2) as total_value_billion_aed,
    ROUND(AVG(f.actual_worth)::numeric, 0) as avg_price
FROM fact_transactions f
JOIN dim_area a ON f.area_id = a.area_id
GROUP BY a.area_name_en
ORDER BY total_value_billion_aed DESC
LIMIT 10;

SELECT 
    p.property_type_en,
    COUNT(*) as total_transactions,
    ROUND(AVG(f.actual_worth)::numeric, 0) as avg_price,
    ROUND((SUM(f.actual_worth) / 1000000000)::numeric, 2) as total_value_billion_aed
FROM fact_transactions f
JOIN dim_property p ON f.property_id = p.property_id
GROUP BY p.property_type_en
ORDER BY total_transactions DESC;


SELECT 
    d.month,
    COUNT(*) as total_transactions,
    ROUND(AVG(f.actual_worth)::numeric, 0) as avg_price
FROM fact_transactions f
JOIN dim_date d ON f.date_id = d.date_id
WHERE d.year = 2022
GROUP BY d.month
ORDER BY d.month;