-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT student_id, AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting
WHERE subject_id = 2
GROUP BY student_id
ORDER BY avg_rate DESC
LIMIT 1;