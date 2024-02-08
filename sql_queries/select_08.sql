-- Знайти середній бал, який ставить певний викладач зі своїх предметів.

SELECT AVG(CAST(r.rate AS FLOAT)) AS avg_rate
FROM raiting r
JOIN subjects s ON r.subject_id = s.id
JOIN professors p ON s.professors_id = p.id
WHERE p.id = 2;
