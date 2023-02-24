from django.forms import ModelForm
from .models import SignupCourses

class CourseForm(ModelForm):
    class Meta:
        model=SignupCourses
        fields=['name', 'email', 'course']