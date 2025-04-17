CREATE TABLE investments (
    investment_id INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for the investment
    investor_id INTEGER NOT NULL,                   -- Foreign key referencing the investor
    fund_id INTEGER NOT NULL,                      -- Foreign key referencing the fund
    investment_amount REAL NOT NULL,               -- Amount invested by the investor
    investment_date DATE NOT NULL,                 -- Date when the investment was made
    FOREIGN KEY (investor_id) REFERENCES investors(investor_id)
        ON DELETE CASCADE                          -- If an investor is deleted, their investments are also deleted
        ON UPDATE CASCADE,                         -- If an investor's ID changes, update references
    FOREIGN KEY (fund_id) REFERENCES funds(fund_id)
        ON DELETE CASCADE                          -- If a fund is deleted, related investments are also deleted
        ON UPDATE CASCADE                          -- If a fund's ID changes, update references
);