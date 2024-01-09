from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from Pankh.models import *
from django.utils.html import format_html


# Register your models here.
@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
    search_fields = ('name', 'email')