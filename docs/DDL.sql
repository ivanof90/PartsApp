CREATE TABLE supplier (
    sid SERIAL PRIMARY KEY,        -- Supplier ID (auto-incremented)
    sname VARCHAR(255) NOT NULL,   -- Supplier name
    scity VARCHAR(100),            -- Supplier city
    sphone VARCHAR(20)             -- Supplier phone number
);

CREATE TABLE parts (
    pid SERIAL PRIMARY KEY,        -- Part ID (auto-incremented)
    pname VARCHAR(255) NOT NULL,   -- Part name
    pmaterial VARCHAR(100),        -- Material of the part
    pcolor VARCHAR(50),            -- Color of the part
    pprice NUMERIC(10, 2)          -- Price of the part
);

CREATE TABLE supplies (
    sid INT REFERENCES supplier(sid) ON DELETE CASCADE,  -- Foreign key to supplier
    pid INT REFERENCES parts(pid) ON DELETE CASCADE,     -- Foreign key to parts
    qty INT DEFAULT 0,                                   -- Quantity supplied
    PRIMARY KEY (sid, pid)                               -- Composite primary key
);