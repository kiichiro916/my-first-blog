# Generated by Django 2.2.8 on 2019-12-08 10:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperationSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_id', models.CharField(max_length=255)),
                ('operation_name', models.CharField(max_length=255)),
                ('patient_name', models.CharField(max_length=20)),
                ('operation_start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('operation_finish_estimation_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('file_path', models.FilePathField(null=True, path='/')),
            ],
        ),
    ]
