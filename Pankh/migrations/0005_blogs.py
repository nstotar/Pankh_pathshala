# Generated by Django 5.0 on 2024-01-23 16:33

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pankh', '0004_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
