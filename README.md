# mining-safety-web-app
A web platform for small-scale miners to report hazards, view geo-hazard maps, and access safety resources.

This is the link to the project's pitch a deck https://gamma.app/docs/Project-Name-Small-Scale-Mining-Safety-Awareness-Web-App-po194dlyhrzs1oz

**Overview**
This project is a Django-based web application designed to provide and manage Mining Safety Tips. The app allows users to view, add, and manage safety tips related to mining operations. The project aims to improve safety awareness by providing easily accessible tips that can be used by mining professionals.

**The app has been set up , and the initial configuration includes the following:**

Django Project Initialization
Creation of the Safety Tips App
Setup of Views, URLs, and Static Files for the app
Basic Admin Interface Integration
Database Model Setup for Safety Tips
**Features Implemented **
1. Django Project Initialization
A new Django project was created using the command:
bash
Copy code
django-admin startproject mining_safety
The project was set up with the following structure:
mining_safety/ - The main project directory.
mining_safety/manage.py - The management script for Django operations.
mining_safety/mining_safety/ - Configuration and settings for the project.
2. Safety Tips App
A new Django app called safety_tips was created using the command:
bash
Copy code
python manage.py startapp safety_tips
The app was registered in the INSTALLED_APPS section of the project’s settings file (mining_safety/mining_safety/settings.py).
3. Database Model for Safety Tips
A model was created in the safety_tips/models.py file with the following fields:
name (CharField): Name of the safety tip.
description (TextField): Detailed description of the safety tip.
The model allows for the storing of safety tips in the SQLite database.
4. Admin Interface
Registered the SafetyTip model with the Django admin interface so that safety tips can be added and managed directly from the Django admin page.
5. Views & URLs
A basic view was created to display a welcome message:
python
Copy code
def home(request):
    return HttpResponse("Welcome to the Mining Safety Tips App!")
A new URL configuration file (safety_tips/urls.py) was created to define the routes for the app.
The URLs for the app were included in the main project’s URL configuration (mining_safety/urls.py).
6. Static Files Setup
Created a static folder inside the safety_tips app for storing static files such as CSS, JS, and images. This folder is used for styling and enhancing the frontend of the application.
The app currently uses a basic view, but future improvements will include applying custom styling using the static CSS files.
7. Migrations
Django's migration system was used to create and apply migrations for the SafetyTip model, which ensured that the database schema matches the defined models.
The following commands were used:
bash
Copy code
python manage.py makemigrations
python manage.py migrate
8. Testing the App
Ran the development server to test the project:
bash
Copy code
python manage.py runserver
Accessed the app in the browser at http://127.0.0.1:8000/ and confirmed the basic functionality.
How to Run the Project Locally
Follow these steps to set up and run the project locally on your machine:

1. Clone the Repository
If you haven’t already cloned the repository, do so by running:

bash
Copy code
git clone https://github.com/serah1-tech/mining-safety-web-app.git
2. Install Dependencies
Make sure you have Python 3.12 installed. If not, download and install Python 3.12.

Create a virtual environment (if you haven’t already):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows:
bash
Copy code
.\venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install required dependencies:

bash
Copy code
pip install -r requirements.txt
3. Run Migrations
Run the following commands to apply the migrations to your database:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
4. Create a Superuser (Optional)
If you want to access the Django admin panel to manage safety tips, you can create a superuser:

bash
Copy code
python manage.py createsuperuser
Follow the prompts to set up the superuser credentials.

5. Run the Development Server
Start the server:


Next Steps
Enhance the UI: Add custom CSS to improve the visual appeal of the app.
Add More Functionality: Implement CRUD functionality to allow users to create, update, and delete safety tips.
Database Integration: Expand the database to handle more data related to mining safety.
Deploy the App: Deploy the app to a cloud server for public access (e.g., Heroku, AWS).
Technologies Used
Python 3.12
Django 5.1.3 (Web Framework)
SQLite (Database)
HTML, CSS (Frontend Styling)
License
This project is open-source and available under the MIT License. See the LICENSE file for more details.
