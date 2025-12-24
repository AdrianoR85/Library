CREATE TABLE staff.employee (
    id_employee   SERIAL PRIMARY KEY,
    first_name    VARCHAR(50),
    middle_name   VARCHAR(50),
    last_name     VARCHAR(50),
    email         VARCHAR(50) UNIQUE,
    position      VARCHAR(20),
    hire_date     DATE,
    phone         VARCHAR(20),
    status        VARCHAR(20)
);
