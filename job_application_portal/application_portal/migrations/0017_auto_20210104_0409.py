# Generated by Django 3.1.4 on 2021-01-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_portal', '0016_auto_20210104_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_attributes',
            name='confirmation_token',
            field=models.UUIDField(editable=False),
        ),
    ]
