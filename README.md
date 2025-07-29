# Student-Database-Management-System-with-Chatbot-and-User-Authentication
# Student Database Chatbot

---

## 🎯 Features

- **User Authentication**  
  - **Admin**: Can add, view, update, and delete student records.  
  - **User**: Can interact with the chatbot to retrieve student information.

- **Admin Dashboard**  
  - Add a new student (name, age, grade)  
  - View all students in a clear, line‑by‑line format  
  - Update existing student details  
  - Delete a student by ID  

- **User Dashboard**  
  - Chatbot interface powered by keyword‑based intent recognition  
  - Ask natural‑language questions about students (e.g. “How many students?”, “Tell me about John”)  
  - Download full chat transcript as a text file  

- **Security**  
  - Passwords are hashed with SHA‑256  
  - Credentials stored in JSON (`credentials.json` and `users.json`)  
  - Session‑based login/logout  

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-database-chatbot.git
cd student-database-chatbot
```

### 2. Create & Activate a Virtual Environment

- **Windows**  
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS/Linux**  
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare Credential Files

Create or update two JSON files in the project root:

- **`credentials.json`**  
  ```json
  {
    "admin": {
      "username": "admin",
      "password": "<sha256-hash-of-admin-password>"
    }
  }
  ```

- **`users.json`**  
  ```json
  {
    "user1": "<sha256-hash-of-user1-password>",
    "user2": "<sha256-hash-of-user2-password>"
  }
  ```

You can generate a SHA‑256 hash in Python:

```python
import hashlib
print(hashlib.sha256("yourPassword".encode()).hexdigest())
```

### 5. Run the App

```bash
streamlit run app.py
```
