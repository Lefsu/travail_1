# LEFEVRE Sullivan - MOREAU Guy-Loup

import mysql.connector
from faker import Faker
import random

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",     
    password="your_password", 
    database="your_database"  
)

cursor = conn.cursor()
faker = Faker()

def get_max_id(table_name, id_column):
    cursor.execute(f"SELECT IFNULL(MAX({id_column}), 0) FROM {table_name}")
    result = cursor.fetchone()
    return result[0]

max_department_id = max(get_max_id('Department', 'id'), 10)
max_employee_id = max(get_max_id('Employees', 'id'), 10)
max_system_id = max(get_max_id('Systems', 'id'), 10)
max_audit_id = max(get_max_id('SecurityAudits', 'id'), 10)

for _ in range(10):
    cursor.execute(
        "INSERT INTO Department (manager_id, type, status, location) VALUES (%s, %s, %s, %s)",
        (
            random.randint(1, max_employee_id),  
            faker.word(),
            random.choice(["Active", "Inactive"]),
            faker.city()
        )
    )

for _ in range(10):
    cursor.execute(
        "INSERT INTO Employees (last_name, first_name, position, department_id) VALUES (%s, %s, %s, %s)",
        (
            faker.last_name(),
            faker.first_name(),
            random.choice(["Cybersecurity Engineer", "Pentester", "HR", "SOC member", "Network Admin"]),
            random.randint(1, max_department_id)
        )
    )

for _ in range(10):
    cursor.execute(
        "INSERT INTO Systems (name, type, department_id, manager_id) VALUES (%s, %s, %s, %s)",
        (
            faker.word(),
            random.choice(["Web Application", "Database", "Network", "Server"]),
            random.randint(1, max_department_id),  
            random.randint(1, max_employee_id)   
        )
    )

for _ in range(10):
    cursor.execute(
        "INSERT INTO SecurityAudits (date, status, employee_id, system_id) VALUES (%s, %s, %s, %s)",
        (
            faker.date_between(start_date='-2y', end_date='today'),  
            random.choice(["Completed", "In Progress", "Scheduled"]),
            random.randint(1, max_employee_id),  
            random.randint(1, max_system_id)   
        )
    )

for _ in range(10):
    cursor.execute(
        "INSERT INTO VulnerabilitiesDetected (audit_id, system_id, severity, status) VALUES (%s, %s, %s, %s)",
        (
            random.randint(1, max_audit_id),  
            random.randint(1, max_system_id),  
            random.choice(["Low", "Medium", "High", "Critical"]),
            random.choice(["New", "In Progress", "Resolved"])
        )
    )

conn.commit()
cursor.close()
conn.close()