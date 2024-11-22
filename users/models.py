from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)  # Matches 'username' in MySQL
    email = models.EmailField(unique=True)  # Matches 'email' in MySQL
    password = models.CharField(max_length=255)  # Matches 'password_hash' in MySQL
    full_name = models.CharField(max_length=255, blank=True)  # Matches 'full_name' in MySQL
    role = models.CharField(max_length=10, choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Manager', 'Manager')], default='Employee')  # Matches 'role' in MySQL
    date_joined = models.DateTimeField(auto_now_add=True)  # Matches 'created_at' in MySQL
    last_login = models.DateTimeField(auto_now=True)  # You may not have this in MySQL, but it’s useful for tracking logins

    def __str__(self):
        return self.username
