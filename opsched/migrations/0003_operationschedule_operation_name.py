# Generated by Django 2.2.8 on 2019-12-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opsched', '0002_auto_20191208_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationschedule',
            name='operation_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]