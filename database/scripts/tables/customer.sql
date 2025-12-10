CREATE TABLE customer.address (
    id_address     SERIAL PRIMARY KEY,
    street         VARCHAR(30),
    number         INTEGER,
    neighborhood   VARCHAR(30),
    city           VARCHAR(30),
    state          CHAR(2)
);

CREATE TABLE customer.user (
    id_user           SERIAL PRIMARY KEY,
    first_name        VARCHAR(50) NOT NULL,
    middle_name       VARCHAR(50),
    last_name         VARCHAR(50) NOT NULL,
    phone             VARCHAR(20),
    registration_date TIMESTAMP,
    id_address        INTEGER,
    id_auth           INTEGER,
    CONSTRAINT fk_user_address
        FOREIGN KEY (id_address)
        REFERENCES customer.address(id_address),
    CONSTRAINT fk_user_auth
        FOREIGN KEY (id_auth)
        REFERENCES authentication.auth(id_auth)
);
