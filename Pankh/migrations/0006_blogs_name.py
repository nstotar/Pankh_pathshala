# Generated by Django 5.0 on 2024-01-23 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pankh', '0005_blogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='name',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
