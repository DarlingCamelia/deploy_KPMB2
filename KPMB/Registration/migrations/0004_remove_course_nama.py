# Generated by Django 4.0.5 on 2024-04-19 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='nama',
        ),
    ]
