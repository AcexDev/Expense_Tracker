CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255),
    security_question VARCHAR(255),
    security_answer_hash VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS categories(
category_id INT PRIMARY KEY AUTO_INCREMENT,
name VARCHAR (255),
user_id INT,
FOREIGN KEY(user_id) REFERENCES users(user_id),
UNIQUE(user_id, name)
);

CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2),
    description VARCHAR(255),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
