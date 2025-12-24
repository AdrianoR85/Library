CREATE TABLE process.reservation (
    id_reservation     SERIAL PRIMARY KEY,
    id_book            INTEGER NOT NULL,
    id_user            INTEGER NOT NULL,
    reservation_date   TIMESTAMP,
    available          BOOLEAN,
    expiration_date    TIMESTAMP,
    priority_position  INTEGER,
    status             VARCHAR(20),
    CONSTRAINT fk_res_book
        FOREIGN KEY (id_book)
        REFERENCES book.book(id_book),
    CONSTRAINT fk_res_user
        FOREIGN KEY (id_user)
        REFERENCES customer.user(id_user)
);

CREATE TABLE process.loan (
    id_loan           SERIAL PRIMARY KEY,
    id_user           INTEGER NOT NULL,
    id_copy           INTEGER NOT NULL,
    loan_date         TIMESTAMP,
    expected_return_date TIMESTAMP,
    actual_return_date   TIMESTAMP,
    id_employee       INTEGER,
    status            VARCHAR(20),
    CONSTRAINT fk_loan_user
        FOREIGN KEY (id_user)
        REFERENCES customer.user(id_user),
    CONSTRAINT fk_loan_copy
        FOREIGN KEY (id_copy)
        REFERENCES book.book_copy(id_copy),
    CONSTRAINT fk_loan_employee
        FOREIGN KEY (id_employee)
        REFERENCES staff.employee(id_employee)
);

CREATE TABLE process.fines (
    id_fines       SERIAL PRIMARY KEY,
    id_loan        INTEGER NOT NULL,
    id_user        INTEGER NOT NULL,
    amount         NUMERIC(10,2),
    days_overdue   INTEGER,
    CONSTRAINT fk_fines_loan
        FOREIGN KEY (id_loan)
        REFERENCES process.loan(id_loan),
    CONSTRAINT fk_fines_user
        FOREIGN KEY (id_user)
        REFERENCES customer.user(id_user)
);

