-- Знайти список курсів, які відвідує студент.
 
SELECT s.student_name, g.group_name, sb.subject_name
FROM students s
JOIN groups g ON s.group_id = g.id
JOIN raiting r ON s.id = r.student_id
JOIN subjects sb ON r.subject_id = sb.id
WHERE s.id = 2