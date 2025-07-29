# import streamlit as st
# import json
# from hashlib import sha256
# from chatbot import Chatbot
# from database import Database
# from student import Student
# import time

# # Initialize Database and Chatbot
# db = Database()
# chatbot = Chatbot(db)

# # Load Credentials and Users from JSON
# def load_credentials():
#     with open('credentials.json') as f:
#         return json.load(f)

# def load_users():
#     with open('users.json') as f:
#         return json.load(f)

# def save_users(users):
#     with open('users.json', 'w') as f:
#         json.dump(users, f, indent=4)

# # Hash password using SHA256
# def hash_password(password):
#     return sha256(password.encode()).hexdigest()

# # Login Page
# def login_page():
#     st.title("Login")
#     user_type = st.radio("Login as:", ["Admin", "User"])
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
    
#     if st.button("Login"):
#         if user_type == "Admin":
#             creds = load_credentials()['admin']
#             Readpass = hash_password(password)
#             # Check if the username and hashed password match the admin credentials
#             if username == creds['username'] and Readpass == creds['password']:
#                 st.session_state.logged_in = True
#                 st.session_state.user_type = "Admin"
#                 st.session_state.username = username
#                 st.success("Logged in as Admin")
#                 st.rerun()  # Refresh the page to show the Admin Dashboard
#             else:
#                 st.error("Invalid Admin credentials")
#         else:
#             users = load_users()
#             if username in users and users[username] == hash_password(password):
#                 st.session_state.logged_in = True
#                 st.session_state.user_type = "User"
#                 st.session_state.username = username
#                 st.success("Logged in as User")
#                 st.rerun()  # Automatically refresh the page and go to User Dashboard
#             else:
#                 st.error("Invalid User credentials")

# # Register Page
# def register_page():
#     st.title("Register")
#     username = st.text_input("New Username")
#     password = st.text_input("New Password", type="password")
#     if st.button("Register"):
#         users = load_users()
#         if username in users:
#             st.error("Username already exists")
#         else:
#             users[username] = hash_password(password)
#             save_users(users)
#             st.session_state.logged_in = True
#             st.session_state.user_type = "User"
#             st.session_state.username = username
#             st.success("User registered successfully, logging in...")
#             st.rerun()  # Automatically refresh the page to go to the User Dashboard

# # Admin Dashboard
# def Admin_Dashboard():
#     st.subheader("Admin Dashboard")
#     # Tabs for different actions
#     admin_tab = st.radio("Choose an action", ["Add Student", "View Students", "Update Student", "Delete Student"])

#     if admin_tab == "Add Student":
#         st.subheader("Add Student")
#         name = st.text_input("Name")
#         age = st.number_input("Age", min_value=18, max_value=30)
#         grade = st.text_input("Grade")
#         if st.button("Add Student"):
#             chatbot_query = f"add student {name} {age} {grade}"
#             response = chatbot.handle_queries(chatbot_query)
#             st.success(response)
#     elif admin_tab == "View Students":
#         st.subheader("View Students")
#         students = db.get_all_students()
#         if students:
#             for student in students:
#                 st.write(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
#         else:
#             st.write("No students found.")
#     elif admin_tab == "Delete Student":
#         st.subheader("Delete Student")
#         student_id = st.number_input("Student ID to delete", min_value=1, step=1)
#         if st.button("Delete Student"):
#             chatbot_query = f"delete student {student_id}"
#             response = chatbot.handle_queries(chatbot_query)
#             st.success(response)

# # User Dashboard
# def User_Dashboard():
#     st.subheader("User Dashboard")
#     st.write("Welcome to the User Dashboard!")
    
#     # Initialize chat history
#     if "messages" not in st.session_state:
#         st.session_state.messages = []
#     if not st.session_state.messages:
#         st.session_state.messages.append({"role": "assistant", "content": " Ask me anything about students."})
    
#     # Display existing messages in the chat
#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     # User input for the chatbot
#     query = st.chat_input("Add Your Message")
    
#     # Handle the user query
#     if query:
#         # Show user message immediately
#         st.session_state.messages.append({"role": "user", "content": query})
#         with st.chat_message("user"):
#             st.markdown(query)
        
#         # Assistant response generation
#         with st.chat_message("assistant"):
#             message_placeholder = st.empty()
#             with st.spinner("Assistant is typing..."):
#                 time.sleep(2.5)  # Simulate typing delay
#                 response = chatbot.handle_queries(query)  # Get response from chatbot
#             message_placeholder.markdown(response)
#             st.session_state.messages.append({"role": "assistant", "content": response})

