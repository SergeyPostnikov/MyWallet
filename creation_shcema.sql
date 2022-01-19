CREATE DATABASE IF NOT EXISTS my_wallet;

USE my_wallet;

CREATE TABLE IF NOT EXISTS user(
	id INT PRIMARY KEY AUTO_INCREMENT,
	firstname VARCHAR(20) NOT NULL,
	lastname  VARCHAR(30) NOT NULL,
	email VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS transaction(
	id INT PRIMARY KEY AUTO_INCREMENT,
	user_id INT,
	description VARCHAR(40),
	amount DECIMAL(10, 2),
	created_at DATETIME DEFAULT NOW() ON UPDATE NOW(),
	FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
);


-- SELECT SUM(amount), DATE(created_at)  
-- FROM transaction
-- WHERE user_id = 2 
-- GROUP BY DATE(created_at);

-- Ability to view sum of income/outcome grouped by dates 
-- (say, an array of {“date”: “2021-05-11”, “sum”: 2543.50} jsons,
-- so that as a user I know how much I’ve spent/received each day).
--  Will be a plus if you also add start date and end date filter to it.


