# Generated by Django 3.0.8 on 2020-10-02 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, unique=True, verbose_name='Номер группы')),
                ('name', models.CharField(max_length=256, unique=True, verbose_name='Название группы')),
            ],
        ),
        migrations.CreateModel(
            name='SubGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3, unique=True, verbose_name='Номер группы')),
                ('name', models.CharField(max_length=256, verbose_name='Название группы')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclature.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код номенклатура')),
                ('tcle_code', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Код услуги в TCLE')),
                ('tcle_abbreviation', models.CharField(blank=True, max_length=50, unique=True, verbose_name='Ключ (аббревиатура) услуги в TCLE')),
                ('kdl_service_key', models.CharField(max_length=50, verbose_name='Кдл. Услуга. Ключ')),
                ('kdl_service_perm_code', models.CharField(max_length=50, verbose_name='Кдл. Услуга. Пермь. Код')),
                ('name', models.CharField(max_length=256, verbose_name='Наименование')),
                ('salesability', models.BooleanField(default=False, verbose_name='Продаваемая')),
                ('type', models.CharField(choices=[('ND', 'Not defined')], default='ND', max_length=50, verbose_name='Тип услуги')),
                ('classifier_1с', models.IntegerField(blank=True, verbose_name='Классификатор 1С')),
                ('start_date', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclature.Group', verbose_name='Группа тестов')),
                ('subgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomenclature.SubGroup', verbose_name='Подгруппа тестов')),
            ],
        ),
    ]