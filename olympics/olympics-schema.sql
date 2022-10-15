CREATE TABLE athletes(
    id SERIAL,
    name text,
    sex text
);
    
CREATE TABLE games(
    id SERIAL,
    city text,
    year integer,
    season text
);

CREATE TABLE events(
    id SERIAL,
    name text
);

CREATE TABLE teams(
    id SERIAL,
    country text,
    abbrev text
);

CREATE TABLE sports(
    id SERIAL,
    name text
);

CREATE TABLE event_results (
    athlete_id INTEGER,
    athlete_age INTEGER,
    athlete_height INTEGER,
    athlete_weight INTEGER,
    games_id INTEGER,
    teams_id INTEGER,
    events_id INTEGER,
    sports_id INTEGER,
    medal TEXT
);

CREATE TABLE medal_count (
    abbrev text,
    gold integer,
    silver integer,
    bronze integer
);
