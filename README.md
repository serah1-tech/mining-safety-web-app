# mining-safety-web-app
A web platform for small-scale miners to report hazards, view geo-hazard maps, and access safety resources.

This is the link to the project's pitch a deck https://gamma.app/docs/Project-Name-Small-Scale-Mining-Safety-Awareness-Web-App-po194dlyhrzs1oz

**Overview**
This project is a Django-based web application designed to provide and manage Mining Safety Tips. The app allows users to view, add, and manage safety tips related to mining operations. The project aims to improve safety awareness by providing easily accessible tips that can be used by mining professionals.
**Objective**
I am building a Mining Safety Management System using Django as the backend and MySQL as the database. The system will have the following features:

Safety Education

Provide safety lessons (with text and optional videos).
Hazard Alerts

Allow users to view hazard alerts related to mining operations.
User Management

Enable user registration, login, and authentication.
Data Management

Store and retrieve data efficiently using MySQL.
Frontend Templates

**Steps to Build the System**
Install Required Tools

Install Python, MySQL, and pip (Python package manager).
Set up Django and MySQL libraries.
Create a New Django Project

Start the Django project (mining_safety_project).
Set Up MySQL Database

Configure Django to use a MySQL database instead of the default SQLite.
Create Apps

Create two Django apps:
education for safety lessons.
hazards for hazard alerts.
Define Models

For education, define a SafetyLesson model (title, content, video URL).
For hazards, define a HazardAlert model (location, description, timestamp).
Create Views

For each app, create views to display lists of safety lessons and hazard alerts.
Add URLs

Add URLs for both apps and connect them to the project’s main URLs.
Design Templates

Build user-friendly HTML templates for displaying safety lessons and hazard alerts.
Add Authentication

Use Django’s built-in authentication system to allow user login and registration.
Deploy & Test

Test the entire system locally.
Deploy the project to a web server if needed.
Installation Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/mining-safety-web-app.git
Navigate into the project directory:

bash
Copy code
cd mining-safety-web-app
Set up a virtual environment:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On Mac/Linux:
bash
Copy code
source venv/bin/activate
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Make sure MySQL is installed and configured, then apply the migrations:
bash
Copy code
python manage.py migrate
Run the application:

bash
Copy code
python manage.py runserver
Access the app in your browser at http://127.0.0.1:8000.

Project Status
Currently in development.
Features still to be added: (e.g., Geo-hazard map integration, advanced user management, etc.)
Contributing
We welcome contributions to improve the project! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch for your feature or bugfix:
bash
Copy code
git checkout -b feature-branch
Make your changes and commit them:
bash
Copy code
git commit -m "Description of changes"
Push to the branch:
bash
Copy code
git push origin feature-branch
Open a pull request.

