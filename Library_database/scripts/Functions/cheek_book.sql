CREATE OR REPLACE FUNCTION process.fn_reserve_book_copy(p_id_book INTEGER)
RETURNS INT AS $$
DECLARE
    v_id_copy INT;
BEGIN
    SELECT id_copy
    INTO v_id_copy
    FROM book.book_copy
    WHERE id = p_id_book AND status = 'available'
    LIMIT 1
    FOR UPDATE SKIP LOCKED;

    IF v_id_copy IS NULL THEN
        RAISE EXCEPTION 'No available copies for the requested book.';
    END IF;
    
    fn_update_copy_numbers(v_id_copy);
END;
$$ LANGUAGE plpgsql;


SELECT fn_reserve_book_copy(1);