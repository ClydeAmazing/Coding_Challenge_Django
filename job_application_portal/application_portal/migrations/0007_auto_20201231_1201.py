# Generated by Django 3.1.4 on 2020-12-31 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0006_auto_20201230_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant_details',
            name='country',
            field=models.CharField(max_length=100, verbose_name='Country of Residence'),
        ),
        migrations.AlterField(
            model_name='applicant_details',
            name='dependents',
            field=models.IntegerField(blank=True, null=True, verbose_name='No. of Dependents'),
        ),
    ]
