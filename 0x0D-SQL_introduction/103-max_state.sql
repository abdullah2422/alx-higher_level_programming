-- Script that displays the max temperature of each state (ordered by State name).
SELECT state, MAX(temp) AS max_temp
FROM weather
GROUP BY state
ORDER BY state ASC;
