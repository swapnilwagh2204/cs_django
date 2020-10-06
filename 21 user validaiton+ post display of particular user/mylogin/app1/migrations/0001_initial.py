# Generated by Django 3.1.1 on 2020-10-06 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20, unique=True)),
                ('Password', models.CharField(max_length=10)),
                ('Fullname', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Address', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='postt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_by', models.CharField(max_length=100)),
                ('cr_date', models.DateTimeField(auto_now_add=True)),
                ('overview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.users')),
            ],
        ),
    ]
