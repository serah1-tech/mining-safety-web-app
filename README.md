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

**Provide user-friendly web interfaces for each feature.**
Tools & Technologies
Backend: Django Framework (Python)
Database: MySQL
Frontend: Django Templates, HTML, CSS, and Bootstrap
Environment: Python Virtual Environment
Version Control: Git
Steps to Build the System
**Step 1: Install Required Tools**
Install Python, MySQL, and pip (Python package manager).
Set up Django and MySQL libraries.
**Step 2: Create a New Django Project**
Start the Django project (mining_safety_project).
**Step 3: Set Up MySQL Database**
Configure Django to use a MySQL database instead of the default SQLite.
**Step 4: Create Apps**
Create two Django apps:
education for safety lessons.
hazards for hazard alerts.
**Step 5: Define Models**
For education, define a SafetyLesson model (title, content, video URL).
For hazards, define a HazardAlert model (location, description, timestamp).
**Step 6: Create Views**
For each app, create views to display lists of safety lessons and hazard alerts.
**Step 7: Add URLs**
Add URLs for both apps and connect them to the project’s main URLs.
**Step 8: Design Templates**
Build user-friendly HTML templates for displaying safety lessons and hazard alerts.
**Step 9: Add Authentication**
Use Django’s built-in authentication system to allow user login and registration.
**Step 10: Deploy & Test**
Test the entire system locally.
Deploy the project to a web server if needed.
**What I am  Using?**
Django: To manage backend logic and connect the database.
MySQL: To store and retrieve data.
HTML, CSS, Bootstrap: To design user-friendly interfaces.
Git: For version control, allowing you to track changes in your code.




