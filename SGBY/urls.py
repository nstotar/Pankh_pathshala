"""
URL configuration for SGBY project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views
from courses.views import coursePage, coursePage2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginPage, name='login'),
    path('', include('Pankh.urls')),
    path('', include('courses.urls')),
    path('signout/', views.signout, name='signout'),
    # path('Courses/class1/class1_videos',coursePage,name='class/class1'),
    # path('Courses/class1/{',coursePage2,name='class/class2'),
    # path('Courses/cp/',coursePage2,name='class/cp')
]
admin.site.site_header="PankhPatashala Admin panel"
admin.site.index_title="Welcome To admin PankhPatashala"