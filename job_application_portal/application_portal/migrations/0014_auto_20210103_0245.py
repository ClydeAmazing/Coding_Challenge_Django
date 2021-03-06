# Generated by Django 3.1.4 on 2021-01-02 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0013_auto_20210103_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_details',
            name='dependents',
            field=models.IntegerField(blank=True, null=True, verbose_name='No. of Dependents'),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='years_of_experience',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
