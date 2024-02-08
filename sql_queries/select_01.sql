-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT student_id, s.student_name, AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting r
JOIN students s ON s.id = r.student_id
GROUP BY student_id
ORDER BY avg_rate DESC
LIMIT 5;