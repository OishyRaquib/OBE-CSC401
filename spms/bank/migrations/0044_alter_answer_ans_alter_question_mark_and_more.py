# Generated by Django 4.1.3 on 2022-12-06 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0043_alter_courseoutline_coursecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='mark',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.TextField(),
        ),
    ]