# Generated by Django 4.1.3 on 2022-12-02 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0019_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseoutline',
            old_name='Assesment',
            new_name='assesment',
        ),
        migrations.RenameField(
            model_name='courseoutline',
            old_name='ContactHour',
            new_name='contactHour',
        ),
        migrations.RenameField(
            model_name='courseoutline',
            old_name='Credit',
            new_name='credit',
        ),
        migrations.RenameField(
            model_name='courseoutline',
            old_name='Duration',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='courseoutline',
            old_name='Grading',
            new_name='grading',
        ),
    ]
