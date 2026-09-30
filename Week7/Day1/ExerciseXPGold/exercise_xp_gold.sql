SELECT * FROM (
    SELECT * 
    FROM students 
    ORDER BY students.id 
    LIMIT 4
) AS first_four ORDER BY last_name;

SELECT * FROM students ORDER BY birth_date DESC LIMIT 1;

SELECT * FROM students LIMIT 3 OFFSET 2;