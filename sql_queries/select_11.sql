-- Середній бал, який певний викладач ставить певному студентові.

SELECT s.student_name, p.professor_name, sb.subject_name, AVG(CAST(rate AS FLOAT)) AS avg_rate
FROM raiting r
JOIN students s ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id
JOIN professors p ON p.id = sb.professors_id
WHERE p.id = 2 and s.id = 2;