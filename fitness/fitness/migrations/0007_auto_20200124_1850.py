# Generated by Django 3.0.2 on 2020-01-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0006_auto_20200117_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
