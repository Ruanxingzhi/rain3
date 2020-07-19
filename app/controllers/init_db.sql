DROP TABLE IF EXISTS target;

CREATE TABLE target (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    host TEXT NOT NULL,
    port INTEGER NOT NULL,
    difficulty INTEGER DEFAULT 0,
    enabled INTEGER DEFAULT TRUE
);