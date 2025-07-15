# 📚 Library Management System

A simple **Library Management Web App** built with **Flask**, **MySQL**, and **SQLAlchemy**.  
Librarians can manage books, members, issue & return transactions — and import book data directly from the **Frappe Library API**!

---

## ✅ **Features**

- 📖 Add, view, and delete books
- 🔍 Import books from the [Frappe Library API](https://frappe.io/api/method/frappe-library)
- 👤 Add and remove members
- 📕 Issue books to members with stock checks & outstanding debt checks
- 📗 Return books and add late fees
- MySQL database with SQLAlchemy ORM
- Clean responsive HTML templates with inline CSS

---

## 🗂 **Project Structure**
```
/Library_app
├── app.py
├── config.py
├── requirements.txt
├── models/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── transaction.py
├── templates/
│   ├── books.html
│   ├── members.html
│   ├── issue.html
│   ├── return.html

```
##  ⚙️ **Setup**
-  1️⃣ Clone the repository
```
git clone https://github.com/RahulPatil-Tech/Library-Management-System.git
cd Library-Management-System
```
- 2️⃣ Create virtual environment (optional but recommended)
```
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
```
- 3️⃣ Install dependencies
```
pip install -r requirements.txt
```
- 4️⃣ Configure your database
Create the MySQL database:

```
CREATE DATABASE library_db;

CREATE USER 'rp32'@'localhost' IDENTIFIED BY 'Strong@123';
GRANT ALL PRIVILEGES ON library_db.* TO 'rp32'@'localhost';
FLUSH PRIVILEGES;
```
  - Update config.py if your user/password differs:
```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://rp32:Strong@123@localhost/library_db'
```
- 5️⃣ Run the app
```
python app.py
Visit http://localhost:5000
```
--------

## ✨ How to Use
1. Add Books: Use the “Add Book” form.
2. Import Books: Use the “Import Books” form to fetch books from the Frappe API.
3. Manage Members: Add new members or remove them.
4. Issue Books: Issue books to members (checks stock & debt).
5. Return Books: Return books and add fees.
-----------
## Screen Short

<img width="914" height="918" alt="Screenshot From 2025-07-15 17-46-25" src="https://github.com/user-attachments/assets/88d55bb2-1e77-40bb-8fac-a66e583b7115" />

-------

<img width="914" height="452" alt="Screenshot From 2025-07-15 17-47-06" src="https://github.com/user-attachments/assets/62e24409-e110-4cab-9bdc-e9f5cf5e0c7e" />

-----

<img width="914" height="452" alt="Screenshot From 2025-07-15 17-48-00" src="https://github.com/user-attachments/assets/e723c5b0-83bd-4969-87b2-5c42b398f573" />


------------

📃 License
This project is open-source. Use it for learning or adapt it for your own needs!

---------------------------------

✏️ Author
📧 Your Name
💻 Your GitHub Username

Happy coding! 🚀📚
