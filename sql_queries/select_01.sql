-- Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT student_id, AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting
GROUP BY student_id
ORDER BY avg_rate DESC
LIMIT 5;