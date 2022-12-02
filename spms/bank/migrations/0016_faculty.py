# Generated by Django 3.1.7 on 2022-12-02 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0015_auto_20221202_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FUserID', models.CharField(max_length=4)),
                ('position', models.CharField(max_length=30)),
                ('room', models.CharField(max_length=5, null=True)),
                ('fac_deptID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fac_dep', to='bank.department')),
            ],
        ),
    ]
