# Generated by Django 4.1.3 on 2022-11-26 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_txt',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='QID',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]