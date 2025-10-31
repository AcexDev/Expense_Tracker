# 💰 Expense Tracker

A modular **Python expense tracking system** built with **MySQL (Aiven-hosted)** for persistent data storage.  
Designed to be lightweight, easy to maintain, and structured like a real-world backend app.

---

## 🚀 Features
- 🧾 Add, view, and categorize expenses
- 👤 User registration & login system
- 🔐 Password hashing and authentication logic
- 🧮 Expense categorization by user
- 🗄️ SQL schema-based database setup
- 🌐 Deployment-ready structure (`Procfile` included)

> Built by AcexDev — learning by building, one project at a time.

---

## 🛠️ Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <project-folder>
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
Dependencies include:
bcrypt, colorama, mysql-connector-python, python-dotenv, tabulate, etc.

3. Configure environment variables
Create a .env file in the project root:

env
Copy code
DB_HOST=your_db_host
DB_USER=your_db_user
DB_PASS=your_db_password
DB_NAME=your_db_name
⚠️ Make sure these credentials match your MySQL database. The app will not run 
without them.

🏃 Running the app
bash
Copy code
python main.py
Note: Free Replit demos may show previous user data due to caching. Running locally 
ensures a fresh start.

📝 Usage Notes
Users must define at least one category before adding expenses.

The app will prompt you to create categories first if none exist.

Main Menu
==============================
     FINANCE TRACKER MENU     
==============================
Welcome <username>!

[1] Category Options 
[2] Expense Options
[3] Reports/Analytics (In development)
[4] Settings 
[0] Logout
Enter choice:

Category Options
-----------------------------
       CATEGORY OPTIONS       
-----------------------------
[1] View All Categories 
[2] Add New Category
[3] Delete Category 
[0] Back to Main Menu
Enter choice:

Expense Options
------------------------------
       EXPENSE OPTIONS        
------------------------------
⚠️ No categories found! Please create categories first via Category Options.
[1] Add New Expense 
[2] View All Expenses 
[3] Filter by Category
[4] Filter by Date 
[5] Total for a Month 
[0] Back to Main Menu
Enter Choice:

📦 Deployment

The project includes a Procfile for deployment on platforms like Railway or Heroku.

Make sure environment variables are set in your host’s secret manager.