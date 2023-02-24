from django.urls import path, include
from .views import Home, Courses, events,data, frontend, python, science,react, Business, Django


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("course/", Courses.as_view(), name="signup"),
    path('django/', Django.as_view(), name='django'),
    path('data/', data, name='data'),
    path('python/', python, name='python'),
    path('science/', science, name='science'),
    path('react/', react, name='react'),
    path('frontend/', frontend, name='frontend'),
    
    
    path('events/', events, name="events"),
    path('business/', Business.as_view(), name="business"),

]
