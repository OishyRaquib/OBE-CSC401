# Generated by Django 3.1.7 on 2022-12-04 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0027_auto_20221203_0216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='correctAns',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ans', models.CharField(max_length=1000)),
                ('q_pk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ans_qpk', to='bank.question')),
            ],
        ),
    ]
