# Generated by Django 3.1.4 on 2020-12-30 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0004_auto_20201230_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applicant_details',
            old_name='year_of_experiene',
            new_name='years_of_experience',
        ),
    ]
