#Q1. What is a database? Differentiate between SQL and NoSQL databases.
'''A database is an organized collection of structured information, or data, 
typically stored electronically in a computer system. A database is usually 
controlled by a database management system (DBMS). Together, the data and the 
DBMS, along with the applications that are associated with them, are referred 
to as a database system, often shortened to just database.

Difference
-SQL databases are relational, and NoSQL databases are non-relational.
-SQL databases use structured query language (SQL) and have a predefined schema.
 NoSQL databases have dynamic schemas for unstructured data.
-SQL databases are vertically scalable, while NoSQL databases are horizontally scalable.
-SQL databases are table-based, while NoSQL databases are document, key-value, graph, or wide-column stores.
-SQL databases are better for multi-row transactions, while NoSQL is better for unstructured data like documents or JSON
'''

#Q2. What is DDL? Explain why CREATE,DROP,ALTER, and TRUNCATE are used with an example.
'''DDL stands for Data Definition Language. DDL consist of Commands to commands like 
CREATE, ALTER, TRUNCATE and DROP. 
These commands are used to create or modify the tables in SQL.
CREATE: It is used for creating Table.
ALTER: This command is used to add, delete or change columns in the existing table.
TRUNCATE: This command is used to remove all rows from the table, but the structure of the table still exists.
DROP: This command is used to remove an existing table along with its structure from the Database.
'''
#Q3. What is DML? Explain INSERT,UPDATE, and DELETE with an example.
''' The SQL commands that deal with the manipulation of data present 
in the database belong to DML
INSERT: It is used to insert data into a table.
UPDATE: It is used to update existing data within a table.
DELETE: It is used to delete records from a database table.'''
#Q4. What is DQL? Explain with an example.
'''We can define DQL as follows it is a component of SQL statement
that allows getting data from the database and imposing order upon it.
It includes the SELECT statement. This command allows getting the 
data out of the database to perform operations with it.'''

#Q5. Explain Primary Key and Foreign Key.
'''A primary key is used to ensure that data in the specific column is unique. 
A column cannot have NULL values.
A foreign key is a column or group of columns in a relational 
database table that provides a link between data in two tables. 
It is a column (or columns) that references a column (most often the primary key) of another table. 
'''
#Q6. Write a python code to connect MySQL to python. Explain the cursor() and execute() method.
'''The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements 
to communicate with the MySQL database. You can create Cursor object using the cursor() method of
the Connection object/class.'''

#Q7. Give the order of execution of SQL clauses in an SQL query.
'''FROM/JOIN
WHERE
GROUP BY
HAVING
SELECT
ORDER BY
LIMIT/OFFSET'''

import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Troy@_37',database='trish')
my_cursor=conn.cursor()
my_cursor.execute('insert into employee values(104,"Esha Mishra","F","E8",823.4)')
conn.commit()
conn.close()
print("connection succesfully created")