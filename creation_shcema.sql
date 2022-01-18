CREATE DATABASE IF NOT EXISTS my_wallet;

USE my_wallet;

CREATE TABLE IF NOT EXISTS user(
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(20),
	lastname  VARCHAR(30),
	email VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS transaction(
	id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT,
	description VARCHAR(40),
	amount DECIMAL(10, 2),
	tr_type VARCHAR(7) DEFAULT 'outcome',
	created_at DATETIME DEFAULT NOW() ON UPDATE NOW(),
	FOREIGN KEY (user_id) REFERENCES user(id)
);

