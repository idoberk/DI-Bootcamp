-- Exercise 1: DVD Rental
SELECT
    *
FROM
    film;


-- Find how many films there are for each rating.
SELECT
    rating,
    COUNT(*) rating
FROM
    film
GROUP BY
    rating;


-- Get a list of the movies that have a rating of G or PG-13 that are under 2 hours long, and whose rental price is under 3.00 sorted alphabetically.
SELECT
    film_id,
    title,
    rental_rate,
    LENGTH,
    rating
FROM
    film
WHERE
    rating IN ('G', 'PG-13')
    AND film.length < 120
    AND rental_rate < 3
ORDER BY
    title;


-- Find a customer in the customer table, and change his / her details to your details, using SQL UPDATE.
UPDATE customer
SET
    first_name = 'Ido',
    last_name = 'Berkovits',
    email = 'berkido@example.com'
WHERE
    customer_id = 524
RETURNING
    *;


-- Now find the customer’s address, and use UPDATE to change the address to your address (or make one up).
UPDATE address
SET
    address = 'Zabotinsky',
    district = 'Holon',
    postal_code = 5828105
WHERE
    address_id = 530
RETURNING
    *;


-- Exercise 2: Students Table
SELECT
    *
FROM
    students;


-- Update 'Lea Benichou' and 'Marc Benichou' are twins, they should have the same birth_dates. Update both their birth_dates to 02/11/1998.
UPDATE students
SET
    birth_date = '11/02/1998'
WHERE
    last_name = 'Benichou'
RETURNING
    *;


-- Change the last_name of David from ‘Grez’ to ‘Guez’.
UPDATE students
SET
    last_name = 'Guez'
WHERE
    last_name = 'Grez'
RETURNING
    *;


-- Delete the student named ‘Lea Benichou’ from the table.
DELETE FROM students
WHERE
    first_name = 'Lea'
    AND last_name = 'Benichou';


-- Count how many students are in the table.
SELECT
    COUNT(*)
FROM
    students;


-- Count how many students were born after 1/01/2000.
SELECT
    COUNT(*)
FROM
    students
WHERE
    birth_date > '01/01/2000';


-- Add a column to the student table called math_grade.
ALTER TABLE students
ADD COLUMN math_grade NUMERIC(5, 2) NOT NULL DEFAULT 0;


-- Add 80 to the student which id is 1.
UPDATE students
SET
    math_grade = 80
WHERE
    students.id = 1
RETURNING
    *;


-- Add 90 to the students which have ids of 2 or 4.
UPDATE students
SET
    math_grade = 90
WHERE
    students.id IN (2, 4)
RETURNING
    *;


-- Add 40 to the student which id is 6.
UPDATE students
SET
    math_grade = 40
WHERE
    students.id = 6
RETURNING
    *;


-- Count how many students have a grade bigger than 83
SELECT
    COUNT(*)
FROM
    students
WHERE
    math_grade > 83;


-- Add another student named ‘Omer Simpson’ with the same birth_date as the one already in the table. Give him a grade of 70.
INSERT INTO
    students (first_name, last_name, birth_date, math_grade)
SELECT
    'Omer',
    'Simpson',
    birth_date,
    70
FROM
    students
WHERE
    first_name = 'Omer'
    AND last_name = 'Simpson';


-- Now, in the table, ‘Omer Simpson’ should appear twice. It’s the same student, although he received 2 different grades because he retook the math exam.
-- Bonus: Count how many grades each student has.
-- Tip: You should display the first_name, last_name and the number of grades of each student. If you followed the instructions above correctly, all the students should have 1 math grade, except Omer Simpson which has 2.
-- Tip : Use an alias called total_grade to fetch the grades.
-- Hint : Use GROUP BY.
SELECT
    first_name,
    last_name,
    COUNT(math_grade) AS total_grade
FROM
    students
GROUP BY
    first_name,
    last_name;


