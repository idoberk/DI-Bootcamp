-- Exercise 1: Complex Subquery Analysis
-- Find the average age of competitors who have won at least one medal, grouped by the type of medal they won. Use a correlated subquery to achieve this.
WITH medal_winner_ages AS (
    SELECT DISTINCT ce.competitor_id, me.medal_name,
    (   SELECT age
        FROM games_competitor gc
        WHERE gc.id = ce.competitor_id
    ) age
    FROM medal me
    JOIN competitor_event ce ON me.id = ce.medal_id
    WHERE me.medal_name != 'NA'
)

SELECT
    ROUND(AVG(age), 2) avg_age,
    medal_name
FROM
    medal_winner_ages
GROUP BY
    medal_name
ORDER BY
    avg_age DESC;


-- Identify the top 5 regions with the highest number of unique competitors who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.
SELECT
    nr.region_name,
    COUNT(DISTINCT competitor_region.person_id) num_of_competitors
FROM noc_region nr
JOIN (  SELECT pr.region_id, pr.person_id
        FROM person_region pr
        WHERE pr.person_id IN 
        (   SELECT gc.person_id
            FROM games_competitor gc
            WHERE gc.id IN
            (   SELECT competitor_id
                FROM competitor_event
                GROUP BY competitor_id
                HAVING COUNT(DISTINCT event_id) > 3))) competitor_region 
                ON nr.id = competitor_region.region_id
GROUP BY
    nr.region_name
ORDER BY
    num_of_competitors DESC
LIMIT 5;


-- Create a temporary table to store the total number of medals won by each competitor and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
CREATE TEMP TABLE medals_per_competitor AS
SELECT competitor_id, total_medals
FROM (
    SELECT ce.competitor_id, COUNT(*) total_medals
    FROM competitor_event ce
    JOIN medal me ON me.id = ce.medal_id
    WHERE me.medal_name != 'NA'
    GROUP BY ce.competitor_id
) medal_counts
WHERE total_medals > 2;

SELECT * FROM medals_per_competitor;


-- Use a subquery within a `DELETE` statement to remove records of competitors who have not won any medals from a temporary table created for analysis.
CREATE TEMP TABLE competitor_analysis AS
SELECT id AS competitor_id, person_id, age
FROM games_competitor;

SELECT COUNT(*) FROM competitor_analysis;

DELETE FROM competitor_analysis
WHERE competitor_id NOT IN (
    SELECT ce.competitor_id
    FROM medal me
    JOIN competitor_event ce ON me.id = ce.medal_id
    WHERE me.medal_name != 'NA');


-- Exercise 2: Advanced Data Manipulation and Optimization
-- Update the heights of competitors based on the average height of competitors from the same region. Use a correlated subquery within the `UPDATE` statement.
CREATE INDEX IF NOT EXISTS idx_person_region_person ON person_region (person_id);
CREATE INDEX IF NOT EXISTS idx_person_region_region ON person_region (region_id);

CREATE TEMP TABLE person_copy AS SELECT * FROM person;

UPDATE person_copy pc
SET height = (
    SELECT AVG(p2.height)
    FROM person p2
    WHERE p2.height > 0
      AND p2.id IN (
          SELECT pr2.person_id
          FROM person_region pr2
          WHERE pr2.region_id IN (
              SELECT pr.region_id
              FROM person_region pr
              WHERE pr.person_id = pc.id
          )
      )
)
WHERE EXISTS (
    SELECT 1
    FROM person_region pr
    WHERE pr.person_id = pc.id
) AND pc.id <= 1000; -- Limiting the amount of people we update because the query takes a very long time to complete for the entire table.


-- Insert new records into a temporary table for competitors who participated in more than one event in the same games and list their total number of events participated. Use nested subqueries for filtering.
CREATE TEMP TABLE multi_event_competitors (
    competitor_id INT,
    total_events  INT
);

INSERT INTO multi_event_competitors (competitor_id, total_events)
SELECT
    ce.competitor_id,
    COUNT(DISTINCT ce.event_id)
FROM competitor_event ce
WHERE ce.competitor_id IN (
    SELECT competitor_id
    FROM competitor_event
    GROUP BY competitor_id
    HAVING COUNT(DISTINCT event_id) > 1
)
GROUP BY ce.competitor_id;

-- Identify regions where the average number of medals won per competitor is greater than the overall average. Use subqueries to calculate and compare averages.
WITH competitor_medals AS (
    SELECT
        gc.id AS competitor_id,
        gc.person_id,
        COUNT(me.id) AS medals
    FROM games_competitor gc
    LEFT JOIN competitor_event ce ON ce.competitor_id = gc.id
    LEFT JOIN medal me ON me.id = ce.medal_id AND me.medal_name != 'NA'
    GROUP BY gc.id, gc.person_id
)
SELECT
    nr.region_name,
    ROUND(AVG(cm.medals), 3) AS avg_medals_per_competitor
FROM competitor_medals cm
JOIN person_region pr ON pr.person_id = cm.person_id
JOIN noc_region nr ON nr.id = pr.region_id
GROUP BY nr.region_name
HAVING AVG(cm.medals) > (SELECT AVG(medals) FROM competitor_medals)
ORDER BY avg_medals_per_competitor DESC;


-- Create a temporary table to track competitors’ participation across different seasons and identify those who have participated in both Summer and Winter games.
CREATE TEMP TABLE person_seasons AS
SELECT DISTINCT
    gc.person_id,
    g.season
FROM games_competitor gc
JOIN games g ON g.id = gc.games_id;

SELECT person_id
FROM person_seasons
GROUP BY person_id
HAVING COUNT(DISTINCT season) = 2;