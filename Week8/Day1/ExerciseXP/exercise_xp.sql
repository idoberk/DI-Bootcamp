-- 🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis
-- Create a temporary table that join all tables and create a new one using `LEFT JOIN`.
-- Create an unique identifier code between the columns `employee_id` and `date` and call it `id`.
-- Convert the column `date` to `DATE` type because it was previously configured as `TIMESTAMP`.
-- Transform this new table into a dataset `df_employee` for analysis.
DROP TABLE IF EXISTS emp_dataset;

CREATE TEMP TABLE emp_dataset AS
    SELECT
        s."date",
        s.employee_id,
        s.employee_name,
        e."GEN(M_F)" AS gender,
        e.age,
        s.salary,
        f.function_group,
        c.company_name,
        c.company_city,
        c.company_state,
        c.company_type,
        c.const_site_category
    FROM salaries AS s
    LEFT JOIN employees AS e
        ON s.employee_id = e.employee_code_emp
        AND s.comp_code = e.comp_code_emp
    LEFT JOIN functions AS f
        ON s.func_code = f.function_code
    LEFT JOIN companies AS c
        ON s.comp_name = c.company_name;

DROP TABLE IF EXISTS df_employee;

CREATE TABLE df_employee AS
    SELECT
        employee_id || '_' || CAST("date" AS TEXT) AS id,
        CAST("date" AS DATE) AS month_year,
        employee_id,
        employee_name,
        gender,
        age,
        salary,
        function_group,
        company_name,
        company_city,
        company_state,
        company_type,
        const_site_category
    FROM emp_dataset;

SELECT
    (SELECT COUNT(*) FROM salaries)    AS salaries_rows,
    (SELECT COUNT(*) FROM df_employee) AS df_rows;

SELECT * FROM df_employee LIMIT 10;


-- 🌟 Exercise 2: Cleaning Data for Consistency and Quality
-- Run the following SQLite request and observe your new table.
SELECT * FROM df_employee;

-- Remove all unwanted spaces from all text columns using `TRIM`.
UPDATE df_employee
SET
    id = TRIM(id),
    employee_id = TRIM(employee_id),
    employee_name = TRIM(employee_name),
    gender = TRIM(gender),
    age = TRIM(age),
    salary = TRIM(salary),
    function_group = TRIM(function_group),
    company_name = TRIM(company_name),
    company_city = TRIM(company_city),
    company_state = TRIM(company_state),
    company_type = TRIM(company_type),
    const_site_category = TRIM(const_site_category);

-- Check for `NULL` values and empty values.
SELECT *
FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR age IS NULL OR age = ''
   OR salary IS NULL OR salary = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';

-- Delete rows of the detected missing values.
DELETE FROM df_employee
WHERE id IS NULL OR id = ''
   OR month_year IS NULL
   OR employee_id IS NULL OR employee_id = ''
   OR employee_name IS NULL OR employee_name = ''
   OR gender IS NULL OR gender = ''
   OR age IS NULL OR age = ''
   OR salary IS NULL OR salary = ''
   OR function_group IS NULL OR function_group = ''
   OR company_name IS NULL OR company_name = ''
   OR company_city IS NULL OR company_city = ''
   OR company_state IS NULL OR company_state = ''
   OR company_type IS NULL OR company_type = ''
   OR const_site_category IS NULL OR const_site_category = '';


-- 🌟 Exercise 3: Calculating Current Employee Counts by Company
-- How many employees do the companies have today?
-- Group them by company.
SELECT
    company_name,
    COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_name
ORDER BY employee_count DESC;


-- 🌟 Exercise 4: Analyzing Employee Distribution by City and Over Time
-- What is the total number of employees each city? Add a percentage column.
SELECT
    company_city,
    COUNT(DISTINCT employee_id) AS employee_count,
    ROUND(
        100.0 * COUNT(DISTINCT employee_id)
        / SUM(COUNT(DISTINCT employee_id)) OVER (),
        2
    ) AS percentage
FROM df_employee
WHERE month_year = (SELECT MAX(month_year) FROM df_employee)
GROUP BY company_city
ORDER BY employee_count DESC;

-- What is the total number of employees each month?
SELECT
    month_year,
    COUNT(DISTINCT employee_id) AS employee_count
FROM df_employee
GROUP BY month_year
ORDER BY month_year;

-- What is the average number of employees each month?
SELECT
    ROUND(AVG(employee_count), 1) AS avg_employees_per_month
FROM (
    SELECT
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
) AS monthly_counts;


-- 🌟 Exercise 5: Analyzing Employment Trends and Salary Metrics
-- What is the minimum and maximum number of employees throughout all the months? In which months were they?
WITH monthly_counts AS (
    SELECT
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY month_year
)

SELECT
    month_year,
    employee_count,
    CASE
        WHEN employee_count = (SELECT MAX(employee_count) FROM monthly_counts)
            THEN 'max'
        ELSE 'min'
    END AS extreme
FROM monthly_counts
WHERE employee_count = (SELECT MAX(employee_count) FROM monthly_counts)
   OR employee_count = (SELECT MIN(employee_count) FROM monthly_counts)
ORDER BY employee_count DESC, month_year;

-- What is the monthly average number of employees by function group?
SELECT
    function_group,
    ROUND(AVG(employee_count), 1) AS avg_monthly_employees
FROM (
    SELECT
        function_group,
        month_year,
        COUNT(DISTINCT employee_id) AS employee_count
    FROM df_employee
    GROUP BY function_group, month_year
) AS monthly_by_group
GROUP BY function_group
ORDER BY avg_monthly_employees DESC;

-- What is the annual average salary?
SELECT
    EXTRACT(YEAR FROM month_year)::int AS year,
    ROUND(AVG(salary), 2) AS avg_salary
FROM df_employee
GROUP BY EXTRACT(YEAR FROM month_year)
ORDER BY year;