#     # Add download functionality for chat history
#     if st.session_state.messages and len(st.session_state.messages) > 1:
#         chat_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
#         st.sidebar.download_button(
#             "Download chat", 
#             chat_text,
#             file_name="chat_history.txt",
#             mime="text/plain"
#         )

# # Main Application
# st.title("Student Database Chatbot")
# st.set_page_config(
#     page_title="Student Database Chatbot",
#     page_icon="📝",
#     layout="wide"
# )

# def display_dashboard():
#     if st.session_state.logged_in:
#         if st.session_state.user_type == "Admin":
#             Admin_Dashboard()
#         else:
#             User_Dashboard()

# if __name__ == "__main__":
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False

# # Sidebar Navigation
# st.sidebar.title("Navigation")
# page = st.sidebar.radio("Go to", ["Login", "Register"])
# if st.sidebar.button("Clear conversation"):
#     st.session_state.messages = []

# if not st.session_state.logged_in:
#     # Show login or registration page if not logged in
#     if page == "Login":
#         login_page()  # Display the login page
#     else:
#         register_page()  # Display the registration page
# else:
#     # If the user is logged in, display the corresponding dashboard
#     display_dashboard()
import streamlit as st
import json
from hashlib import sha256
from chatbot import Chatbot
from database import Database
from student import Student
import time
import random

greetings = [
    "Hello! How can I assist you today?",
    "Hi! I'm your student database assistant. How can I help you?",
    "Greetings! Ask me anything about students.",
    "Hey! Ready to manage your student data? Let me know what you need."
]
# Initialize Database and Chatbot
db = Database()
chatbot = Chatbot(db)

# Load Credentials and Users from JSON
def load_credentials():
    with open('credentials.json') as f:
        return json.load(f)

def load_users():
    with open('users.json') as f:
        return json.load(f)

def save_users(users):
    with open('users.json', 'w') as f:
        json.dump(users, f, indent=4)

