# Generated by Django 3.1.1 on 2020-09-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_faculty_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='just',
            field=models.FloatField(default=1000),
        ),
    ]
