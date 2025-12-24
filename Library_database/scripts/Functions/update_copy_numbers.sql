CREATE OR REPLACE FUNCTION process.fn_update_copy_numbers(p_id_copy integer)
RETURNS integer
LANGUAGE plpgsql AS 
$body$
DECLARE
  v_total_copy INTEGER;
BEGIN
  SELECT copy_number INTO v_total_copy
  FROM book.book_copy
  WHERE id_copy = p_id_copy;

  IF v_total_copy > 1 THEN
    UPDATE book.book_copy
    SET copy_number = copy_number - 1
    WHERE id_copy = p_id_copy;
  ELSE
    UPDATE book.book_copy
    SET status = 'loaned', copy_number = 0
    WHERE id_copy = p_id_copy;
  END IF;
END;
$body$; 
