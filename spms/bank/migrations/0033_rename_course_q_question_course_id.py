# Generated by Django 4.1.3 on 2022-12-06 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0032_alter_answer_id_alter_co_id_alter_course_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='course_q',
            new_name='course_ID',
        ),
    ]