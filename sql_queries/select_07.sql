-- Знайти оцінки студентів у окремій групі з певного предмета.

SELECT r.student_id, s.student_name, sb.subject_name, r.rate
FROM raiting r
JOIN students s ON r.student_id = s.id
JOIN subjects sb ON r.subject_id = sb.id
JOIN groups g ON s.group_id = g.id
WHERE g.id = 2 AND sb.id = 2;
