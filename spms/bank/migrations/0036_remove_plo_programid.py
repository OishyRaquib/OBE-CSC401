# Generated by Django 4.1.3 on 2022-12-06 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0035_courseoutline_course_descrip_courseoutline_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plo',
            name='ProgramID',
        ),
    ]