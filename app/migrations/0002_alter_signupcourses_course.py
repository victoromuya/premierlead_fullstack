# Generated by Django 4.1.7 on 2023-02-23 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupcourses',
            name='course',
            field=models.CharField(choices=[('Python', 'Python'), ('Html', 'Html'), ('React', 'React'), ('Data Analysis', 'Data Analysis'), ('Data Science', 'Data Science'), ('Python Web', 'Python Web')], max_length=20),
        ),
    ]
