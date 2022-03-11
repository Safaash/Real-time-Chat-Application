from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignupForm

# Home Page
def home(request):
    return render(request,'home/home.html')

# Signup Page
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            print("success")
            login(request,user)
          
            return redirect('home')
    else:
        form=SignupForm()
    context={
        'form':form
    }
    return render(request,'home/signup.html',context)