# Generated by Django 3.1.2 on 2020-10-08 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0012_auto_20201006_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='group',
        ),
        migrations.AlterField(
            model_name='service',
            name='kdl_service_key',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Кдл. Услуга. Ключ'),
        ),
        migrations.AlterField(
            model_name='service',
            name='kdl_service_perm_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Кдл. Услуга. Пермь. Код'),
        ),
        migrations.AlterField(
            model_name='service',
            name='subgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclature.subgroup', verbose_name='Группа тестов'),
        ),
    ]
