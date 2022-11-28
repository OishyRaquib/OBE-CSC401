# Generated by Django 3.1.7 on 2022-11-28 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SUserID', models.CharField(max_length=7)),
                ('enroll_year', models.IntegerField()),
                ('deptID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.department')),
                ('programID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.program')),
            ],
        ),
    ]
