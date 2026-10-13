-- 🌟 Exercise 1: Advanced Medal Analysis
-- Identify competitors who have won medals in both individual and team events, and calculate the total number of medals they have won in each category. Create a temporary table to store the results and ensure it includes their full name, total medals in individual events, and total medals in team events.
DROP TABLE IF EXISTS medals_won_categories;

CREATE TEMP TABLE medals_won_categories AS
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
    ),

    medals_won_per_event_type AS (
        SELECT person_id,
            COUNT(*) FILTER (WHERE event_type = 'team') team_event_medal_count,
            COUNT(*) FILTER (WHERE event_type = 'individual') individual_event_medal_count
        FROM labeled
        GROUP BY person_id
    )

    SELECT mwpet.person_id, p.full_name, mwpet.team_event_medal_count, mwpet.individual_event_medal_count
    FROM medals_won_per_event_type mwpet
    JOIN person p
    ON mwpet.person_id = p.id
    WHERE mwpet.team_event_medal_count > 0 AND mwpet.individual_event_medal_count > 0;

SELECT *
FROM medals_won_categories
ORDER BY person_id;

-- 🌟 Exercise 2: Complex Event Participation
-- Create a temporary table to store the competitors who have won medals in exactly 3 different sports. Then, using this temporary table, identify the top 3 competitors with the highest total number of medals across all sports. Use nested subqueries and aggregation.
DROP TABLE IF EXISTS three_different_sport_medal_winners;

CREATE TEMP TABLE three_different_sport_medal_winners AS
    WITH medal_winners AS (
        SELECT g_competitor.person_id, e.sport_id, c_event.medal_id, e.event_name
        FROM games_competitor g_competitor
        JOIN competitor_event c_event ON c_event.competitor_id = g_competitor.id
        JOIN event e ON c_event.event_id = e.id
        WHERE c_event.medal_id != 4
    )

    SELECT person_id, COUNT(DISTINCT sport_id) sports_count, COUNT(*) total_medals
    FROM medal_winners
    GROUP BY person_id
    HAVING COUNT(DISTINCT sport_id) = 3;

SELECT p.id, p.full_name, tdsmw.sports_count, tdsmw.total_medals
FROM three_different_sport_medal_winners tdsmw
JOIN person p ON tdsmw.person_id = p.id
WHERE tdsmw.total_medals IN (
    SELECT total_medals
    FROM (
        SELECT DISTINCT total_medals
        FROM three_different_sport_medal_winners
        ORDER BY total_medals DESC
        LIMIT 3
    ) top_counts
)
ORDER BY tdsmw.total_medals DESC;