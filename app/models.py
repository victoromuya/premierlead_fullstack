from django.db import models

class SignupCourses(models.Model):
    
    COURSE_CHOICES=(
    ('Python','Python'),
    ('HTML/CSS','HTML/CSS'),
    ('Reactjs', 'Reactjs'),
    ('Data Analysis', 'Data Analysis'),
    ('Data Science', 'Data Science'),
    ('Python Web', 'Python Web')
    
)
    
    def __str__(self):
        return self.name +" " +self.course
    
    name = models.CharField(default="yourname", max_length=30)
    email = models.EmailField(default="email@yahoo.com")
    course = models.CharField(choices=COURSE_CHOICES, max_length=20)  
    
    class Meta:
        unique_together = ["email", "course"]
        