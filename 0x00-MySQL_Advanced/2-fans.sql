-- Rabk country origins of bands by the number of fans
SELECT origin, SUM(fans) AS nb_fans FROM bands GROUP BY
    origin
ORDER BY
    b_fans DESC;