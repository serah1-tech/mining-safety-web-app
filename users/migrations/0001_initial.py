# Generated by Django 5.1.3 on 2024-11-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('role', models.CharField(choices=[('Admin', 'Admin'), ('Employee', 'Employee'), ('Manager', 'Manager')], default='Employee', max_length=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
