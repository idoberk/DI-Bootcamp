-- Exercise 1:
-- Get a list of all the languages, from the language table.
SELECT
    *
FROM
    LANGUAGE;


-- Get a list of all films joined with their languages – select the following details: film title, description, and language name.
SELECT
    f.title,
    f.description,
    l.name AS LANGUAGE
FROM
    film AS f
    INNER JOIN LANGUAGE AS l ON f.language_id = l.language_id;


-- Get all languages, even if there are no films in those languages – select the following details: film title, description, and language name.
SELECT
    f.title,
    f.description,
    l.name AS LANGUAGE
FROM
    LANGUAGE AS l
    LEFT JOIN film AS f ON f.language_id = l.language_id;


-- Create a new table called new_film with the following columns: id, name. Add some new films to the table.
CREATE TABLE
    new_film (id SERIAL PRIMARY KEY, NAME VARCHAR(50) NOT NULL);


INSERT INTO
    new_film (NAME)
VALUES
    ('Inception'),
    ('The Matrix'),
    ('Interstellar'),
    ('Parasite'),
    ('Spirited Away');


-- Create a new table called customer_review, which will contain film reviews that customers will make.
-- It should have the following columns:
-- review_id – a primary key, non null, auto-increment.
-- film_id – references the new_film table. The film that is being reviewed.
-- language_id – references the language table. What language the review is in.
-- title – the title of the review.
-- score – the rating of the review (1-10).
-- review_text – the text of the review. No limit on the length.
-- last_update – when the review was last updated.
CREATE TABLE
    customer_review (
        review_id SERIAL PRIMARY KEY,
        film_id INTEGER NOT NULL REFERENCES new_film (id) ON DELETE CASCADE,
        language_id INTEGER NOT NULL REFERENCES LANGUAGE (language_id),
        title VARCHAR(100),
        score SMALLINT CHECK (score BETWEEN 1 AND 10),
        review_text TEXT,
        last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );


-- Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
INSERT INTO
    customer_review (film_id, language_id, title, score, review_text)
VALUES
    (
        (
            SELECT
                id
            FROM
                new_film
            WHERE
                NAME = 'Inception'
        ),
        (
            SELECT
                language_id
            FROM
                LANGUAGE
            WHERE
                NAME = 'English'
        ),
        'A dream within a dream',
        9,
        'Mind-bending plot with a great soundtrack. Needs a second viewing to catch everything.'
    ),
    (
        (
            SELECT
                id
            FROM
                new_film
            WHERE
                NAME = 'Spirited Away'
        ),
        (
            SELECT
                language_id
            FROM
                LANGUAGE
            WHERE
                NAME = 'Japanese'
        ),
        'Beautiful and strange',
        10,
        'Stunning animation and a story that works for both kids and adults.'
    );


SELECT
    *
FROM
    new_film;


SELECT
    *
FROM
    customer_review;


-- Delete a film that has a review from the new_film table, what happens to the customer_review table?
DELETE FROM new_film
WHERE
    NAME = 'Inception';


-- The review of the film that was deleted in the new_film table will also be deleted. So the review will be deleted from customer_review.
-- -- -- --
-- Exercise 2:
-- Use UPDATE to change the language of some films. Make sure that you use valid languages.
UPDATE film
SET
    language_id = 3
WHERE
    film_id IN (3, 5, 6, 7, 9, 11)
RETURNING
    *;


-- Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- Foreign keys: address_id.
-- Effect on INSERT: The address must already exist in the address table. Inserting a customer with a non-existent address_id is a FK violation.
SELECT
    *
FROM
    customer;


-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- Yes, it is an easy step, because no other table depends on customer_review.
DROP TABLE IF EXISTS customer_review;


-- Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
SELECT
    COUNT(*)
FROM
    rental
WHERE
    return_date IS NULL;


-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet).
SELECT DISTINCT
    f.film_id,
    f.title,
    f.rental_rate,
    f.replacement_cost
FROM
    rental AS r
    INNER JOIN inventory AS inv ON r.inventory_id = inv.inventory_id
    INNER JOIN film AS f ON f.film_id = inv.film_id
WHERE
    r.return_date IS NULL
ORDER BY
    f.rental_rate DESC,
    f.replacement_cost DESC,
    f.title
LIMIT
    30;


-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
-- 1. The 1st film: The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
SELECT
    fa.film_id,
    f.title,
    CONCAT(act.first_name, ' ', act.last_name) AS actor_name
FROM
    actor AS act
    INNER JOIN film_actor AS fa ON act.actor_id = fa.actor_id
    INNER JOIN film AS f ON f.film_id = fa.film_id
WHERE
    act.first_name ILIKE 'Penelope'
    AND act.last_name ILIKE 'Monroe'
    AND f.description ILIKE '%sumo wrestler%';


-- 2. The 2nd film: A short documentary (less than 1 hour long), rated “R”.
SELECT
    f.film_id,
    f.title,
    f.length
FROM
    film AS f
    INNER JOIN film_category AS fc ON fc.film_id = f.film_id
    INNER JOIN category AS cat ON cat.category_id = fc.category_id
WHERE
    f.length < 60
    AND f.rating = 'R'
    AND cat.name ILIKE 'documentary';


-- 3. The 3rd film: A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
SELECT
    f.film_id,
    f.title,
    f.rental_rate,
    f.replacement_cost,
    pay.amount,
    r.return_date
FROM
    customer AS cu
    INNER JOIN payment AS pay ON cu.customer_id = pay.customer_id
    INNER JOIN rental AS r ON pay.rental_id = r.rental_id
    INNER JOIN inventory AS inv ON r.inventory_id = inv.inventory_id
    INNER JOIN film AS f ON inv.film_id = f.film_id
WHERE
    cu.first_name ILIKE 'Matthew'
    AND cu.last_name ILIKE 'Mahan'
    AND pay.amount > 4
    AND r.return_date >= '2005-07-28'
    AND r.return_date < '2005-08-02';


-- 4. The 4th film: His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.
SELECT DISTINCT
    f.film_id,
    f.title,
    f.description,
    f.replacement_cost
FROM
    customer AS cu
    INNER JOIN rental AS r ON cu.customer_id = r.customer_id
    INNER JOIN inventory AS inv ON r.inventory_id = inv.inventory_id
    INNER JOIN film AS f ON inv.film_id = f.film_id
WHERE
    cu.first_name ILIKE 'Matthew'
    AND cu.last_name ILIKE 'mahan'
    AND (
        title ILIKE '%boat%'
        OR description ILIKE '%boat%'
    )
ORDER BY
    f.replacement_cost DESC
LIMIT
    1;