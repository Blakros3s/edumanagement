# Generated by Django 4.1.7 on 2023-04-18 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_hod', '0004_rename_title_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='doj',
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_year',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.DeleteModel(
            name='EnrollmentYear',
        ),
    ]
