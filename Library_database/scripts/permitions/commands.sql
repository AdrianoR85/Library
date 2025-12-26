/* Criar um usuário */
CREATE USER sara WITH PASSWORD 'sara123'; 

/* Ou criar usuário com mais poder */
CREATE USER sara WITH PASSWORD 'sara123' SUPERUSER;

/* Ou dara permissões de criar databases e usuários */
CREATE USER sara WITH PASSWORD 'sara123' CREATEDB CREATEROLE;

/* Dar permissão para conectar o banco de dados */
GRANT CONNECT ON DATABASE library_db TO sara;

/* Dar permissão para os schemas */
GRANT USAGE ON SCHEMA book TO sara;
GRANT USAGE ON SCHEMA customer TO sara;
GRANT USAGE ON SCHEMA process TO sara;
GRANT USAGE ON SCHEMA staff TO sara;

/*Dar permissão para os comandos DQL, DML, DDL */
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA book TO sara;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA customer TO sara;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA process TO sara;
GRANT SELECT ON ALL TABLES IN SCHEMA staff TO sara;

/* Permiti que se use sequences */
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA book TO sara;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA customer TO sara;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA process TO sara;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA staff TO sara;

