CREATE TABLE olympic_games(
    id SERIAL,
    year integer,
    season text,
    city text
);
CREATE TABLE

CREATE TABLE events(
    id SERIAL,
    name text
);

CREATE TABLE events_olympic_games(
    event_id integer,
    olympic_games_id integer
);
