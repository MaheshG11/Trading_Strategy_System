CREATE DATABASE IF NOT EXISTS StocksData;
USE StocksData;
CREATE TABLE IF NOT EXISTS  Stocks(
	id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) unique,
    stock_name varchar(100)
);
CREATE TABLE IF NOT EXISTS  StockPrice(
	id INT PRIMARY KEY AUTO_INCREMENT,
	stocks_id INT,
	FOREIGN KEY (stocks_id) REFERENCES Stocks(id),
    date VARCHAR(30),
    UNIQUE (id,date),
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume DOUBLE
);

