# Generated by Django 4.1.3 on 2022-12-06 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0045_alter_question_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=500),
        ),
    ]
