# Generated by Django 5.1.3 on 2024-11-24 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_safetylesson_description_safetylesson_duration_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('video_url', models.URLField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='SafetyLesson',
        ),
    ]