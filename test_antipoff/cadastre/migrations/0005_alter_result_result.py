# Generated by Django 4.2.5 on 2023-09-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastre', '0004_remove_cadastredata_result_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='result',
            field=models.BooleanField(null=True),
        ),
    ]
