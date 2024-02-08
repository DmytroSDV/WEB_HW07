-- Список курсів, які певному студенту читає певний викладач.

SELECT s.student_name, sb.subject_name, p.professor_name
FROM students s
JOIN raiting r ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id
JOIN professors p ON sb.professors_id = p.id
WHERE s.id = 2 AND p.id = 2;