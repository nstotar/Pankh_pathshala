from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
# models.py
from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class Blogs(models.Model):
    name = models.CharField(max_length=100)
    content = RichTextField(config_name='awesome_ckeditor')
    def __str__(self):
        return self.content
