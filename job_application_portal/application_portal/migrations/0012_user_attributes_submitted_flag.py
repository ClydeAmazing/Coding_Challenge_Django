# Generated by Django 3.1.4 on 2021-01-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0011_auto_20210101_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_attributes',
            name='submitted_flag',
            field=models.BooleanField(default=False),
        ),
    ]
