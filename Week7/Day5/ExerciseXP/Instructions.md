### **👩‍🏫 👩🏿‍🏫 What You'll learn**

Through this series of exercises, you will enhance your SQL skills and gain valuable insights into data manipulation and analysis in the entertainment sector. Here's what we will cover:

- Advanced Window Functions: Learn to apply window functions like `RANK()`, `NTILE()`, and `SUM()` to perform complex rankings, segmentations, and cumulative calculations.
- Insights into Movie Industry Trends: Analyze trends in movie popularity, revenue distribution, and budget allocations across different genres and production companies.
- Performance Evaluation of Cast and Crew: Evaluate the performance of actors and directors based on various metrics such as movie appearances, average ratings, and budget management.
- Real-World SQL Applications: Gain hands-on experience with practical SQL applications that reflect scenarios encountered by data analysts in the film industry.
- Analytical Thinking and Problem Solving: Develop your analytical thinking by tackling tasks that require careful consideration of both the data available and the SQL techniques suitable for extracting meaningful insights.

By the end of these exercises, you will have not only advanced your technical skills but also acquired a deeper understanding of the dynamics within the film industry.

---

### **🌟 Exercise 1: Movie Rankings and Analysis**

### **Task 1: Rank Movies by Popularity within Each Genre**

Use the `RANK()` function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.

### **Task 2: Identify the Top 3 Movies by Revenue within Each Production Company**

Use the `NTILE()` function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.

### **Task 3: Calculate the Running Total of Movie Budgets for Each Genre**

Use the `SUM()` function with the `ROWS` frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.

### **Task 4: Identify the Most Recent Movie for Each Genre**

Use the `FIRST_VALUE()` function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.

---

### **🌟 Exercise 2: Cast and Crew Performance Analysis**

### **Task 1: Rank Actors by Their Appearance in Movies**

Use the `DENSE_RANK()` function to rank actors based on the number of movies they have appeared in. Display the actor's name and their rank.

### **Task 2: Identify the Top Director by Average Movie Rating**

Use a CTE and the `RANK()` function to find the director with the highest average movie rating. Display the director's name and their average rating.

### **Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor**

Use the `SUM()` function to calculate the cumulative revenue of movies acted by each actor. Display the actor's name and the cumulative revenue.

### **Task 4: Identify the Director Whose Movies Have the Highest Total Budget**

Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director's name and the total budget.