# Generated by Django 3.2.9 on 2022-04-27 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
                ('salary', models.FloatField(max_length=20)),
                ('image', models.FileField(upload_to='')),
                ('description', models.CharField(max_length=300)),
                ('experience', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('creationdate', models.DateTimeField(auto_now_add=True)),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.recruiter')),
            ],
        ),
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.studentuser')),
            ],
        ),
    ]
