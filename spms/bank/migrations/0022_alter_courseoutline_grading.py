# Generated by Django 4.1.3 on 2022-12-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0021_alter_courseoutline_grading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoutline',
            name='grading',
            field=models.CharField(max_length=100),
        ),
    ]
