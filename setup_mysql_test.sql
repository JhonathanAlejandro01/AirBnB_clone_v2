-- the create databese
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- CREATE USER
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- THE ALL PRIVILEGES TO USER
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

