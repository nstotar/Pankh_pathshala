
from django.urls import path
from login import views
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.home, name='index'),
    path('Courses/', views.Courses, name='Courses'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blogs/', views.blogs, name='blogs'),
    # path('login/', views.login, name='login'),
    path('logout/', RedirectView.as_view(url='/admin/logout/')),

    path('contact_view/', views.contact_view, name='contact_view'),
    # Add other URLs as needed

    # path('login/', views.LoginPage, name='login'),


]