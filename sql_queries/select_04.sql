-- Знайти середній бал на потоці (по всій таблиці оцінок).

SELECT AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting;
