# Generated by Django 4.1.3 on 2022-12-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0040_plo_outly_pk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseoutline',
            name='assesment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='courseResource',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='course_descrip',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='days',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='grading',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='courseoutline',
            name='mob',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
