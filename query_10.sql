SELECT sub.name AS subject_name
FROM subjects sub
JOIN grades g ON sub.id = g.subject_id
JOIN teachers t ON sub.teacher_id = t.id
WHERE g.student_id = 15 AND t.id = 4;
