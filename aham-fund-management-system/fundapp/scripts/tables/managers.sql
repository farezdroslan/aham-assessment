CREATE TABLE managers (
    manager_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for the manager
    manager_name TEXT NOT NULL,                  -- Name of the manager
    manager_bio TEXT                            -- Biography or description of the manager
);