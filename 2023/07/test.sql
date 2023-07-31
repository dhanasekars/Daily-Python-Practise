BEGIN;
CREATE TABLE IF NOT EXISTS members (
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    email TEXT
);

-- Insert five records into the table
INSERT INTO members VALUES ('John', 'Doe', 30, 'john.doe@example.com');
INSERT INTO members VALUES ('Jane', 'Smith', 25, 'jane.smith@example.com');
INSERT INTO members VALUES ('Michael', 'Johnson', 40, 'michael.johnson@example.com');
INSERT INTO members VALUES ('Emily', 'Williams', 28, 'emily.williams@example.com');
INSERT INTO members VALUES ('David', 'Brown', 35, 'david.brown@example.com');
COMMIT;
