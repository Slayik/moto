# Generated by Django 5.1.4 on 2025-01-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callback', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='callbackrequest',
            name='email',
        ),
        migrations.AlterField(
            model_name='callbackrequest',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
