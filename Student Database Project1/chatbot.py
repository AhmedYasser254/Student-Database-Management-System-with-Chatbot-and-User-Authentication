# from database import Database
# from student import Student
# class Chatbot():
#     def __init__(self, db: Database):
#         self.db = db
#         self.responses = {
#             'greeting': ['hello', 'hi', 'hey', 'greetings'],
#             'add_student': ['add student to my database','add the following student'],
#             'total_students': ['how many students', 'total students', 'number of students'],
#             'student_info': ['tell me about', 'information about', 'details of'],
#             'all_students': ['show all students', 'list all students', 'all students'],
#             'grades': ['what grades', 'grade levels', 'available grades'],
#             'help': ['help', 'what can you do', 'commands']
#         }

#     def handle_queries(self, query):

#         query = query.lower().strip()



#         if query.startswith("add student"):
#             print(query.split())
#             _, _, _,name, age, grade = query.split()
#             student = Student(name=name, age=int(age), grade=grade)
#             self.db.insert_student(student)
#             return f"Student {name} added successfully."
        
#         elif any(greeting in query for greeting in self.responses['greeting']):
#             return "Hello! I'm your student database assistant. Ask me about students, grades, or say 'help' for available commands."
        
#         elif query.startswith("get all students"):
#             students = self.db.get_all_students()
#             print(students)
#             student_info = []

#             for s in students:
#                 student_info.append(f"ID: {s[0]}")
#                 student_info.append(f"Name: {s[1]}")
#                 student_info.append(f"Age: {s[2]}")
#                 student_info.append(f"Grade: {s[3]}")
#                 student_info.append("")  # Adding an empty line between students

#             return "\n".join(student_info) if student_info else "No students found."

#         elif query.startswith("get student"):
#             print(query.split())
#             _, _, student_id = query.split()
#             student = self.db.get_student_by_id(int(student_id))
#             if student:
#                 return f"{student[0]}: {student[1]}, Age: {student[2]}, Grade: {student[3]}"
#             else:
#                 return "Student not found."

#         elif query.startswith("delete student"):
#             _, _, student_id = query.split()
#             self.db.delete_student(int(student_id))
#             return f"Student with ID {student_id} deleted successfully."

#         elif query.startswith("update student"):
#             _, _, student_id, name, age, grade = query.split()
#             student = Student(student_id=int(student_id), name=name, age=int(age), grade=grade)
#             self.db.update_student(student)
#             return f"Student with ID {student_id} updated successfully."
#         elif query.startswith("get student by name"):
#             _, _, student_name = query.split()
#             student = self.db.get_student_by_name(student_name)
#             if student:
#                 return f"{student[0]}: {student[1]}, Age: {student[2]}, Grade: {student[3]}"
#             else:
#                 return "Student not found by name."
#         elif query.startswith("delete student by name"):
#             _, _, student_name = query.split()
#             student = self.db.get_student_by_name(student_name)
#             if student:
#                 self.db.delete_student(student[0])
#                 return f"Student {student_name} deleted successfully."
#             else:
#                 return "Student not found by name."
#         elif query.startswith("help"):
#             return ("Available commands:\n"
#                     "- add student <name> <age> <grade>\n"
#                     "- get all students\n"
#                     "- get student <id>\n"
#                     "- delete student <id>\n"
#                     "- update student <id> <name> <age> <grade>\n"
#                     "- get student by name <name>\n"
#                     "- delete student by name <name>\n"
#                     "- Introduce yourself")
#         elif query.startswith("clear chat".lower()):
#             return "Chat cleared."
        
#         elif query.startswith("exit"):
#             return "Exiting the chatbot. Goodbye!"
        
#         elif query.startswith(("Introduce yourself").lower()):
#             return "I am AI Chatbot for Manging the Students database"
#         else:
#             return "Unknown command."


# from database import Database
# from student import Student
# import re
# import streamlit as st
# def ex():
#     st.session_state.logged_in = False
#     st.session_state.user_type = ""
#     st.session_state.username = ""
#     st.success("You have logged out successfully.")
        
#     st.rerun()
# class Chatbot():
#     def __init__(self, db: Database):
#         self.db = db
#         self.responses = {
#             'greeting': ['hello', 'hi', 'hey', 'greetings'],
#             'add_student': ['add student to my database', 'add the following student', 'add student'],
#             'total_students': ['how many students', 'total students', 'number of students'],
#             'student_info': ['tell me about', 'information about', 'details of'],
#             'all_students': ['show all students', 'list all students', 'all students'],
#             'grades': ['what grades', 'grade levels', 'available grades'],
#             'help': ['help', 'what can you do', 'commands', 'how do you work'],
#             'exit': ['exit', 'quit', 'goodbye']
#         }

