# Generated by Django 3.0.2 on 2020-01-16 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('muscle_group', models.CharField(max_length=50)),
                ('ex_type', models.CharField(max_length=50)),
                ('equipment', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('youtube', models.URLField()),
                ('img', models.ImageField(upload_to='')),
                ('weight', models.IntegerField(blank=True)),
                ('reps', models.IntegerField(blank=True)),
            ],
        ),
    ]
