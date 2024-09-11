from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout as new_logout

# Create your views here.
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        con_passsword=request.POST['conform_password']
        if password != con_passsword:
            messages.error(request,"password is not same incorrect")
            return redirect('signup')

        try:
            if User.objects.get(username=email):
                messages.error(request,"email alredy exist")
                return redirect('signup')
        except:
            pass
        user=User.objects.create_user(email,email,password)
        user.save()
        messages.info(request,"user created")
    return render(request,'eapp/signin/signin.html')

def login_views(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request,"please sign up")

    return render (request,'eapp/signin/login.html')
def logout(request):
    new_logout(request)
    return redirect('signin')

def pandi(pandis):
    return render(pandis,"eapp/pandi.html")