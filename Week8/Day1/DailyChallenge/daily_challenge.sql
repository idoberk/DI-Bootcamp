CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    salary DECIMAL(10, 2),
    hire_date VARCHAR(20),
    department VARCHAR(50)
);

INSERT INTO employees (employee_id, employee_name, salary, hire_date, department) VALUES
(1, 'Amy West', 60000.00, '2021-01-15', 'HR'),
(2, 'Ivy Lee', 75000.50, '2020-05-22', 'Sales'),
(3, 'joe smith', 80000.75, '2019-08-10', 'Marketing'), 
(4, 'John White', 90000.00, '2020-11-05', 'Finance'),
(5, 'Jane Hill', 55000.25, '2022-02-28', 'IT'),
(6, 'Dave West', 72000.00, '2020-03-12', 'Marketing'),
(7, 'Fanny Lee', 85000.50, '2018-06-25', 'Sales'),
(8, 'Amy Smith', 95000.25, '2019-11-30', 'Finance'),
(9, 'Ivy Hill', 62000.75, '2021-07-18', 'IT'),
(10, 'Joe White', 78000.00, '2022-04-05', 'Marketing'),
(11, 'John Lee', 68000.50, '2018-12-10', 'HR'),
(12, 'Jane West', 89000.25, '2017-09-15', 'Sales'),
(13, 'Dave Smith', 60000.75, '2022-01-08', NULL),
(14, 'Fanny White', 72000.00, '2019-04-22', 'IT'),
(15, 'Amy Hill', 84000.50, '2020-08-17', 'Marketing'),
(16, 'Ivy West', 92000.25, '2021-02-03', 'Finance'),
(17, 'Joe Lee', 58000.75, '2018-05-28', 'IT'),
(18, 'John Smith', 77000.00, '2019-10-10', 'HR'),
(19, 'Jane Hill', 81000.50, '2022-03-15', 'Sales'),
(20, 'Dave White', 70000.25, '2017-12-20', 'Marketing');

-- Identify and handle any missing value.
SELECT * FROM employees WHERE department IS NULL OR TRIM(department) = '';

UPDATE employees
SET department = 'Unknown'
WHERE department IS NULL OR TRIM(department) = '';


-- Check for and eliminate any duplicate rows in the dataset.
SELECT employee_name, salary, hire_date, department, COUNT(*) AS copies
FROM employees
GROUP BY employee_name, salary, hire_date, department
HAVING COUNT(*) > 1;

SELECT LOWER(TRIM(employee_name)) AS name_key, COUNT(*) AS occurrences
FROM employees
GROUP BY LOWER(TRIM(employee_name))
HAVING COUNT(*) > 1;

DELETE FROM employees
WHERE employee_id IN (
    SELECT employee_id
    FROM (
        SELECT
            employee_id,
            ROW_NUMBER() OVER (
                PARTITION BY LOWER(TRIM(employee_name)), salary, hire_date, department
                ORDER BY employee_id
            ) AS row_num
        FROM employees
    ) AS ranked
    WHERE row_num > 1
);


-- Correct any structural issues, such as inconsistent naming conventions or formatting errors.
UPDATE employees
SET
    employee_name = INITCAP(TRIM(employee_name)),
    department = CASE
        WHEN UPPER(TRIM(department)) IN ('HR', 'IT') THEN UPPER(TRIM(department))
        ELSE INITCAP(TRIM(department))
    END,
    hire_date = TRIM(hire_date);

-- Verify
SELECT DISTINCT department FROM employees ORDER BY department;


-- Ensure all columns have appropriate data types (e.g. the hire_date column).
ALTER TABLE employees
    ALTER COLUMN hire_date TYPE DATE USING hire_date::date;

-- Verify the types
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'employees'
ORDER BY ordinal_position;


-- Detect and address any outliers that may skew the analysis.
WITH bounds AS (
    SELECT
        percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
        percentile_cont(0.75) WITHIN GROUP (ORDER BY salary) AS q3
    FROM employees
)

SELECT
    q1,
    q3,
    q1 - 1.5 * (q3 - q1) AS lower_bound,
    q3 + 1.5 * (q3 - q1) AS upper_bound
FROM bounds;

WITH bounds AS (
    SELECT
        percentile_cont(0.25) WITHIN GROUP (ORDER BY salary) AS q1,
        percentile_cont(0.75) WITHIN GROUP (ORDER BY salary) AS q3
    FROM employees
)

SELECT e.*
FROM employees AS e, bounds AS b
WHERE e.salary < b.q1 - 1.5 * (b.q3 - b.q1)
   OR e.salary > b.q3 + 1.5 * (b.q3 - b.q1);

-- If the query above returned rows and you decide they are errors, delete them:
-- DELETE FROM employees WHERE employee_id IN (...);


-- Standardize and normalize data where applicable to ensure consistency.
ALTER TABLE employees
    ADD COLUMN IF NOT EXISTS salary_zscore NUMERIC(10, 4),
    ADD COLUMN IF NOT EXISTS salary_minmax NUMERIC(10, 4);

UPDATE employees AS e
SET
    salary_zscore = (e.salary - s.mean_salary) / s.std_salary,
    salary_minmax = (e.salary - s.min_salary) / (s.max_salary - s.min_salary)
FROM (
    SELECT
        AVG(salary)         AS mean_salary,
        STDDEV_SAMP(salary) AS std_salary,
        MIN(salary)         AS min_salary,
        MAX(salary)         AS max_salary
    FROM employees
) AS s;

-- Final check
SELECT * FROM employees ORDER BY employee_id;