# Generated by Django 5.0 on 2023-12-15 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('att', '0006_student_image_teacher_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='classname',
        ),
        migrations.AddField(
            model_name='classroom',
            name='program',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='classroom',
            name='year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='class_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
