# Generated by Django 3.1.2 on 2020-10-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0006_service_clients_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='classifier_1с',
            field=models.IntegerField(blank=True, null=True, verbose_name='Классификатор 1С'),
        ),
    ]
