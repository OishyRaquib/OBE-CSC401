# Generated by Django 4.1.3 on 2022-12-06 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0052_alter_question_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.FloatField(),
        ),
    ]
