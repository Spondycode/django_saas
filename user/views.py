from django.shortcuts import render, redirect 
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout   

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/course")
    else:
        form = CustomUserCreationForm()
    context = {
        "form": form
    }  
    return render(request, "registration/register.html", context)

    
# def login(request):
#     if request.method == "POST":
#         pass
#     else:
#         return render(request, "user/login.html")


