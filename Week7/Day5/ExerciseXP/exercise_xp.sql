-- 🌟 Exercise 1: Movie Rankings and Analysis
-- Rank Movies by Popularity within Each Genre
-- Use the `RANK()` function to rank movies by their popularity within each genre. Display the genre name, movie title, and their rank based on popularity.
SELECT g.genre_name,
    m.title,
    RANK() OVER (PARTITION BY g.genre_id ORDER BY m.popularity DESC) genre_popularity
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY g.genre_name, genre_popularity;


-- Identify the Top 3 Movies by Revenue within Each Production Company
-- Use the `NTILE()` function to divide the movies produced by each production company into quartiles based on revenue. Display the company name, movie title, revenue, and quartile.
WITH ranked_movies AS (
    SELECT p_company.company_name,
        m.title,
        m.revenue,
        NTILE(4) OVER (PARTITION BY p_company.company_id ORDER BY m.revenue DESC) revenue_quartile,
        ROW_NUMBER() OVER (PARTITION BY p_company.company_id ORDER BY m.revenue DESC) revenue_position
    FROM movie m
    JOIN movie_company m_company ON m.movie_id = m_company.movie_id
    JOIN production_company p_company ON m_company.company_id = p_company.company_id
    WHERE m.revenue > 0
)

SELECT company_name, title, revenue, revenue_quartile
FROM ranked_movies
WHERE revenue_position <= 3
ORDER BY company_name, revenue_position;


-- Calculate the Running Total of Movie Budgets for Each Genre
-- Use the `SUM()` function with the `ROWS` frame specification to calculate the running total of movie budgets within each genre. Display the genre name, movie title, budget, and running total budget.
SELECT g.genre_name,
    m.title,
    m.budget,
    SUM(m.budget) OVER (PARTITION BY g.genre_id ORDER BY m.release_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) genre_running_total_budget
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id;


-- Identify the Most Recent Movie for Each Genre
-- Use the `FIRST_VALUE()` function to find the most recent movie within each genre based on the release date. Display the genre name, movie title, and release date.
SELECT DISTINCT g.genre_name,
    FIRST_VALUE(m.title) OVER (PARTITION BY g.genre_id ORDER BY m.release_date DESC) most_recent_title,
    FIRST_VALUE(m.release_date) OVER (PARTITION BY g.genre_id ORDER BY m.release_date DESC) most_recent_release_date
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
ORDER BY most_recent_release_date DESC;


-- 🌟 Exercise 2: Cast and Crew Performance Analysis
-- Rank Actors by Their Appearance in Movies
-- Use the `DENSE_RANK()` function to rank actors based on the number of movies they have appeared in. Display the actor's name and their rank.
SELECT p.person_name,
    COUNT(*) total_movies,
    DENSE_RANK() OVER (ORDER BY COUNT(DISTINCT m.movie_id) DESC) actor_rank
FROM movie m
JOIN movie_cast m_cast ON m.movie_id = m_cast.movie_id
JOIN person p ON m_cast.person_id = p.person_id
GROUP BY p.person_name
ORDER BY total_movies DESC;


-- Identify the Top Director by Average Movie Rating
-- Use a CTE and the `RANK()` function to find the director with the highest average movie rating. Display the director's name and their average rating.
WITH director_avg AS (
    SELECT p.person_name, ROUND(AVG(m.vote_average), 2) avg_movies_rating
    FROM movie m
    JOIN movie_crew m_crew ON m.movie_id = m_crew.movie_id
    JOIN person p ON m_crew.person_id = p.person_id
    WHERE m_crew.job = 'Director' AND m.vote_average > 0
    GROUP BY p.person_id, p.person_name
    HAVING COUNT(*) >= 3
),

ranked_directors AS (
    SELECT person_name,
        avg_movies_rating,
        RANK() OVER (ORDER BY avg_movies_rating DESC) rating_rank
    FROM director_avg
)

SELECT person_name, avg_movies_rating, rating_rank
FROM ranked_directors
WHERE rating_rank = 1;


-- Calculate the Cumulative Revenue of Movies Acted by Each Actor
-- Use the `SUM()` function to calculate the cumulative revenue of movies acted by each actor. Display the actor's name and the cumulative revenue.
SELECT DISTINCT p.person_name,
    SUM(m.revenue) OVER (PARTITION BY p.person_id) cumulative_revenue
FROM movie m
JOIN movie_cast m_cast ON m.movie_id = m_cast.movie_id
JOIN person p ON m_cast.person_id = p.person_id
ORDER BY cumulative_revenue DESC;


-- Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have the highest total budget. Display the director's name and the total budget.
WITH director_total_budget AS (
    SELECT p.person_name, SUM(m.budget) total_budget
    FROM movie m
    JOIN movie_crew m_crew ON m.movie_id = m_crew.movie_id
    JOIN person p ON m_crew.person_id = p.person_id
    WHERE m_crew.job = 'Director' AND m.budget > 0
    GROUP BY p.person_id, p.person_name
),

ranked_directors_by_total_budget AS (
    SELECT person_name,
        total_budget,
        RANK() OVER (ORDER BY total_budget DESC) budget_rank 
    FROM director_total_budget
)

SELECT *
FROM ranked_directors_by_total_budget
WHERE budget_rank = 1;