# Generated by Django 3.0.6 on 2020-08-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compression_api', '0003_auto_20200805_0122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.IntegerField(blank=True, default=0.0),
        ),
    ]
