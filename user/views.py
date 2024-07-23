from django.shortcuts import render, HttpResponse, redirect
from user import forms as user_form
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from user import models as user_model
from chatroom import models as chatroom_model
from django.db.models import Count
# Create your views here.

def home(request):
    featuringrooms = chatroom_model.Room.objects.annotate(num_users=Count('ruser')).filter(num_users__gt=0)[:3]
    if request.user.is_authenticated:
        collegerooms = chatroom_model.Room.objects.filter(rcollege=request.user.ucollege)[:3]
        courserooms = chatroom_model.Room.objects.filter(rcourse=request.user.ucourse)[:3]
        context = {
            'collegerooms':collegerooms,
            'courserooms':courserooms,
            'featuringrooms':featuringrooms,
        }
    else:
        context = {
            'featuringrooms':featuringrooms
        }
    return render(request, "user/home.html", context)

def registeruser(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = user_form.CreateUserForm()
    college = user_model.Usercollege.objects.filter(is_approved=True)
    course = user_model.Usercourse.objects.filter(is_approved=True)

    if request.method=="POST":
        form = user_form.CreateUserForm(request.POST)
        if form.is_valid():
            form.instance.email = form.cleaned_data.get('username')
            form.instance.username = form.cleaned_data.get('username').split('@')[0]
            form.save()
            messages.success(request, f"Account has been Created for {form.cleaned_data.get('username')}")
            return redirect('login')
            
    context={
        "form":form,
        "colleges":college,
        "courses":course,
    }
    return render(request, "user/register.html", context=context)

def loginuser(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method=="POST":
        username = request.POST.get('username').split('@')[0]
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
    
    return render(request, "user/login.html")

def logoutuser(request):
    logout(request)
    return redirect('login')


def addcollege(request):

    form = user_form.Addcollegeform()

    if request.method == "POST":
        form = user_form.Addcollegeform(request.POST)
        try:
            user_model.Usercollege.objects.get(college=request.POST.get('college').upper())
            messages.info(request, "College already exists.")
        except  Exception as e:
            if form.is_valid():
                form.instance.college = form.cleaned_data['college'].upper()
                form.instance.is_approved = True
                form.save()
                messages.success(request, "College added successfully")

        return redirect('register')
    context = {
        'form':form
    }

    return render(request, "user/addcollege.html", context)

def addcourse(request):

    form = user_form.Addcourseform()

    if request.method == "POST":
        form = user_form.Addcourseform(request.POST)
        try:
            user_model.Usercourse.objects.get(course=request.POST.get('course').upper())
            messages.info(request, "Course already exists.")
        except  Exception as e:
            if form.is_valid():
                form.instance.course = form.cleaned_data['course'].upper()
                form.instance.is_approved = True
                form.save()
                messages.success(request, "Course added successfully")

        return redirect('register')
    context = {
        'form':form
    }

    return render(request, "user/addcollege.html", context)