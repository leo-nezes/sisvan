# Generated by Django 3.1.7 on 2021-03-25 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210319_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pesoidade',
            old_name='município',
            new_name='municipio',
        ),
    ]