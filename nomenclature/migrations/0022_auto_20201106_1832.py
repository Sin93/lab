# Generated by Django 3.1.2 on 2020-11-06 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0021_auto_20201106_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='файл'),
        ),
    ]
