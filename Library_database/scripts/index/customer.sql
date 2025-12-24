
CREATE INDEX idx_user_cpf ON customer.user USING btree (cpf);
CREATE INDEX idx_user_last_name ON customer.user USING btree (first_name, last_name);