-- Sum bands fans and group by origin country
-- to exec on command line "cat 2-fans.sql | mysql -uroot -p holberton > tmp_res ; head tmp_res"

SELECT origin,
    SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY SUM(fans) DESC;