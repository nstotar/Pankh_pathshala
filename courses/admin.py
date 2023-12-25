from django.contrib import admin

# Register your models here.
from django.contrib import admin
from courses.models import Course,Video
from django.utils.html import format_html


# Register your models here.
admin.site.register(Video)
admin.site.register(Course)
# class VideoAdmin(admin.TabularInline):
#     model = Video
