import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect("student.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Corrected SQL command for creating the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25), 
    CLASS VARCHAR(25), 
    SECTION VARCHAR(25), 
    MARKS INT
);
"""

# Execute the table creation
cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT VALUES ('vijay', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('vinay', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Mukesh', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('sujit', 'DEVOPS', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)")

# Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# Commit changes and close the connection
connection.commit()
connection.close()
