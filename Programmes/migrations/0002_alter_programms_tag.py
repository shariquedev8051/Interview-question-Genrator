# Generated by Django 3.2.6 on 2021-12-19 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Programmes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programms',
            name='Tag',
            field=models.CharField(choices=[('Python', (('List', 'List'), ('Dictionary', 'Dictionary'), ('Tuple', 'Tuple'), ('Set', 'Set'), ('OOPS', 'OOPS'))), ('Django', (('Middle ware', 'Middle ware'), ('Session', 'Session'))), ('Flask', (('Decorators', 'Decorators'), ('App.run()', 'App.run()'))), ('Rest Api', (('JSON', 'JSON'), ('Mixin', 'Mixin'))), ('AWS', (('Lambda', 'Lambda'), ('Boto 3', 'Boto 3')))], default='Python', max_length=30),
        ),
    ]
