# Generated by Django 3.0.2 on 2020-01-16 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_auto_20200116_1944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='ex_type',
            new_name='category',
        ),
    ]
