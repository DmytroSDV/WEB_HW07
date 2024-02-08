-- Знайти середній бал у групах з певного предмета.

SELECT g.group_name, AVG(CAST(r.rate AS FLOAT)) AS avg_rate
FROM raiting AS r
JOIN students AS s ON r.student_id = s.id
JOIN groups AS g ON s.group_id = g.id
JOIN subjects AS sub ON r.subject_id = sub.id
WHERE sub.id = 2
GROUP BY g.group_name;