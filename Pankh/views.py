from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from courses.models import Course, Video


def home(request):
    return render(request, "index.html")


def Courses(request):
    courses = Course.objects.all()

    # print("cour/sses : ", courses[0].slug)
    for course in courses:
        print(course.name)
        print(course.slug)
        # print(course)
    slug1 = courses[0].slug
    context = {
        "courses": courses,
    }
    # print("slug1 is : ", slug1)
    # courses=Course.objects.get()[:2]
    # for ele in courses[1]:
    #     print(ele)
    return render(request, "Courses.html", context=context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def blogs(request):
    return render(request, "blogs.html")
