# Generated by Django 3.1.1 on 2020-10-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostsApp', '0003_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]