CREATE TABLE investors (
    investor_id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for the investor
    investor_name TEXT NOT NULL,                   -- Name of the investor
    investor_email TEXT UNIQUE NOT NULL           -- Email address of the investor (unique)
);