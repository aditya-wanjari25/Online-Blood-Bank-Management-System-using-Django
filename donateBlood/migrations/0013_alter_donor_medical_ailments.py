# Generated by Django 3.2.7 on 2021-10-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donateBlood', '0012_donor_medical_ailments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='medical_ailments',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