-- Find the sum of all the students grades.
SELECT
    SUM(math_grade) AS grade_sum
FROM
    students;


-- Exercise 3: Items and Customers
-- 1. Create a table named purchases. It should have 3 columns:
-- id: the primary key of the table
-- customer_id: this column references the table customers
-- item_id: this column references the table items
-- quantity_purchased: this column is the quantity of items purchased by a certain customer
CREATE TABLE
    purchases (
        id SERIAL PRIMARY KEY,
        customer_id INT NOT NULL REFERENCES customers (customer_id),
        item_id INT NOT NULL REFERENCES items (item_id),
        quantity_purchased INT NOT NULL
    );


-- 2. Insert purchases for the customers, use subqueries:
-- Scott Scott bought one fan
-- Melanie Johnson bought ten large desks
-- Greg Jones bought two small desks
INSERT INTO
    purchases (customer_id, item_id, quantity_purchased)
VALUES
    (
        (
            SELECT
                customer_id
            FROM
                customers
            WHERE
                first_name = 'Scott'
                AND last_name = 'Scott'
        ),
        (
            SELECT
                item_id
            FROM
                items
            WHERE
                item_name = 'Fan'
        ),
        1
    ),
    (
        (
            SELECT
                customer_id
            FROM
                customers
            WHERE
                first_name = 'Melanie'
                AND last_name = 'Johnson'
        ),
        (
            SELECT
                item_id
            FROM
                items
            WHERE
                item_name = 'Large Desk'
        ),
        10
    ),
    (
        (
            SELECT
                customer_id
            FROM
                customers
            WHERE
                first_name = 'Greg'
                AND last_name = 'Jones'
        ),
        (
            SELECT
                item_id
            FROM
                items
            WHERE
                item_name = 'Small Desk'
        ),
        2
    )
RETURNING
    *;


-- 1. Use SQL to get the following from the database:
-- All purchases. Is this information useful to us?
SELECT
    *
FROM
    purchases;


-- This information as itself is not useful to us (though it depends on what we are looking for).
-- All purchases, joining with the customers table.
SELECT
    cu.customer_id,
    CONCAT(cu.first_name, ' ', cu.last_name) AS full_name,
    pu.item_id,
    pu.quantity_purchased
FROM
    purchases AS pu
    INNER JOIN customers AS cu ON pu.customer_id = cu.customer_id;


-- Purchases of the customer with the ID equal to 5.
SELECT
    cu.customer_id,
    CONCAT(cu.first_name, ' ', cu.last_name) AS full_name,
    pu.item_id,
    pu.quantity_purchased
FROM
    purchases AS pu
    INNER JOIN customers AS cu ON pu.customer_id = cu.customer_id
WHERE
    pu.customer_id = 5;


-- Purchases for a large desk AND a small desk.
SELECT
    pu.id,
    pu.customer_id,
    it.item_id,
    it.item_name,
    pu.quantity_purchased
FROM
    purchases AS pu
    INNER JOIN items AS it ON pu.item_id = it.item_id
WHERE
    it.item_name ILIKE '%desk%';


-- 2. Use SQL to show all the customers who have made a purchase. Show the following fields/columns:
-- Customer first name
-- Customer last name
-- Item name
SELECT
    cu.first_name,
    cu.last_name,
    it.item_name
FROM
    purchases AS pu
    INNER JOIN customers AS cu ON pu.customer_id = cu.customer_id
    INNER JOIN items AS it ON pu.item_id = it.item_id;


-- 3. Add a row which references a customer by ID, but does not reference an item by ID (leave it blank). Does this work? Why/why not?
INSERT INTO
    purchases (customer_id, quantity_purchased)
VALUES
    (1, 1);


-- It won't work because of the NOT NULL constraint. Also, a purchases without an item makes no sense. If we remove the NOT NULL constraint, it would work because foreign keys allow NULL, but also won't make sense since NOT NULL foreign key columns must always point to something.