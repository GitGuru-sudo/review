# Generated by Django 5.2.1 on 2025-07-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='drc',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='review',
            name='name',
            field=models.CharField(max_length=122),
        ),
        migrations.AlterField(
            model_name='review',
            name='phone',
            field=models.CharField(max_length=122),
        ),
    ]
