
-- Loan
CREATE INDEX idx_loan_user ON process.loan USING btree (id_user);
CREATE INDEX idx_loan_book ON process.loan USING btree (id_copy);
CREATE INDEX idx_loan_loan_date ON process.loan USING btree (loan_date, expected_return_date);
CREATE INDEX idx_loan_status ON process.loan USING btree (status);

-- Reservation
CREATE INDEX idx_reservation_user ON process.reservation USING btree (id_user);
CREATE INDEX idx_reservation_book ON process.reservation USING btree (id_book);
CREATE INDEX idx_reservation_status ON process.reservation USING btree (status);