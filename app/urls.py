from django.urls import path, include
from .views import Home, Courses, events, Business, Django


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("course/", Courses.as_view(), name="signup"),
    path('django/', Django.as_view(), name='django'),
    
    path('events/', events, name="events" ),
    path('business/', Business.as_view(), name="business" ),
    
    
]
