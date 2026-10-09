-- Exercise 1: Detailed Medal Analysis
-- Identify competitors who have won at least one medal in events spanning both Summer and Winter Olympics. Create a temporary table to store these competitors and their medal counts for each season, and then display the contents of this table.
CREATE TEMP TABLE multi_seasonal_medal_winners AS 
    WITH medal_winners AS (
        SELECT gc.person_id, me.medal_name, games.season
        FROM medal me
        JOIN competitor_event ce ON me.id = ce.medal_id
        JOIN games_competitor gc ON ce.competitor_id = gc.id
        JOIN games ON gc.games_id = games.id
        WHERE me.medal_name != 'NA'
    ),

    season_counts AS (
        SELECT person_id, season, COUNT(medal_name) medal_count
        FROM medal_winners
        GROUP BY person_id, season
    )

    SELECT person_id, season, medal_count
    FROM season_counts
    WHERE person_id IN (
        SELECT person_id
        FROM season_counts
        GROUP BY person_id
        HAVING COUNT(*) = 2
    );

SELECT * FROM multi_seasonal_medal_winners ORDER BY person_id;


-- Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors with the highest total number of medals across all sports. Display the contents of this table.
CREATE TEMP TABLE two_sport_medal_winners AS
    WITH sport_medal_winners AS (
        SELECT gc.person_id, me.medal_name, s.sport_name
        FROM medal me
        JOIN competitor_event ce ON me.id = ce.medal_id
        JOIN games_competitor gc ON ce.competitor_id = gc.id
        JOIN event e ON ce.event_id = e.id
        JOIN sport s ON e.sport_id = s.id
        WHERE me.medal_name != 'NA'
    )

    SELECT person_id, COUNT(DISTINCT sport_name) distinct_sports, COUNT(medal_name) total_medals
    FROM sport_medal_winners
    GROUP BY person_id
    HAVING COUNT(DISTINCT sport_name) = 2;


SELECT *
FROM (
    SELECT person_id, distinct_sports, total_medals
    FROM two_sport_medal_winners
    ORDER BY total_medals DESC
    LIMIT 3
) top_three;
-- Exercise 2: Region and Competitor Performance
-- Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. Use a subquery to determine the event with the highest number of medals for each competitor, and then display the top 5 regions with the highest total medals.
WITH event_medal_winners_by_region AS (
    SELECT gc.person_id, nr.id region_id, nr.region_name, e.event_name, me.medal_name
    FROM medal me
    JOIN competitor_event ce ON me.id = ce.medal_id
    JOIN games_competitor gc ON ce.competitor_id = gc.id
    JOIN person_region pr ON gc.person_id = pr.person_id
    JOIN noc_region nr ON pr.region_id = nr.id
    JOIN event e ON ce.event_id = e.id
    WHERE me.medal_name != 'NA'
),

person_event_counts AS (
    SELECT person_id, event_name, region_name, COUNT(medal_name) total_medals
    FROM event_medal_winners_by_region
    GROUP BY person_id, event_name, region_name
),

best_events AS (
    SELECT pec.person_id, pec.event_name, pec.region_name, pec.total_medals
    FROM person_event_counts pec
    JOIN (
        SELECT person_id, MAX(total_medals) max_medals
        FROM person_event_counts
        GROUP BY person_id
    ) m ON pec.person_id = m.person_id AND pec.total_medals = m.max_medals
),

best_per_person_region AS (
    SELECT person_id, region_name, MAX(total_medals) best_count
    FROM best_events
    GROUP BY person_id, region_name
)

SELECT region_name, SUM(best_count) total_region_medals
FROM best_per_person_region
GROUP BY region_name
ORDER BY total_region_medals DESC
LIMIT 5;


-- Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals. Retrieve and display the contents of this table, including their full names and the number of games they participated in.
CREATE TEMP TABLE four_plus_games_no_medal AS 
    WITH medal_winners AS (
        SELECT gc.person_id
        FROM medal me
        JOIN competitor_event ce ON me.id = ce.medal_id
        JOIN games_competitor gc ON ce.competitor_id = gc.id
        WHERE me.medal_name != 'NA'
    )

    SELECT p.id, p.full_name, COUNT(DISTINCT gc.games_id) games_competed
    FROM games_competitor gc
    JOIN person p ON gc.person_id = p.id
    WHERE p.id NOT IN (
        SELECT person_id
        FROM medal_winners
        )
    GROUP BY p.id
    HAVING COUNT(DISTINCT gc.games_id) > 3;

SELECT * FROM four_plus_games_no_medal;