# Generated by Django 4.1.3 on 2022-12-02 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0016_alter_department_id_alter_program_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseTitle', models.CharField(blank=True, max_length=100)),
                ('courseCode', models.CharField(max_length=20, unique=True)),
                ('courseResource', models.CharField(max_length=100)),
                ('Duration', models.CharField(blank=True, max_length=10)),
                ('PreRequisite', models.CharField(blank=True, max_length=100)),
                ('Credit', models.IntegerField()),
                ('ContactHour', models.CharField(blank=True, max_length=10)),
                ('Grading', models.CharField(max_length=100)),
                ('Assesment', models.CharField(max_length=100)),
            ],
        ),
    ]