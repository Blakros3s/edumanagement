# Generated by Django 4.1.7 on 2023-04-19 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_hod', '0007_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subject_id', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hod.course')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_hod.staff')),
            ],
        ),
    ]
