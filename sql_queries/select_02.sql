-- Знайти студента із найвищим середнім балом з певного предмета.

SELECT student_id, s.student_name, sb.subject_name, AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting r
JOIN students s ON s.id = r.student_id
JOIN subjects sb ON sb.id = r.subject_id
WHERE subject_id = 2
GROUP BY student_id
ORDER BY avg_rate DESC
LIMIT 1;