# Generated by Django 4.2 on 2023-04-06 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='login',
        ),
        migrations.DeleteModel(
            name='register',
        ),
    ]