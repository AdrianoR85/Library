CREATE OR REPLACE FUNCTION process.check_book_availability(p_book_id INTEGER)
RETURNS BOOLEAN 
LANGUAGE plpgsql AS
$$
DECLARE
	v_available_quantity INTEGER;
BEGIN
	
	SELECT available_quantity
	INTO v_available_quantity
	FROM book.book
	WHERE id_book = p_book_id;

	return v_available_quantity > 0;
	
END;
$$;

COMMENT ON FUNCTION process.check_book_availability IS
'Checks if a book has available copies for reservation or loan';


