from django.shortcuts import render,redirect
from .models import Blogs
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    blog=Blogs.objects.all()
    return render(request,'home.html',{'blog':blog})

def add(request):
    return render(request,'addblog.html')

def addct(request):
    x=request.POST['title']
    y=request.POST['content']
    z=request.FILES.get('image')
    blog=Blogs(title=x,content=y,image=z)
    blog.save()
    return redirect("/")

def sign(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['apassword']
        user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
        user.save()
        return redirect('login')
    else:
        return render(request,'sign.html')

def login(request):
    if request.method=='POST':
        user_name=request.POST['uname']
        password=request.POST['password']

        user=auth.authenticate(username=user_name,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')