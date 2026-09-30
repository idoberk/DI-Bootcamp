CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
)

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

SELECT * FROM actors LIMIT 1000;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

SELECT age FROM actors;

SELECT first_name, last_name FROM actors;

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('John','Doe','21/10/1993', 100);

SELECT * FROM actors WHERE number_oscars > 2;

SELECT * FROM actors WHERE first_name = 'Matt';

SELECT * FROM actors WHERE first_name != 'Matt';

SELECT * FROM actors WHERE first_name = 'John' AND last_name = 'Doe';

SELECT * FROM actors WHERE first_name = 'John' AND last_name = 'Damon';

SELECT * FROM actors WHERE first_name = 'John' OR last_name = 'Damon';

SELECT * FROM actors WHERE first_name = 'John' AND NOT last_name = 'Damon';

SELECT * FROM actors WHERE (number_oscars > 2 AND number_oscars < 100) OR last_name = 'Doe';

SELECT * FROM actors WHERE (number_oscars > 2 AND number_oscars < 100) OR NOT last_name = 'Clooney';

SELECT * FROM actors WHERE last_name LIKE '%mon';

SELECT * FROM actors WHERE first_name LIKE 'Jo%';

SELECT * FROM actors LIMIT 3;

SELECT * FROM actors WHERE last_name LIKE '%ooney' LIMIT 1;

SELECT * FROM actors WHERE actor_id > 2;

SELECT * FROM actors OFFSET 2;

SELECT * FROM actors LIMIT 1 OFFSET 2;

SELECT * FROM actors ORDER BY last_name ASC;

SELECT * FROM actors ORDER BY last_name DESC;

SELECT * FROM actors ORDER BY number_oscars ASC;

UPDATE actors SET number_oscars = '7' WHERE first_name = 'Matt'
RETURNING actor_id, first_name, last_name, age, number_oscars;

DELETE FROM actors WHERE actor_id = 2;

SELECT COUNT(*) FROM actors;

INSERT INTO actors (last_name, age, number_oscars)
VALUES('Levi','24/07/1997', 5);