# Generated by Django 4.1.9 on 2023-07-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_remove_student_password_remove_student_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='when',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
