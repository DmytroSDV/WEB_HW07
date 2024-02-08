-- Знайти які курси читає певний викладач.

SELECT s.subject_name, p.professor_name
FROM subjects s
JOIN professors p ON s.professors_id = p.id
WHERE p.id = 2;