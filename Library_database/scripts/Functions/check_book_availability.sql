CREATE OR REPLACE FUNCTION process.check_book_availability(p_book_id INTEGER)
RETURN BOOLEAN
LANGUAGE plpgsql
AS $$
DECLARE
BEGIN

END;
$$;

-- Get total number of copies
SELECT COALESCE(SUM(copy_number),0)
FROM book.book_copy
WHERE id_book = 1
AND status = 'available';

-- Get number of active loans
SELECT COALESCE(COUNT(*), 0)
FROM process.loan
WHERE id_book = 1
AND actual_return_date IS NULL;