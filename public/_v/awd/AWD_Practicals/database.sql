-- Run this once in phpMyAdmin (Import / SQL tab) before the database practicals
CREATE DATABASE IF NOT EXISTS awd_practical;
USE awd_practical;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    balance DECIMAL(10,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO users (name, email) VALUES ('Ravi', 'ravi@example.com'), ('Neha', 'neha@example.com');
INSERT INTO accounts (name, balance) VALUES ('Account A', 1000), ('Account B', 500);
INSERT INTO products (name, price) VALUES ('Pen', 10), ('Notebook', 50);
