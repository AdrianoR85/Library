CREATE TABLE authentication.auth (
    id_auth     SERIAL PRIMARY KEY,
    email       VARCHAR(50) UNIQUE NOT NULL,
    password    VARCHAR(20) NOT NULL,
    created_at  TIMESTAMP
);