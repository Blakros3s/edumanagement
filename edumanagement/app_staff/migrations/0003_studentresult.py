# Generated by Django 4.1.7 on 2023-04-24 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hod', '0010_studentnotification'),
        ('app_staff', '0002_attendance_attendancereport'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('assignment_marks', models.IntegerField()),
                ('exam_marks', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hod.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hod.subject')),
            ],
        ),
    ]