-- creates a table second_table in the database hbtn_0c_0 in MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Gege', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Max', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'kadi', 8);