#     def handle_queries(self, query):
#         query = query.lower().strip()

#         # Greeting responses
#         if any(greeting in query for greeting in self.responses['greeting']):
#             return "Hello! I'm your student database assistant. Ask me about students, grades, or say 'help' for available commands."

#         # Help command
#         elif any(help_query in query for help_query in self.responses['help']):
#             return ("Available commands:\n"
#                     "- add student <name> <age> <grade>\n"
#                     "- get all students\n"
#                     "- get student <id>\n"
#                     "- delete student <id>\n"
#                     "- update student <id> <name> <age> <grade>\n"
#                     "- get student by name <name>\n"
#                     "- delete student by name <name>\n"
#                     "- Show total students\n"
#                     "- Show grades available\n"
#                     "- exit")

#         # Add student command
#         elif any(add_query in query for add_query in self.responses['add_student']):
#             match = re.match(r"add student (.+?) (\d+) (\w+)", query)
#             if match:
#                 name, age, grade = match.groups()
#                 student = Student(name=name, age=int(age), grade=grade)
#                 self.db.insert_student(student)
#                 return f"Student {name} added successfully."
#             else:
#                 return "Please provide the student's name, age, and grade (e.g., 'add student John 20 A')."

#         # Get all students
#         elif any(all_students_query in query for all_students_query in self.responses['all_students']):
#             students = self.db.get_all_students()
#             student_info = [f"ID: {s[0]}, Name: {s[1]}, Age: {s[2]}, Grade: {s[3]}" for s in students]
#             return "\n".join(student_info) if student_info else "No students found."

#         # Get student by ID
#         elif query.startswith("get student"):
#             student_id = self.extract_student_id(query)
#             if student_id:
#                 student = self.db.get_student_by_id(student_id)
#                 if student:
#                     return f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}"
#                 else:
#                     return "Student not found."
#             else:
#                 return "Please provide a valid student ID."

#         # Delete student by ID
#         elif query.startswith("delete student"):
#             student_id = self.extract_student_id(query)
#             if student_id:
#                 self.db.delete_student(student_id)
#                 return f"Student with ID {student_id} deleted successfully."
#             else:
#                 return "Please provide a valid student ID to delete."

#         # Update student information
#         elif query.startswith("update student"):
#             match = re.match(r"update student (\d+) (.+?) (\d+) (\w+)", query)
#             if match:
#                 student_id, name, age, grade = match.groups()
#                 student = Student(student_id=int(student_id), name=name, age=int(age), grade=grade)
#                 self.db.update_student(student)
#                 return f"Student with ID {student_id} updated successfully."
#             else:
#                 return "Please provide the correct format (e.g., 'update student 1 John 22 B')."

#         # Total number of students
#         elif any(total_query in query for total_query in self.responses['total_students']):
#             total = len(self.db.get_all_students())
#             return f"There are {total} students in the database."

#         # Grades available
#         elif any(grades_query in query for grades_query in self.responses['grades']):
#             grades = self.db.get_all_grades()
#             if grades:
#                 return f"Available grades: {', '.join(grades)}"
#             else:
#                 return "No grades found in the database."

#         # Exit chatbot
#         elif any(exit_query in query for exit_query in self.responses['exit']):
#             return ex()

#         else:
#             return "Sorry, I didn't understand that. Please try asking something else or say 'help' for available commands."

#     def extract_student_id(self, query):
#         """Helper function to extract student ID from the query"""
#         match = re.match(r"\D*(\d+)", query)
#         if match:
#             return int(match.group(1))
#         return None


from database import Database
from student import Student
import re
import streamlit as st
import random
import time

greetings = [
    "Hello! How can I assist you today?",
    "Hi! I'm your student database assistant. How can I help you?",
    "Greetings! Ask me anything about students.",
    "Hey! Ready to manage your student data? Let me know what you need."
]

