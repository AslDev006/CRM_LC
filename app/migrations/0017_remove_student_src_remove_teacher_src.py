# Generated by Django 4.1.9 on 2023-07-22 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='src',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='src',
        ),
    ]
