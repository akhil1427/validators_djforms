# Generated by Django 4.2.6 on 2024-01-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='school',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sname', models.CharField(max_length=100)),
                ('Sprinc', models.CharField(max_length=100)),
                ('Sloc', models.CharField(max_length=100)),
                ('Semail', models.EmailField(max_length=254)),
                ('re', models.EmailField(max_length=254)),
            ],
        ),
    ]
