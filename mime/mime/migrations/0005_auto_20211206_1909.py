# Generated by Django 3.2.9 on 2021-12-06 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mime', '0004_auto_20211206_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='location',
            name='estate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mime',
            name='dumps_name',
            field=models.CharField(max_length=50),
        ),
    ]
