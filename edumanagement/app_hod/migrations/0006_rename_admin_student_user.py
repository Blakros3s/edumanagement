# Generated by Django 4.1.7 on 2023-04-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_hod', '0005_remove_student_doj_student_enrollment_year_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='admin',
            new_name='user',
        ),
    ]
