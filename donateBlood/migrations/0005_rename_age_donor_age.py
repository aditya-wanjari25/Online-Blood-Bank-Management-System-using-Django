# Generated by Django 3.2.7 on 2021-10-19 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donateBlood', '0004_auto_20211019_1522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='Age',
            new_name='age',
        ),
    ]
