# Generated by Django 3.1.7 on 2022-11-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('dateofbirth', models.DateField()),
                ('email', models.CharField(blank=True, max_length=50)),
                ('phone', models.IntegerField(blank=True)),
                ('address', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
