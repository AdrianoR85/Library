CREATE INDEX idx_employee_email ON staff.employee USING btree (email);
CREATE INDEX idx_employee_status ON staff.employee USING btree (status);
CREATE INDEX idx_employee_name ON staff.employee USING btree (first_name, last_name);