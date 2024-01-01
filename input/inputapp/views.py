from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
def print(request):
    # if request=="POST":
    #     username=request.POST['username']
    #     password=request.POST['password']
    #     user=authenticate(username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         return HttpResponse("login")
            
    return render(request,'index.html')
# Create your views here.
def registeration(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        return redirect("loging")
    
    return render(request,'regestertion.html')
def home(request):
    return render(request,'home.html')