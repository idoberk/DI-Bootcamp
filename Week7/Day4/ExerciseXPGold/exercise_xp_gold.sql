-- 🌟 Exercise 1: Comprehensive Competitor Analysis
-- Identify competitors who have won medals in both individual and team events. Use subqueries to distinguish between individual and team events and correlate with medal records.
WITH medal_rows AS (

    SELECT c_event.competitor_id, g_competitor.person_id, c_event.event_id, g_competitor.games_id, c_event.medal_id
    FROM competitor_event c_event
    JOIN games_competitor g_competitor ON c_event.competitor_id = g_competitor.id
    JOIN medal m ON c_event.medal_id = m.id
    WHERE m.medal_name != 'NA'
),

team_group AS (
    SELECT event_id, games_id, medal_id
    FROM medal_rows
    GROUP BY event_id, games_id, medal_id
    HAVING COUNT(*) > 1
),

labeled AS (
    SELECT mr.*,
        CASE WHEN (mr.event_id, mr.games_id, mr.medal_id) IN
                (SELECT event_id, games_id, medal_id FROM team_group)
            THEN 'team' ELSE 'individual'
        END AS event_type
    FROM medal_rows mr
)

SELECT l.person_id, p.full_name, COUNT(*) total_medals
FROM labeled l
JOIN person p
ON l.person_id = p.id
GROUP BY l.person_id, p.full_name
HAVING COUNT(DISTINCT l.event_type) = 2
ORDER BY l.person_id, p.full_name, total_medals DESC;


-- Create a temporary table to store the cumulative medal count for each region, then find the top 3 regions with the highest cumulative medal count. Use nested subqueries and aggregation.
DROP TABLE IF EXISTS medals_won_per_region;

CREATE TEMP TABLE medals_won_per_region AS
    SELECT nr.region_name, COUNT(*) total_medals_won
    FROM competitor_event c_event
    JOIN medal m ON m.id = c_event.medal_id
    JOIN games_competitor g_competitor ON g_competitor.id = c_event.competitor_id
    JOIN person_region pr ON pr.person_id = g_competitor.person_id
    JOIN noc_region nr ON pr.region_id = nr.id
    WHERE m.medal_name != 'NA'
    GROUP BY nr.region_name;

SELECT region_name, total_medals_won
FROM medals_won_per_region
WHERE total_medals_won IN (
    SELECT total_medals_won
    FROM (
        SELECT DISTINCT total_medals_won
        FROM medals_won_per_region
        ORDER BY total_medals_won DESC
        LIMIT 3
    ) top_regions
)
ORDER BY total_medals_won DESC;


-- Insert records into a temporary table for competitors who have won at least one gold medal and participated in more than 2 different games. Use subqueries to aggregate the data.
DROP TABLE IF EXISTS veteran_gold_winners;

CREATE TEMP TABLE veteran_gold_winners (
    person_id INTEGER,
    full_name VARCHAR(75),
    games_count INTEGER
);

INSERT INTO veteran_gold_winners (person_id, full_name, games_count)
WITH gold_winners AS (
    SELECT DISTINCT g_competitor.person_id
    FROM competitor_event c_event
    JOIN games_competitor g_competitor ON c_event.competitor_id = g_competitor.id
    JOIN medal m ON c_event.medal_id = m.id
    WHERE m.medal_name ILIKE '%gold%'
)

SELECT person_id, full_name, COUNT(DISTINCT games_id) games_count
FROM games_competitor
JOIN person ON person.id = games_competitor.person_id
WHERE person_id IN (
    SELECT person_id
    FROM gold_winners
)
GROUP BY person_id, full_name
HAVING COUNT(DISTINCT games_id) > 2;

SELECT * FROM veteran_gold_winners;


-- 🌟 Exercise 2: Advanced Data Manipulation and Optimization
-- Update the weights of competitors who have won medals in multiple games, setting it to the average weight of all medal winners. Use subqueries within the `UPDATE` statement.
DROP TABLE IF EXISTS person_copy;

CREATE TEMP TABLE person_copy AS SELECT * FROM person;

WITH medal_winners AS (
    SELECT DISTINCT g_competitor.person_id
    FROM games_competitor g_competitor
    JOIN competitor_event c_event ON c_event.competitor_id = g_competitor.id
    WHERE c_event.medal_id != 4
),

multi_games_winners AS (
    SELECT g_competitor.person_id
    FROM games_competitor g_competitor
    JOIN competitor_event c_event ON c_event.competitor_id = g_competitor.id
    WHERE c_event.medal_id != 4
    GROUP BY g_competitor.person_id
    HAVING COUNT(DISTINCT g_competitor.games_id) > 1
)

UPDATE person_copy
SET weight = (
    SELECT AVG(weight) medal_winners_avg_weight
        FROM person_copy
        WHERE weight > 0
        AND id IN (
            SELECT person_id FROM medal_winners
        )
)
WHERE id IN (SELECT person_id FROM multi_games_winners);


-- Create a temporary table to store the number of events participated by each competitor, then identify those who have participated in events across different seasons. Use complex subqueries for filtering.
DROP TABLE IF EXISTS events_per_competitor;

CREATE TEMP TABLE events_per_competitor AS
    SELECT g_competitor.person_id, COUNT(*) events_participated
    FROM games_competitor g_competitor
    JOIN competitor_event c_event ON c_event.competitor_id = g_competitor.id
    GROUP BY g_competitor.person_id
    ORDER BY g_competitor.person_id;

SELECT person_id, events_participated
FROM events_per_competitor
WHERE person_id IN (
    SELECT g_competitor.person_id
    FROM games_competitor g_competitor
    JOIN competitor_event c_event ON g_competitor.id = c_event.competitor_id
    JOIN games g ON g_competitor.games_id = g.id
    GROUP BY g_competitor.person_id
    HAVING COUNT(DISTINCT g.season) > 1
)
ORDER BY events_participated DESC, person_id;