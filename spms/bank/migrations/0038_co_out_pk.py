# Generated by Django 4.1.3 on 2022-12-06 12:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0037_remove_co_secid'),
    ]

    operations = [
        migrations.AddField(
            model_name='co',
            name='out_pk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='out_pk', to='bank.courseoutline'),
            preserve_default=False,
        ),
    ]
