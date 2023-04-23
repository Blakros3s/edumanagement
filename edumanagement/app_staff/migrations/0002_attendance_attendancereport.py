# Generated by Django 4.1.7 on 2023-04-22 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hod', '0010_studentnotification'),
        ('app_staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_data', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_hod.subject')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_staff.attendance')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app_hod.student')),
            ],
        ),
    ]
