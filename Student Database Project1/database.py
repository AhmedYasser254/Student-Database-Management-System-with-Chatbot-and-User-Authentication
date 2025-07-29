from student import Student
import sqlite3

class Database:
    def __init__(self):
        # Connect to SQLite database (or create it if it doesn't exist)
        self.connection = sqlite3.connect('student_db.sqlite')
        self.cursor = self.connection.cursor()
        # Create the students table if it doesn't exist
        self.create_table()

    def create_table(self):
        # SQL query to create the students table
        query = '''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL
        );
        '''
        self.cursor.execute(query)
        self.connection.commit()

    def insert_student(self, student):
        # Insert a student record into the table
        query = "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)"
        self.cursor.execute(query, (student.name, student.age, student.grade))
        self.connection.commit()

    def get_all_students(self):
        # Get all students from the table
        query = "SELECT * FROM students"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_student_by_id(self, student_id):
        # Get a specific student by ID
        query = "SELECT * FROM students WHERE id = ?"
        self.cursor.execute(query, (student_id,))
        return self.cursor.fetchone()
    def get_student_by_name(self, student_name):
        # Get a specific student by name
        query = "SELECT * FROM students WHERE name = ?"
        self.cursor.execute(query, (student_name,))
        return self.cursor.fetchone()
    
    def update_student(self, student):
        # Update a student's information based on their ID
        query = "UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?"
        self.cursor.execute(query, (student.name, student.age, student.grade, student.student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        # Delete a student by ID
        query = "DELETE FROM students WHERE id = ?"
        self.cursor.execute(query, (student_id,))
        self.connection.commit()

    def delet_student_name(self, student_name):
        # Delete a student by name
        query = "DELETE FROM students WHERE name = ?"
        self.cursor.execute(query, (student_name,))
        self.connection.commit()


    def close(self):
        # Close the database connection
        self.cursor.close()
        self.connection.close()
