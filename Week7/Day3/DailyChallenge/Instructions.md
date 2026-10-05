### **Instructions**

You are going to practice tables relationships

### **Part I**

1. Create 2 tables: Customer and Customer profile. They have a One to One relationship.
	- A customer can have only one profile, and a profile belongs to only one customer
	- The Customer table should have the columns: `id`, `first_name`, `last_name NOT NULL`
	- The Customer profile table should have the columns: `id`, `isLoggedIn DEFAULT false` (a Boolean), `customer_id` (a reference to the Customer table)
2. Insert those customers
	- John, Doe
	- Jerome, Lalu
	- Lea, Rive
3. Insert those customer profiles, use subqueries
	- John is loggedIn
	- Jerome is not logged in
4. Use the relevant types of Joins to display:
	- The `first_name` of the LoggedIn customers
	- All the customers `first_name` and `isLoggedIn` columns - even the customers those who don’t have a profile.
	- The number of customers that are not LoggedIn

---

### **Part II**

1. Create a table named Book, with the columns: `book_id SERIAL PRIMARY KEY`, `title NOT NULL`, `author NOT NULL`
2. Insert those books:
	- Alice In Wonderland, Lewis Carroll
	- Harry Potter, J.K Rowling
	- To kill a mockingbird, Harper Lee
3. Create a table named Student, with the columns: `student_id SERIAL PRIMARY KEY`, `name NOT NULL UNIQUE`, `age`. Make sure that the age is never bigger than 15 (Find an SQL method);
4. Insert those students:
	- John, 12
	- Lera, 11
	- Patrick, 10
	- Bob, 14
5. Create a table named Library, with the columns:
	- `book_fk_id ON DELETE CASCADE ON UPDATE CASCADE`
	- `student_id ON DELETE CASCADE ON UPDATE CASCADE`
	- `borrowed_date`

	This table, is a junction table for a Many to Many relationship with the Book and Student tables: A student can borrow many books, and a book can be borrowed by many children
	- `book_fk_id` is a Foreign Key representing the column `book_id` from the Book table
	- `student_fk_id` is a Foreign Key representing the column `student_id` from the Student table
	- The pair of Foreign Keys is the Primary Key of the Junction Table
6. Add 4 records in the junction table, use subqueries.
	- the student named John, borrowed the book Alice In Wonderland on the 15/02/2022
	- the student named Bob, borrowed the book To kill a mockingbird on the 03/03/2021
	- the student named Lera, borrowed the book Alice In Wonderland on the 23/05/2021
	- the student named Bob, borrowed the book Harry Potter the on 12/08/2021
7. Display the data
	- Select all the columns from the junction table
	- Select the name of the student and the title of the borrowed books
	- Select the average age of the children, that borrowed the book Alice in Wonderland
	- Delete a student from the Student table, what happened in the junction table?