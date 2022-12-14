# Generated by Django 3.1.7 on 2022-12-02 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0020_section_courseid'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CONo', models.CharField(max_length=3)),
                ('Level', models.IntegerField()),
                ('Statement', models.CharField(max_length=200)),
                ('SecID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='co_sec', to='bank.section')),
            ],
        ),
    ]
