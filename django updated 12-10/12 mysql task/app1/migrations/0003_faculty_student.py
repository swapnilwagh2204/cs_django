# Generated by Django 3.1.1 on 2020-09-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_employees_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('specialisation', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rollno', models.IntegerField()),
                ('marks', models.FloatField()),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
