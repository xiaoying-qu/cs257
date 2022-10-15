--List all the NOCs (National Olympic Committees), in alphabetical order by abbreviation. These entities, by the way, are mostly equivalent to countries. But in some cases, you might find that a portion of a country participated in a particular games (e.g. one guy from Newfoundland in 1904) or some other oddball situation.

SELECT 
    DISTINCT abbrev
FROM 
    teams
ORDER BY 
    abbrev ASC;


--List the names of all the athletes from Jamaica. If your database design allows it, sort the athletes by last name.
SELECT 
    athletes.name, teams.abbrev, event_results.athlete_id, event_results.teams_id
FROM
    athletes,teams, event_results
WHERE teams.abbrev LIKE 'JAM%' AND event_results.athlete_id = athletes.id AND event_results.teams_id = teams.id
ORDER BY 
    athletes.name ASC;


--List all the medals won by Greg Louganis, sorted by year. Include whatever fields in this output that you think appropriate.


SELECT 
    athletes.name, games.year, event_results.games_id, event_results.athlete_id, event_results.medal
FROM athletes,games, event_results

WHERE athletes.name = 'Gregory Efthimios "Greg" Louganis'
AND athletes.id = event_results.athlete_id
AND event_results.medal LIKE 'Gold%' OR event_results.medal LIKE 'Silver%'
OR event_results.medal LIKE 'Bronze%'

ORDER BY games.year;


--List all the NOCs and the number of gold medals they have won, in decreasing order of the number of gold medals.


SELECT medal_count.noc_id, medal_count.gold
FROM medal_count
ORDER BY medal_count.gold;