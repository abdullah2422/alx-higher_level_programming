-- Script that displays the top 3 of cities temperature
SELECT city, AVG(temp) as avg_temp
FROM weather
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