# Hash password using SHA256
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Login Page
def login_page():
    st.title("Login")
    user_type = st.radio("Login as:", ["Admin", "User"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if user_type == "Admin":
            creds = load_credentials()['admin']
            Readpass = hash_password(password)
            # Check if the username and hashed password match the admin credentials
            if username == creds['username'] and Readpass == creds['password']:
                st.session_state.logged_in = True
                st.session_state.user_type = "Admin"
                st.session_state.username = username
                st.success("Logged in as Admin")
                st.rerun()  # Refresh the page to show the Admin Dashboard
            else:
                st.error("Invalid Admin credentials")
        else:
            users = load_users()
            if username in users and users[username] == hash_password(password):
                st.session_state.logged_in = True
                st.session_state.user_type = "User"
                st.session_state.username = username
                st.success("Logged in as User")
                st.rerun()  # Automatically refresh the page and go to User Dashboard
            else:
                st.error("Invalid User credentials")

# Register Page
def register_page():
    st.title("Register")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    if st.button("Register"):
        users = load_users()
        if username in users:
            st.error("Username already exists")
        else:
            users[username] = hash_password(password)
            save_users(users)
            st.session_state.logged_in = True
            st.session_state.user_type = "User"
            st.session_state.username = username
            st.success("User registered successfully, logging in...")
            st.rerun()  # Automatically refresh the page to go to the User Dashboard


def logout_button():
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_type = ""
        st.session_state.username = ""
        st.success("You have logged out successfully.")
        st.rerun()  # Refresh the page to show the Login/Register page

def exit():
    st.session_state.logged_in = False
    st.session_state.user_type = ""
    st.session_state.username = ""
    st.success("You have logged out successfully.")
    st.rerun()
    
# Admin Dashboard
# def Admin_Dashboard():
#     st.subheader("Admin Dashboard")
#     # Tabs for different actions
#     admin_tab = st.radio("Choose an action", ["Add Student", "View Students", "Update Student", "Delete Student"])

#     if admin_tab == "Add Student":
#         st.subheader("Add Student")
#         name = st.text_input("Name")
#         age = st.number_input("Age", min_value=18, max_value=30)
#         grade = st.text_input("Grade")

#         if st.button("Add Student"):
#             chatbot_query = f"add student {name} {age} {grade}"
#             response = chatbot.handle_queries(chatbot_query)
#             st.success(response)
            
#     elif admin_tab == "View Students":
#         st.subheader("View Students")
#         chatbot_query = f"list all students"
#         response = chatbot.handle_queries(chatbot_query)
#         st.write(response)
#         if response:
#             for student in response:
#                 st.write(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
#         else:
#             st.write("No students found.")

#     elif admin_tab == "Delete Student":
#         st.subheader("Delete Student")
#         student_id = st.number_input("Student ID to delete", min_value=1, step=1)
#         if st.button("Delete Student"):
#             chatbot_query = f"delete student {student_id}"
#             response = chatbot.handle_queries(chatbot_query)
#             st.success(response)

def Admin_Dashboard():
    st.subheader("Admin Dashboard")
    
    # Tabs for different actions
    admin_tab = st.radio("Choose an action", ["Add Student", "View Students", "Update Student", "Delete Student"])

    # Add Student Tab
    if admin_tab == "Add Student":
        st.subheader("Add Student")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=18, max_value=30)
        grade = st.text_input("Grade")

        if st.button("Add Student"):
            # Generate query for adding student
            chatbot_query = f"add student {name} {age} {grade}"
            response = chatbot.handle_queries(chatbot_query)
            st.success(response)

    # View Students Tab
    # View Students Tab
    # View Students Tab
    # View Students Tab
    elif admin_tab == "View Students":
        st.subheader("View Students")
        # Request for all students
        students = db.get_all_students()

        if students:
            student_found = False  # Flag to track if valid student data is found
            for student in students:
                # Ensure that the student has the correct number of fields (ID, Name, Age, Grade)
                if len(student) == 4:  # Check for a valid record with 4 fields
                    student_found = True
                    st.write(f"**ID**: {student[0]}")
                    st.write(f"**Name**: {student[1]}")
                    st.write(f"**Age**: {student[2]}")
                    st.write(f"**Grade**: {student[3]}")
                    st.write("---")
            
            if not student_found:
                st.write("No valid student records found.")
        else:
            st.write("No students found in the database.")




    # Update Student Tab
    elif admin_tab == "Update Student":
        st.subheader("Update Student Information")
        student_id = st.number_input("Student ID to Update", min_value=1, step=1)
        
        student = db.get_student_by_id(student_id)  # Fetch student details for the given ID
        if student:
            st.write(f"Current details for {student[1]} (ID: {student[0]}):")
            st.write(f"**Name**: {student[1]}")
            st.write(f"**Age**: {student[2]}")
            st.write(f"**Grade**: {student[3]}")
            
            # Input fields for new student data
            new_name = st.text_input("New Name", value=student[1])
            new_age = st.number_input("New Age", min_value=18, max_value=100, value=student[2])
            new_grade = st.text_input("New Grade", value=student[3])

            if st.button("Update Student"):
                # Generate query for updating student information
                chatbot_query = f"update student {student_id} {new_name} {new_age} {new_grade}"
                response = chatbot.handle_queries(chatbot_query)
                st.success(response)
        else:
            st.write("Student not found.")

    # Delete Student Tab
    elif admin_tab == "Delete Student":
        st.subheader("Delete Student")
        student_id = st.number_input("Student ID to delete", min_value=1, step=1)
        if st.button("Delete Student"):
            # Generate query to delete student
            chatbot_query = f"delete student {student_id}"
            response = chatbot.handle_queries(chatbot_query)
            st.success(response)



# User Dashboard
def User_Dashboard():
    st.subheader("User Dashboard")
    st.write("Welcome to the User Dashboard!")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if not st.session_state.messages:
        st.session_state.messages.append({"role": "assistant", "content": random.choice(greetings)})
    
    # Display existing messages in the chat
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # User input for the chatbot
    query = st.chat_input("Add Your Message")
    
    # Handle the user query
    if query:
        # Show user message immediately
        st.session_state.messages.append({"role": "user", "content": query})
        

        with st.chat_message("user"):
            st.markdown(query)
        
        # Assistant response generation
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            with st.spinner("Assistant is typing..."):
                time.sleep(2.5)  # Simulate typing delay
                response = chatbot.handle_queries(query)  
            message_placeholder.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})


# Main Application
st.title("Student Database Chatbot")
st.set_page_config(
    page_title="Student Database Chatbot",
    page_icon="📝",
    layout="wide"
)

def display_dashboard():
    if st.session_state.logged_in:
        if st.session_state.user_type == "Admin":
            Admin_Dashboard()
        else:
            User_Dashboard()

if __name__ == "__main__":
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Login", "Register"])
if st.sidebar.button("Clear conversation"):
    st.session_state.messages = []
if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_type = ""
        st.session_state.username = ""
        st.success("You have logged out successfully.")
        st.rerun()

if not st.session_state.logged_in:
    # Show login or registration page if not logged in
    if page == "Login":
        login_page()  # Display the login page
    else:
        register_page()  # Display the registration page
else:
    # If the user is logged in, display the corresponding dashboard
    display_dashboard()


