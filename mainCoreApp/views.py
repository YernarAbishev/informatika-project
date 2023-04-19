from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm
from .models import *
from django.db.models import Q  # New

def homePage(request):
    return render(request, "core/home.html")

def courses(request, slug=None):
    category = None
    categories = Category.objects.all()
    searchData = request.GET.get('search')
    if searchData:
        courses = Course.objects.filter(Q(courseName__icontains=searchData) | Q(courseDescription__icontains=searchData))
    else:
        courses = Course.objects.all().order_by('-postDate')
    if slug:
        category = get_object_or_404(Category, slug=slug)
        courses = courses.filter(category=category)

    return render(request, "core/courses.html", {
        'courses': courses,
        'categories': categories,
        'category': category
    })

def courseDetail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, "core/course-detail.html", {
        'course': course,
    })

def lessonsList(request, slug=None):
    course = get_object_or_404(Course, slug=slug)
    lessons = Lesson.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        lessons = lessons.filter(course=course)
    return render(request, "core/lessons.html", {
        'course': course,
        'lessons': lessons
    })

def lessonDetail(request, slug, pk):
    course = get_object_or_404(Course, slug=slug)
    lesson = get_object_or_404(Lesson, pk=pk)
    lessons = Lesson.objects.all()
    if slug:
        lessons = lessons.filter(course=course)
    return render(request, "core/lesson-detail.html", {
        'course': course,
        'lesson': lesson,
        'lessons': lessons,
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Тіркелу сәтті өтті!")
            return redirect("homePage")
        messages.error(request, "Тіркелу барысында қателіктер пайда болды")
    else:
        form = NewUserForm()
    return render(request, "user/sign-up.html", {
        'form': form
    })

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Қош келдіңіз, {username}!")
                return redirect("homePage")
            else:
                messages.error(request, "Логин немесе пароль қате.")
        else:
            messages.error(request, "Логин немесе пароль қате.")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Сіз платформадан сәтті шықтыңыз.")
    return redirect("homePage")