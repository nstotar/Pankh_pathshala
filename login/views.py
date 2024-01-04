from django.core.checks import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


# def SignupPage(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#
#         if pass1 != pass2:
#             return HttpResponse("Your password and confrom password are not Same!!")
#         else:
#
#             my_user = User.objects.create_user(uname, email, pass1)
#             my_user.save()
#             return redirect('login')
#
#     return render(request, 'signup.html')


# def LoginPage(request):
#     if request.method == 'post':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             request.session['username'] = user.username
#
#             return redirect('Courses')
#         else:
#             messages.error(request, 'Invalid login credentials.')
#             return redirect("/login/")
#
#     return render(request, 'login.html')
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            # request.session['email']=authenticate.email
            return redirect('Courses')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect("/login/")

    return render(request, 'login.html')


from django.contrib.auth import logout
from django.shortcuts import redirect



def signout(request ):
    logout(request)
    return redirect("index")