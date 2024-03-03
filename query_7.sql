SELECT s.name AS student_name, g.grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.name = 'History' AND s.group_id = 2;
