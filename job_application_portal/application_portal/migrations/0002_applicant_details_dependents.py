# Generated by Django 3.1.4 on 2020-12-30 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant_details',
            name='dependents',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]