CREATE TABLE athletes(
    id SERIAL,
    name text,
    sex text,
    age integer,
    height integer,
    weight integer,
    sport text
);
    
CREATE TABLE olympic_games(
    id SERIAL,
    game text,
    year integer,
    season text,
    city text
);

CREATE TABLE events(
    id SERIAL,
    name text
);

CREATE TABLE teams(
    id SERIAL,
    team text,
    noc text
);

CREATE TABLE medals(
    id SERIAL,
    medal text,
    game text,
    owner text,
    team text,
    event text
);