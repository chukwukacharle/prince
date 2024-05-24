from django.db import models

# Create your models here.

class Home(models.Model):
    Login_home = models.CharField(max_length = 50)
    Courses = models.CharField(max_length = 50)
    Feedback = models.TextField()
    Image = models.ImageField(upload_to='images/', default='image/IMG3.JPG')
    
    def __str__(self):
        return self.Login_home

