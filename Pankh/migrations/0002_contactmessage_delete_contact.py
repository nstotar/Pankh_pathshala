# Generated by Django 5.0 on 2024-01-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pankh', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
