# Generated by Django 3.1.2 on 2020-10-06 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0002_auto_20201006_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subgroup',
            name='number',
            field=models.CharField(max_length=3, verbose_name='Номер группы'),
        ),
    ]