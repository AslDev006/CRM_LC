# Generated by Django 4.1.9 on 2023-07-21 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_payment_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
