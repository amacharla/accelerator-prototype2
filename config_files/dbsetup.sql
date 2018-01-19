-- create user credentials for flask and database
CREATE USER IF NOT EXISTS 'flask'@'%' IDENTIFIED BY 'f1ask';
CREATE DATABASE IF NOT EXISTS app_db;
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON app_db.* TO 'flask'@'%';
FLUSH PRIVILEGES;
