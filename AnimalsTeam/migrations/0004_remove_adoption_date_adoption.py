# Generated by Django 3.2.12 on 2022-03-17 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AnimalsTeam', '0003_auto_20220313_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoption',
            name='date_adoption',
        ),
    ]
