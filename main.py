# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)
# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql(""" SELECT e.firstName, e.lastName 
                            FROM employees e
                            JOIN offices o ON e.officeCode = o.officeCode
                            WHERE o.city == 'Boston'
                            ;""", conn)
# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""
    SELECT COUNT(*)
    FROM employees e
    JOIN offices o  ON e.officeCode= o.officeCode
    GROUP BY o.officeCode; 
    """, conn)
# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
        SELECT e.firstName, e.lastName, o.city, o.state
        FROM employees e
        JOIN offices o ON e.officeCode = o.officeCode;
""", conn)
# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT c.contactLastName, c.contactFirstName, c.phone, c.salesRepEmployeeNumber 
    FROM customers c
    JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    ORDER BY c.contactLastName
""", conn)
# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT contactLastName,contactFirstName, p.amount, p.paymentDate
    FROM customers c
    JOIN payments p ON c.customerNumber= p.customerNumber
    ORDER BY CAST(p.amount AS REAL) DESC                
""",conn)
# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT e.employeeNumber, e.firstName, e.lastName, COUNT(c.customerNumber) AS customer_count
    FROM customers c
    JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber
    WHERE creditLimit > 90000 
    GROUP BY e.employeeNumber
    ORDER BY customer_count DESC                     
""", conn)
# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""
SELECT p.productName, COUNT(o.orderNumber) AS numorders,SUM(o.quantityOrdered) AS totalunits
FROM products p
JOIN orderDetails o ON o.productCode= p.productCode
GROUP BY p.productCode
ORDER by totalunits DESC      
""", conn)
# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT   p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers
    FROM products p
    JOIN orderDetails od ON p.productCode = od.productCode
    JOIN orders o ON od.orderNumber = o.orderNumber  
    GROUP BY p.productCode
    ORDER BY numpurchasers DESC                          
""",conn)
# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
SELECT o.officeCode, COUNT(c.customerNumber) AS n_customers
FROM offices o
JOIN employees e ON o.officeCode= e.officeCode
JOIN customers c ON e.employeeNumber=c.salesRepEmployeeNumber 
GROUP BY o.officeCode
""",conn)
# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""
    SELECT DISTINCT e.employeeNumber,e.firstName, e.lastName,of.city,of.officeCode
    FROM employees e
    JOIN customers c ON e.employeeNumber=c.salesRepEmployeeNumber
    JOIN orders o ON c.customerNumber= o.customerNumber
    JOIN orderdetails od ON o.orderNumber= od.orderNumber
    JOIN offices of ON e.officeCode= of.officeCode
    WHERE od.productCode IN(
    SELECT p.productCode
    FROM products p
    JOIN orderdetails od2 ON p.productCode= od2.productCode
    JOIN orders o2 ON od2.orderNumber= o2.orderNumber
    GROUP BY p.productCode
    HAVING COUNT(DISTINCT o2.customerNumber)<20             
    )                                                
""",conn)
# Run this cell without changes

conn.close()