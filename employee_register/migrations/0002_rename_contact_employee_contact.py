# Generated by Django 4.0.3 on 2022-03-07 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Contact',
            new_name='contact',
        ),
    ]
