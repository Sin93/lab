# Generated by Django 3.1.2 on 2020-10-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0010_auto_20201006_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='biomaterials',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Биоматериалы'),
        ),
        migrations.AlterField(
            model_name='service',
            name='result_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='тип результата'),
        ),
    ]
