-- BOOK 
CREATE INDEX idx_book_title ON book.book USING btree (title);
CREATE INDEX idx_book_isbn ON book.book USING btree (isbn);
CREATE INDEX idx_book_publication_year ON book.book USING btree (publication_year);

--BOOK_AUTHOR
CREATE INDEX idx_book_author_id_book ON book.book_author USING btree (id_book);
CREATE INDEX idx_book_author_id_author ON book_author USING btree (id_author);

--BOOK_CATEGORY
CREATE INDEX idx_book_category_id_category ON book.book_category USING btree (id_category);
CREATE INDEX idx_book_category_id_book ON book.book_category USING btree (id_book);

--Book_Copy
CREATE INDEX idx_book_copy_id_book ON book_copy USING btree (id_book);
CREATE INDEX idx_book_copy_status ON book_copy USING btree (status);
CREATE INDEX idx_book_copy_id_shelf ON book_copy USING btree (id_shelf);
