# Generated by Django 3.1.1 on 2020-10-05 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_auto_20201005_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]