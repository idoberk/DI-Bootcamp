### **🌟 Exercise 1: Building a Comprehensive Dataset for Employee Analysis**

1. Create a temporary table that join all tables and create a new one using `LEFT JOIN`.
2. Create an unique identifier code between the columns `employee_id` and `date` and call it `id`.
3. Convert the column `date` to `DATE` type because it was previously configured as `TIMESTAMP`.
4. Transform this new table into a dataset `df_employee` for analysis.

---

### **🌟 Exercise 2: Cleaning Data for Consistency and Quality**

1. Run the following SQLite request and observe your new table.
    ```
    SELECT * FROM df_employee;
    ```
2. Remove all unwanted spaces from all text columns using `TRIM`.
3. Check for `NULL` values and empty values.
4. Delete rows of the detected missing values.

---

### **🌟 Exercise 3: Calculating Current Employee Counts by Company**

- How many employees do the companies have today?
- Group them by company.

---

### **🌟 Exercise 4: Analyzing Employee Distribution by City and Over Time**

- What is the total number of employees each city? Add a percentage column.
- What is the total number of employees each month?
- What is the average number of employees each month?

---

### **🌟 Exercise 5: Analyzing Employment Trends and Salary Metrics**

- What is the minimum and maximum number of employees throughout all the months? In which months were they?
- What is the monthly average number of employees by function group?
- What is the annual average salary?
