from django.urls import path
from .import views

app_name = 'school'
urlpatterns = [
    path('',views.login, name='login'),
    path('home/',views.home, name='home'), 
    path('courses/',views.courses, name='courses'), 
    path('feedback/',views.feedback, name='feedback'),  
    path('post/',views.post, name='post'),  
    path('data/',views.data, name='data'),  
    path('addpost/',views.addpost, name='addpost'),   
]
