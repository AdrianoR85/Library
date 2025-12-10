CREATE TABLE book.publisher (
    id_publisher     SERIAL PRIMARY KEY,
    name             VARCHAR(100) NOT NULL,
    country          VARCHAR(30),
    city             VARCHAR(45),
    phone            VARCHAR(50),
    email            VARCHAR(50)
);

CREATE TABLE book.author (
    id_author    SERIAL PRIMARY KEY,
    first_name   VARCHAR(50) NOT NULL,
    middle_name  VARCHAR(50),
    last_name    VARCHAR(50) NOT NULL,
    biography    TEXT
);

CREATE TABLE book.book (
    id_book           SERIAL PRIMARY KEY,
    title             VARCHAR(100) NOT NULL,
    isbn              CHAR(13),
    publication_year  INTEGER,
    number_of_pages   INTEGER,
    id_publisher      INTEGER,
    language          VARCHAR(30),
    total_quantity    INTEGER,
    available_quantity INTEGER,
    CONSTRAINT fk_book_publisher
        FOREIGN KEY (id_publisher)
        REFERENCES book.publisher(id_publisher)
);


CREATE TABLE book.book_author (
    id_book_author  SERIAL PRIMARY KEY,
    id_book         INTEGER NOT NULL,
    id_author       INTEGER NOT NULL,
    CONSTRAINT fk_ba_book
        FOREIGN KEY (id_book)
        REFERENCES book.book(id_book),
    CONSTRAINT fk_ba_author
        FOREIGN KEY (id_author)
        REFERENCES book.author(id_author)
);


CREATE TABLE book.book_category (
    id_book_category SERIAL PRIMARY KEY,
    id_category      INTEGER NOT NULL,
    id_book          INTEGER NOT NULL,
    CONSTRAINT fk_bc_category
        FOREIGN KEY (id_category)
        REFERENCES book.category(id_category),
    CONSTRAINT fk_bc_book
        FOREIGN KEY (id_book)
        REFERENCES book.book(id_book)
);

CREATE TABLE book.section (
    id_section   SERIAL PRIMARY KEY,
    name         VARCHAR(50) NOT NULL,
    floor        SMALLINT,
    description  TEXT
);

CREATE TABLE book.shelf (
    id_shelf       SERIAL PRIMARY KEY,
    id_section     INTEGER NOT NULL,
    shelf_code     VARCHAR(50),
    capacity       INTEGER,
    description    TEXT,
    CONSTRAINT fk_shelf_section
        FOREIGN KEY (id_section)
        REFERENCES book.section(id_section)
);

CREATE TABLE book.book_copy (
    id_copy        SERIAL PRIMARY KEY,
    id_book        INTEGER NOT NULL,
    id_shelf       INTEGER,
    copy_number    INTEGER,
    barcode        VARCHAR(20),
    acquisition_date DATE,
    condition      VARCHAR(20),
    status         VARCHAR(20),
    CONSTRAINT fk_copy_book
        FOREIGN KEY (id_book)
        REFERENCES book.book(id_book),
    CONSTRAINT fk_copy_shelf
        FOREIGN KEY (id_shelf)
        REFERENCES book.shelf(id_shelf)
);

CREATE TABLE book.book_copy (
    id_copy        SERIAL PRIMARY KEY,
    id_book        INTEGER NOT NULL,
    id_shelf       INTEGER,
    copy_number    INTEGER,
    barcode        VARCHAR(20),
    acquisition_date DATE,
    condition      VARCHAR(20),
    status         VARCHAR(20),
    CONSTRAINT fk_copy_book
        FOREIGN KEY (id_book)
        REFERENCES book.book(id_book),
    CONSTRAINT fk_copy_shelf
        FOREIGN KEY (id_shelf)
        REFERENCES book.shelf(id_shelf)
);
