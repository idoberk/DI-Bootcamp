### Instructions

In this puzzle you have to go through all the SQL queries and provide us the output of the requests before executing them (ie. make an assumption).
Then, execute them to make sure you were correct.

**Queries**

```sql
CREATE TABLE FirstTab (
id integer,
name VARCHAR(10)
)

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar')

CREATE TABLE SecondTab (
id integer
)

INSERT INTO SecondTab VALUES
(5),
(NULL)
```

**Questions**

- Q1. What will be the OUTPUT of the following statement?
    ```sql
      SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
    ```
- Q2. What will be the OUTPUT of the following statement?
    ```sql
    SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
    ```
- Q3. What will be the OUTPUT of the following statement?
    ```sql
    SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
    ```
- Q4. What will be the OUTPUT of the following statement?
    ```sql
    SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
    ```

**Answers**

- A1. 0
- A2. 2
- A3. 0
- A4. 2
