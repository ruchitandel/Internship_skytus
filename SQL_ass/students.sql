-- Create students table
CREATE TABLE students(
id INT PRIMARY KEY,
name VARCHAR(50) NOT NULL,
department VARCHAR(30) NOT NULL,
year INT,
marks INT
);

INSERT INTO students VALUES
(1,'Ruchi','CSE',1,95),
(2,'Kripa','IT',2,99),
(3,'Nish','ICT',3,98),
(4,'Prachi','CSD',4,96);

--Display all student records
SELECT * FROM students;

--Display only name and department
SELECT name, department FROM students;

--Find students with marks greater than 75
SELECT * FROM students WHERE marks>75;

--Display students from CSE department
SELECT * FROM students WHERE department='CSE';

--Sort students by marks (descending)
SELECT * FROM students ORDER BY marks DESC;

--Display top 3 scorers
SELECT * FROM students ORDER BY marks DESC LIMIT 3;
