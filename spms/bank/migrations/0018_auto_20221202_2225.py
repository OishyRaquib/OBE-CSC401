# Generated by Django 3.1.7 on 2022-12-02 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0017_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='secNo',
            field=models.IntegerField(),
        ),
    ]
