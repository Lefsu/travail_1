-- DATABASE FOR MANAGING SECURITY AUDITS
-- LEFEVRE Sullivan - MOREAU Guy-Loup
--Employees (id(PK), last name, first name, position, department_id(FK))
--Systems (id(PK), name, type, department_id(FK), manager_id(FK))
--Security Audits (id(PK), date, status, employee_id(FK), system_id(FK))
--Vulnerabilities detected (id(PK), audit_id(FK), system_id(FK), severity, status)
--Department (id(PK), manager_id(FK), type, status, location)
-- CREATION OF THE DB
-- EMPLOYEES TABLE
CREATE TABLE Employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    position VARCHAR(255),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(id)
);
-- SYSTEMS TABLE
CREATE TABLE Systems (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(255),
    department_id INT,
    manager_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(id),
    FOREIGN KEY (manager_id) REFERENCES Employees(id)
);
--SECURITY AUDITS TABLE
CREATE TABLE SecurityAudits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    date DATE NOT NULL,
    status VARCHAR(255),
    employee_id INT,
    system_id INT,
    FOREIGN KEY (employee_id) REFERENCES Employees(id),
    FOREIGN KEY (system_id) REFERENCES Systems(id)
);
-- VULNERABILITIES DETECTED
CREATE TABLE VulnerabilitiesDetected (
    id INT PRIMARY KEY AUTO_INCREMENT,
    audit_id INT,
    system_id INT,
    severity VARCHAR(255),
    status VARCHAR(255),
    FOREIGN KEY (audit_id) REFERENCES SecurityAudits(id),
    FOREIGN KEY (system_id) REFERENCES Systems(id)
);
-- DEPARTMENT TABLE
CREATE TABLE Department (
    id INT PRIMARY KEY AUTO_INCREMENT,
    manager_id INT,
    type VARCHAR(255),
    status VARCHAR(255),
    location VARCHAR(255),
    FOREIGN KEY (manager_id) REFERENCES Employees(id)
);