-- 🌟 Task 1: Calculate the Average Budget Growth Rate for Each Production Company
-- Calculate the average budget growth rate for each production company across all movies they have produced. Use window functions to determine the budget growth rate and then calculate the average growth rate.
WITH previous_movie_budget AS (
    SELECT p_company.company_name,
        p_company.company_id,
        m.budget,
        LAG(m.budget) OVER (PARTITION BY p_company.company_id ORDER BY m.release_date) prev_budget
    FROM movie m
    JOIN movie_company m_company ON m.movie_id = m_company.movie_id
    JOIN production_company p_company ON m_company.company_id = p_company.company_id
),

per_movie_growth_rate AS (
    SELECT company_name,
        company_id,
        budget,
        (budget - prev_budget) / NULLIF(prev_budget::numeric, 0) * 100 budget_growth_rate
    FROM previous_movie_budget
)

SELECT company_name, ROUND(AVG(budget_growth_rate), 2) avg_growth_rate_pct
FROM per_movie_growth_rate
GROUP BY company_id, company_name
ORDER BY avg_growth_rate_pct DESC NULLS LAST;


-- 🌟 Task 2: Determine the Most Consistently High-Rated Actor
-- Identify the actor who has appeared in the most movies that are rated above the average rating of all movies. Use window functions and CTEs to calculate the average rating and filter the actors based on this criterion.
WITH movie_with_avg AS (
    SELECT movie_id,
        title,
        vote_average,
        AVG(vote_average) OVER() overall_avg
        FROM movie
),

high_rated_movies AS (
    SELECT *
    FROM movie_with_avg 
    WHERE vote_average > overall_avg
),

high_rated_actors AS (
    SELECT p.person_id, p.person_name, COUNT(DISTINCT hrm.movie_id) movies_above_average
    FROM high_rated_movies hrm
    JOIN movie_cast m_cast ON hrm.movie_id = m_cast.movie_id
    JOIN person p ON m_cast.person_id = p.person_id
    GROUP BY p.person_id, p.person_name
),

actors_ranking AS (
    SELECT person_id,
    person_name,
    movies_above_average,
    DENSE_RANK() OVER (ORDER BY movies_above_average DESC) actor_rank
    FROM high_rated_actors
)

SELECT * FROM actors_ranking WHERE actor_rank = 1;


-- 🌟 Task 3: Calculate the Rolling Average Revenue for Each Genre
-- Calculate the rolling average revenue for movies within each genre, considering only the last three movies released in the genre. Use window functions with the `ROWS` frame specification to achieve this.
SELECT m.movie_id,
    m.title,
    g.genre_name,
    m.revenue,
    m.release_date,
    ROUND(AVG(m.revenue) OVER (PARTITION BY g.genre_id ORDER BY m.release_date, m.movie_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) rolling_avg_revenue
FROM movie m
JOIN movie_genres mg ON m.movie_id = mg.movie_id
JOIN genre g ON mg.genre_id = g.genre_id
WHERE m.revenue > 0 AND m.release_date IS NOT NULL
ORDER BY g.genre_id, m.release_date, m.movie_id;


-- 🌟 Task 4: Identify the Highest-Grossing Movie Series
-- Identify the movie series (based on shared keywords) with the highest total revenue. Use window functions and CTEs to group movies by their series and calculate the total revenue.
Here is a solution. I'm giving it in chat, not editing your file, and I haven't run it. The table and column names (keyword, movie_keywords, keyword_name) are my assumptions from your earlier schema, so adjust them if they differ.


-- Series = a keyword shared by 2 to 20 movies (with recorded revenue).
-- Below 2 isn't a series; above 20 is usually a generic tag like "sequel"
-- or "based on novel". Revenue of 0 is treated as unrecorded and excluded.
-- Keyword groups overlap (a movie has many keywords), which is fine because
-- each series total sums only its own movies; totals are never added together.
WITH movie_keyword_revenue AS (
    SELECT k.keyword_id,
        k.keyword_name,
        m.movie_id,
        m.revenue
    FROM movie m
    JOIN movie_keywords mk ON m.movie_id = mk.movie_id
    JOIN keyword k ON mk.keyword_id = k.keyword_id
    WHERE m.revenue > 0
),

series_totals AS (
    SELECT keyword_id,
        keyword_name,
        COUNT(*) OVER (PARTITION BY keyword_id) movies_in_series,
        SUM(revenue) OVER (PARTITION BY keyword_id) series_revenue
    FROM movie_keyword_revenue
),

candidate_series AS (
    SELECT DISTINCT keyword_id, keyword_name, movies_in_series, series_revenue
    FROM series_totals
    WHERE movies_in_series BETWEEN 2 AND 20
),

series_ranking AS (
    SELECT *,
        RANK() OVER (ORDER BY series_revenue DESC) revenue_rank
    FROM candidate_series
)

SELECT *
FROM series_ranking
WHERE revenue_rank = 1;