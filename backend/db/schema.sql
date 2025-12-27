CREATE TABLE maintenance_team (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE equipment (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    serial_number TEXT UNIQUE,
    status TEXT,
    team_id INTEGER,
    FOREIGN KEY(team_id) REFERENCES maintenance_team(id)
);
