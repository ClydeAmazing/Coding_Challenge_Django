# Generated by Django 3.1.4 on 2021-01-03 17:27

import application_portal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0015_auto_20210103_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application_attachment',
            name='attachment_file',
            field=models.FileField(blank=True, null=True, upload_to=application_portal.models.user_attachment_path, verbose_name='File'),
        ),
    ]
