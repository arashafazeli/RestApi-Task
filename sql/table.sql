CREATE TABLE IF NOT EXISTS beers (
    id INT PRIMARY KEY,
    beer_id INT,
    name VARCHAR(20) NOT NULL,
    price FLOAT(10) NOT NULL,
    alcohol_percentage FLOAT(5)
);