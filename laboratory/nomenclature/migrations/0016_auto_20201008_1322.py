# Generated by Django 3.1.2 on 2020-10-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0015_auto_20201008_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('ND', 'Not defined'), ('PR', 'ПРОФ'), ('LS', 'Лабораторное исследование'), ('KP', 'Коммерческий профиль'), ('SE', 'Услуга')], default='ND', max_length=50, verbose_name='Тип услуги'),
        ),
    ]