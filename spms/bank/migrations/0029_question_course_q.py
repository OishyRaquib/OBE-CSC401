# Generated by Django 3.1.7 on 2022-12-04 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0028_auto_20221204_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course_q',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='q_course', to='bank.course'),
            preserve_default=False,
        ),
    ]