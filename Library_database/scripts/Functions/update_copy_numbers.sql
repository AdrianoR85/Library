CREATE OR REPLACE FUNCTION process.fn_update_copy_numbers(p_id_copy integer)
RETURNS TRIGGER 
LANGUAGE plpgsql AS
$$
DECLARE
    v_id_book INTEGER;
BEGIN
    IF TG_TABLE_NAME = 'loan' THEN
      v_id_book := COALESCE(NEW.id_book, OLD.id_book);
    ELSIF TG_TABLE_NAME = 'reservation' THEN
      v_id_book := COALESCE(NEW.id_book, OLD.id_book);
    ELSE
      RAISE EXCEPTION 'Trigger called from unsupported table: %', TG_TABLE_NAME;
    END IF;

    UPDATE book.book
    SET total_quantity = (
      SELECT COALESCE(COUNT(*), 0)
      FROM book.book_copy
      WHERE id_book = v_id_book AND status = 'available'
    )