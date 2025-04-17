CREATE TABLE funds (
    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,       -- Unique identifier for the fund
    fund_name TEXT NOT NULL,                        -- Name of the fund
    fund_manager_id INTEGER NOT NULL,               -- Foreign key referencing the manager
    fund_description TEXT NOT NULL,                 -- Description of the fund
    nav REAL NOT NULL,                             -- Net Asset Value (NAV) of the fund
    date_of_creation DATE NOT NULL,                -- Date when the fund was created
    performance REAL NOT NULL,                     -- Performance of the fund as a percentage
    FOREIGN KEY (fund_manager_id) REFERENCES managers(manager_id)
        ON DELETE CASCADE                          -- If a manager is deleted, their funds are also deleted
        ON UPDATE CASCADE                          -- If a manager's ID changes, update references
);