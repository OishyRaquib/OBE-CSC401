# Generated by Django 4.1.3 on 2022-12-06 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0046_alter_question_mark_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]