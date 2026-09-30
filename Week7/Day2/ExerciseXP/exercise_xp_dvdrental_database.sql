SELECT * FROM customer;

SELECT CONCAT(first_name, ' ', last_name) AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * FROM customer ORDER BY first_name DESC;

SELECT film_id, title, film.description, release_year, rental_rate FROM film ORDER BY rental_rate;

SELECT address.address, phone FROM address WHERE district = 'Texas';

SELECT * FROM film WHERE film_id IN (15, 150);

SELECT film_id, title, film.description, film.length, rental_rate FROM film WHERE title ILIKE '%avengers%';

SELECT film_id, title, film.description, film.length, rental_rate FROM film WHERE title ILIKE 'av%';

SELECT * FROM film ORDER BY rental_rate LIMIT 10;

SELECT * FROM film ORDER BY rental_rate OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;

SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date 
FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY c.customer_id;

SELECT * FROM film AS f
LEFT JOIN inventory AS i
ON f.film_id = i.film_id
WHERE i.inventory_id IS NULL
ORDER BY f.film_id;

SELECT city.city_id, country.country, city.city FROM city
LEFT JOIN country
ON city.country_id = country.country_id
ORDER BY country.country;

SELECT p.staff_id, c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id
ORDER BY p.staff_id, p.payment_date;