# Generated by Django 5.0 on 2023-12-15 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att', '0008_remove_teacher_student_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_address',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
