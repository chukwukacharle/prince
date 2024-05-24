from django.shortcuts import render
from .models import Home
from .forms import Post_Form
# Create your views here.


def login(request):
    age = 20
    context ={
        'age' : age 
        }
    return render(request,('SchoolWeb/login.html',context))

def home(request):
    return render(request,('SchoolWeb/home.html')) 

def courses(request):
    return render(request,('SchoolWeb/courses.html')) 

def feedback(request):
    return render(request,('SchoolWeb/feedback.html')) 

def data(request):
    datas = Home.objects.all()
    return render(request,'SchoolWeb/data.html',{'datas':datas}) 

def post(request):
    datas = Home.objects.all()
    return render(request,'SchoolWeb/post.html',{'datas':datas}) 
def addpost(request):
    if request.method == 'POST':
        form = Post_Form(request.POST)
        if form.is_valid():
            new_author =form.cleaned_data['Login_home']
            new_courses =form.cleaned_data['Courses']
            new_feedback =form.cleaned_data['Feedback']
    
    
    
        cleaned_post= Home(
            Login_home=new_author,
            Courses=new_courses,
            Feedback=new_feedback,
        )
        cleaned_post.save()
        return render(request,'SchoolWeb/addpost.html',{'form':Post_Form()}) 
    else:
        form = Post_Form()
        return render(request,'SchoolWeb/addpost.html',{
        'form':Post_Form()
        })
        
    
