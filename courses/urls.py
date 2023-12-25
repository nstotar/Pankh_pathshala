from django.contrib import admin
from django.urls import path, include
from courses.views import coursePage, coursePage2
from django.conf.urls.static import static
from django.conf import settings
from courses.models import Course
# urls.py

from django.urls import path

from . import views
from .views import coursePage2  # Make sure to import the correct view function

urlpatterns = [

                  path('Courses/<str:slug>', coursePage2, name='class2'),
                  # path('Courses/cp', coursePage2, name='class2'),
                  # path('/cp', coursePage2, name='class2'),
                  # path('Courses/cp/<slug:str>/', views.coursePage2, name='course_page2'),

                  # path('course/cp/<str:slug>', coursePage2, name='cp'),
                  path('course/cp', coursePage, name='cp'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
