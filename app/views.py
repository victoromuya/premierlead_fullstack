from django.shortcuts import render
from django.views import View
from .models import SignupCourses
from .forms import CourseForm
from  django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string

class Home(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'index.html')
    
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            print(name, email, phone, subject, message)
            
            html = render_to_string('email.html', {
            'name' : name,
            'email' : email,
            'content' : message
        })
        
        send_mail(subject, message, "viczik16@gmail.com", ["victor_zik@yahoo.com"], html_message=html)
        
        return render(request, 'index.html')
    
class Courses(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'signup.html')


class Django(View):
    def get(self, request, *args, **kwargs ):
        form = CourseForm()
        return render(request, 'django.html', {'form' : form})
    
    def post(self, request, *args, **kwargs):
        form = CourseForm(request.POST or None)
        
        if form.is_valid():
            
            Course = SignupCourses.objects.create(**form.cleaned_data)
            if Course:
                messages.success(request, 'Signup successful, you will recieve a mail for validation!')
        
        context = {
            'form':form
        }
        return render(request, 'django.html', context)
    

def frontend(request):
    return render(request, 'basic-fronthend.html')

def science(request):
    return render(request, 'data-science.html')

def data(request):
    return render(request, 'data-analysis.html')

def python(request):
    return render(request, 'python.html')

def react(request):
    return render(request, 'react.html')


class Business(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'bs.html')
    
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            print(name, email, phone, subject, message)
            
            html = render_to_string('email.html', {
            'name' : name,
            'email' : email,
            'content' : message
        })
        
        send_mail(subject, message, "viczik16@gmail.com", ["victor_zik@yahoo.com"], html_message=html)
        
        return render(request, 'bs.html')
    

def events(request):
    return render(request, 'events.html')
                
        