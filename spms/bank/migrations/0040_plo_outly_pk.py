# Generated by Django 4.1.3 on 2022-12-06 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0039_co_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='plo',
            name='outly_pk',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='outly_pk', to='bank.courseoutline'),
            preserve_default=False,
        ),
    ]
