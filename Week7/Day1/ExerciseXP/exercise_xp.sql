CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR (100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL CHECK (price >= 0)
)

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR (50) NOT NULL,
    last_name VARCHAR (100) NOT NULL
)

INSERT INTO items (item_name, price)
VALUES('Small Desk', 100), ('Large Desk', 300), ('Fan', 80);

INSERT INTO customers (first_name, last_name)
VALUES('Greg', 'Jones'), ('Sandra', 'Scott'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

SELECT * FROM items;

SELECT * FROM items WHERE price > 80;

SELECT * FROM items WHERE price < 300;

SELECT * FROM customers WHERE last_name = 'Smith'; -- Will return an empty table because it doesn't match any existing customer.

SELECT * FROM customers WHERE last_name = 'Jones';

SELECT * FROM customers WHERE first_name != 'Jones';