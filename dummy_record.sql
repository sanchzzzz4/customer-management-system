-- Insert into Customers
INSERT INTO Customers (name, email, phone, age, location) 
VALUES 
('Alice Johnson', 'alice.johnson@example.com', '1234567890', 28, 'New York'),
('Bob Smith', 'bob.smith@example.com', '9876543210', 35, 'Los Angeles'),
('Charlie Brown', 'charlie.brown@example.com', '1122334455', 40, 'Chicago');

-- Insert into Products
INSERT INTO Products (name, description, price, stock) 
VALUES 
('Laptop', 'High-performance laptop with 16GB RAM', 1200.00, 10),
('Smartphone', 'Latest model with 5G support', 800.00, 20),
('Headphones', 'Noise-cancelling over-ear headphones', 150.00, 30);

-- Insert into Purchases
INSERT INTO Purchases (customer_id, product_id, quantity, total_price) 
VALUES 
(1, 1, 1, 1200.00),
(2, 2, 2, 1600.00),
(3, 3, 3, 450.00);

-- Insert into Feedback
INSERT INTO Feedback (customer_id, feedback_text, rating) 
VALUES 
(1, 'Great service and excellent products!', 5),
(2, 'Satisfied with the purchase, but delivery was late.', 4),
(3, 'Product quality could be improved.', 3);

-- Insert into ChurnPredictions
INSERT INTO ChurnPredictions (customer_id, churn_probability) 
VALUES 
(1, 0.10),
(2, 0.70),
(3, 0.95);