class Chatbot():
    def __init__(self, db: Database):
        self.db = db
        self.responses = {
            'greeting': ['hello', 'hi', 'hey', 'greetings'],
            'add_student': ['add student to my database', 'add the following student', 'add student'],
            'total_students': ['how many students', 'total students', 'number of students'],
            'student_info': ['tell me about', 'information about', 'details of'],
            'all_students': ['show all students', 'list all students', 'all students'],
            'grades': ['what grades', 'grade levels', 'available grades'],
            'help': ['help', 'what can you do', 'commands', 'how do you work'],
            'exit': ['exit', 'quit', 'goodbye']
        }

    def handle_queries(self, query):
        query = query.lower().strip()

        # Greeting responses
        if any(greeting in query for greeting in self.responses['greeting']):
            return self.generate_greeting()

        # Help command
        elif any(help_query in query for help_query in self.responses['help']):
            return self.generate_help()

        # Add student command
        elif any(add_query in query for add_query in self.responses['add_student']):
            return self.add_student(query)

        # Get all students
        elif any(all_students_query in query for all_students_query in self.responses['all_students']):
            return self.get_all_students()

        # Get student by ID
        elif query.startswith("get student"):
            return self.get_student_by_id(query)

        # Delete student by ID
        elif query.startswith("delete student"):
            return self.delete_student(query)

        # Update student information
        elif query.startswith("update student"):
            return self.update_student(query)

        # Total number of students
        elif any(total_query in query for total_query in self.responses['total_students']):
            return self.get_total_students()

        # Grades available
        elif any(grades_query in query for grades_query in self.responses['grades']):
            return self.get_available_grades()

        # Exit chatbot
        elif any(exit_query in query for exit_query in self.responses['exit']):
            return self.exit()

        else:
            return self.unknown_command()

    def generate_greeting(self):
        """Generate a dynamic greeting message."""
        if "username" in st.session_state:
            return f"Hello {st.session_state.username}, how can I assist you today?"
        return random.choice(greetings)

    def generate_help(self):
        """Provide help commands dynamically."""
        return (
            "Here are the available commands:\n"
            "- Add a student: 'Add student <name> <age> <grade>'\n"
            "- View all students: 'Show all students'\n"
            "- Get student by ID: 'Get student <id>'\n"
            "- Delete a student: 'Delete student <id>'\n"
            "- Update student info: 'Update student <id> <name> <age> <grade>'\n"
            "- Get total students: 'How many students'\n"
            "- Get available grades: 'What grades are available?'\n"
            "- Exit: 'Exit'"
        )

    def add_student(self, query):
        """Handle adding a student."""
        match = re.match(r"add student (.+?) (\d+) (\w+)", query)
        if match:
            name, age, grade = match.groups()
            student = Student(name=name, age=int(age), grade=grade)
            self.db.insert_student(student)
            return f"Student {name} added successfully."
        return "Please provide the student's name, age, and grade in the correct format (e.g., 'add student John 20 A')."

    # Get all students
    # Get all students
    def get_all_students(self):
        """Return all students."""
        students = self.db.get_all_students()
        if students:
            student_info = ""
            for student in students:
                # Check if the student record has the expected number of fields (4: ID, Name, Age, Grade)
                if len(student) == 4:
                    student_info += f"**ID**: {student[0]}\n**Name**: {student[1]}\n**Age**: {student[2]}\n**Grade**: {student[3]}\n\n"
                else:
                    student_info += "Invalid student data format.\n\n"
            return student_info
        return "No students found."



    def get_student_by_id(self, query):
        """Return student by ID."""
        student_id = self.extract_student_id(query)
        if student_id:
            student = self.db.get_student_by_id(student_id)
            if student:
                return f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}"
            return "Student not found."
        return "Please provide a valid student ID."

    def delete_student(self, query):
        """Delete student by ID."""
        student_id = self.extract_student_id(query)
        if student_id:
            self.db.delete_student(student_id)
            return f"Student with ID {student_id} deleted successfully."
        return "Please provide a valid student ID to delete."

    def update_student(self, query):
        """Update student information."""
        match = re.match(r"update student (\d+) (.+?) (\d+) (\w+)", query)
        if match:
            student_id, name, age, grade = match.groups()
            student = Student(student_id=int(student_id), name=name, age=int(age), grade=grade)
            self.db.update_student(student)
            return f"Student with ID {student_id} updated successfully."
        return "Please provide the correct format (e.g., 'update student 1 John 22 B')."

    def get_total_students(self):
        """Return the total number of students."""
        total = len(self.db.get_all_students())
        return f"There are {total} students in the database."

    def get_available_grades(self):
        """Return available grades."""
        grades = self.db.get_all_grades()
        if grades:
            return f"Available grades: {', '.join(grades)}"
        return "No grades found in the database."

    def exit(self):
        """Exit the chatbot."""
        st.session_state.logged_in = False
        st.session_state.user_type = ""
        st.session_state.username = ""
        return "You have logged out successfully. Goodbye!"

    def unknown_command(self):
        """Return a message for unknown commands."""
        return "Sorry, I didn't understand that. Please try asking something else or say 'help' for available commands."

    def extract_student_id(self, query):
        """Helper function to extract student ID from the query."""
        match = re.match(r"\D*(\d+)", query)
        if match:
            return int(match.group(1))
        return None
