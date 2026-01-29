CREATE SCHEMA book;
CREATE SCHEMA process;
CREATE SCHEMA authentication;
CREATE SCHEMA customer;
CREATE SCHEMA staff;


-- BOOK SCHEMA
-- Category table
CREATE TABLE book.category (
    id_category INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

-- Publisher table
CREATE TABLE book.publisher (
    id_publisher INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(30),
    city VARCHAR(15),
    phone VARCHAR(15),
    email VARCHAR(50)
);

-- Author table
CREATE TABLE book.author (
    id_author INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    nationality VARCHAR(30),
    biography TEXT
);

-- Book table
CREATE TABLE book.book (
    id_book INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    isbn CHAR(13),
    publication_year SMALLINT,
    edition SMALLINT,
    number_of_pages INTEGER,
    id_publisher INTEGER,
    language VARCHAR(30),
    available_quantity INTEGER,
    FOREIGN KEY (id_publisher) REFERENCES book.publisher(id_publisher)
);

-- Book_Category junction table
CREATE TABLE book.book_Category (
    id_book_category INTEGER PRIMARY KEY,
    id_category INTEGER NOT NULL,
    id_book INTEGER NOT NULL,
    FOREIGN KEY (id_category) REFERENCES book.category(id_category),
    FOREIGN KEY (id_book) REFERENCES book.book(id_book)
);

-- Book_Author junction table
CREATE TABLE book.book_Author (
    id_book INTEGER NOT NULL,
    id_author INTEGER NOT NULL,
    PRIMARY KEY (id_book, id_author),
    FOREIGN KEY (id_book) REFERENCES book.book(id_book),
    FOREIGN KEY (id_author) REFERENCES book.author(id_author)
);

-- Section table
CREATE TABLE book.section (
    id_section INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    floor SMALLINT,
    description TEXT
);

-- Shelf table
CREATE TABLE book.shelf (
    id_shelf INTEGER PRIMARY KEY,
    id_section INTEGER NOT NULL,
    shelf_code TEXT,
    capacity INTEGER,
    description TEXT,
    FOREIGN KEY (id_section) REFERENCES book.section(id_section)
);

-- Book_Copy table
CREATE TABLE book.book_copy (
    id_copy INTEGER PRIMARY KEY,
    id_book INTEGER NOT NULL,
    id_shelf INTEGER NOT NULL,
    copy_number INTEGER,
    barcode TEXT,
    acquisition_date DATE,
    condition VARCHAR(20),
    status VARCHAR(20),
    FOREIGN KEY (id_book) REFERENCES book.book(id_book),
    FOREIGN KEY (id_shelf) REFERENCES book.shelf(id_shelf)
);

-- PROCESS SCHEMA
-- Fines table
CREATE TABLE process.fines (
    id_fines INTEGER PRIMARY KEY,
    id_loan INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    fine_amount DECIMAL(10,2),
    days_overdue INTEGER
);

-- Reservation table
CREATE TABLE process.reservation (
    id_reservation INTEGER PRIMARY KEY,
    id_book INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    reservation_date TIMESTAMP NOT NULL,
    available BOOLEAN,
    expiration_date TIMESTAMP,
    status VARCHAR(20),
    FOREIGN KEY (id_book) REFERENCES book.book(id_book)
);

-- Loan table
CREATE TABLE process.loan (
    id_loan INTEGER PRIMARY KEY,
    id_user INTEGER NOT NULL,
    id_copy INTEGER NOT NULL,
    loan_date TIMESTAMP NOT NULL,
    expected_return_date TIMESTAMP NOT NULL,
    actual_return_date TIMESTAMP,
    id_employee VARCHAR(20),
    status VARCHAR(20)
);

-- USER SCHEMA
-- Address table
CREATE TABLE customer.address (
    id_address INTEGER PRIMARY KEY,
    street VARCHAR(30),
    number INTEGER,
    neighborhood VARCHAR(30),
    city CHAR(2),
    state CHAR(2)
);

-- AUTHENTICATION SCHEMA
-- Auth table
CREATE TABLE authentication.auth (
    id_auth     SERIAL PRIMARY KEY,
    username    VARCHAR(20) NOT NULL UNIQUE,
    password    TEXT NOT NULL,
    role        VARCHAR(10) NOT NULL CHECK(role IN ('admin', 'customer')),
    is_active   BOOLEAN DEFAULT TRUE,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- User table
CREATE TABLE customer.user (
    id_user INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    cpf CHAR(9),
    phone VARCHAR(20),
    status VARCHAR(20),
    registration_date DATE,
    id_address INTEGER,
    id_auth INTEGER,
    FOREIGN KEY (id_address) REFERENCES customer.address(id_address),
    FOREIGN KEY (id_auth) REFERENCES authentication.auth(id_auth)
);

-- EMPLOYEE SCHEMA
-- Employee table
CREATE TABLE staff.employee (
    id_employee INTEGER PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    cpf CHAR(9),
    ssn VARCHAR(20),
    position VARCHAR(30),
    hire_date DATE,
    fire_date DATE,
    phone VARCHAR(20),
    status VARCHAR(20)
);

-- Add foreign keys that reference tables created later
ALTER TABLE process.fines 
    ADD FOREIGN KEY (id_loan) REFERENCES process.loan(id_loan),
    ADD FOREIGN KEY (id_user) REFERENCES customer.user(id_user);

ALTER TABLE process.reservation 
    ADD FOREIGN KEY (id_user) REFERENCES customer.user(id_user);

ALTER TABLE process.loan 
    ADD FOREIGN KEY (id_user) REFERENCES customer.user(id_user),
    ADD FOREIGN KEY (id_copy) REFERENCES book.book_copy(id_copy);