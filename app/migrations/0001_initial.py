# Generated by Django 4.1.7 on 2023-02-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignupCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='yourname', max_length=30)),
                ('email', models.EmailField(default='email@yahoo.com', max_length=254)),
                ('course', models.CharField(choices=[('Python', 'Python'), ('Html', 'Html'), ('React', 'React'), ('Analysis', 'Analysis'), ('Data Science', 'Data Science'), ('Django', 'Django')], max_length=20)),
            ],
            options={
                'unique_together': {('email', 'course')},
            },
        ),
    ]