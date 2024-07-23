CREATE DATABASE bot_database;

USE bot_database;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pseudo VARCHAR(255) NOT NULL,
    points INT DEFAULT 0
);

CREATE TABLE challenges (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    solved_by VARCHAR(255),
    FOREIGN KEY (solved_by) REFERENCES users(pseudo)
);
