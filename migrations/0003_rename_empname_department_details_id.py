# Generated by Django 4.0.6 on 2022-07-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flexibeetask', '0002_department_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department_details',
            old_name='empname',
            new_name='Id',
        ),
    ]
