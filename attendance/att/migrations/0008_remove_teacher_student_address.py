# Generated by Django 5.0 on 2023-12-15 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('att', '0007_remove_classroom_classname_classroom_program_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='student_address',
        ),
    ]
