-- Оцінки студентів у певній групі з певного предмета на останньому занятті.

SELECT s.student_name, r.rate, r.date_of
FROM students s
JOIN raiting r ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id
JOIN groups g ON s.group_id = g.id
WHERE g.id = 2 AND sb.id = 2
ORDER BY r.date_of DESC
LIMIT 1;

