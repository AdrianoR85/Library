CREATE TABLE authentication.auth (
    id_auth     SERIAL PRIMARY KEY,
    email       VARCHAR(50) UNIQUE NOT NULL,
    password    VARCHAR(256) NOT NULL,
    created_at  TIMESTAMP
);
