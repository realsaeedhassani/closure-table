# Generated by Django 4.0.3 on 2022-04-05 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Edge',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
    ]
