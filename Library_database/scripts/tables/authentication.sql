CREATE TABLE authentication.auth (
    id_auth     SERIAL PRIMARY KEY,
    username    VARCHAR(20) NOT NULL UNIQUE,
    password    TEXT NOT NULL,
    role        VARCHAR(10) NOT NULL CHECK(role IN ('admin', 'customer')),
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMP
);