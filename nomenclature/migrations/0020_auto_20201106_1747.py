# Generated by Django 3.1.2 on 2020-11-06 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nomenclature', '0019_auto_20201103_1838'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfiles',
            old_name='file',
            new_name='my_file',
        ),
    ]