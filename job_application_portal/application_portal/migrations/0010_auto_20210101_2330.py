# Generated by Django 3.1.4 on 2021-01-01 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0009_auto_20210101_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant_education',
            old_name='degree_title',
            new_name='degree',
        ),
    ]
