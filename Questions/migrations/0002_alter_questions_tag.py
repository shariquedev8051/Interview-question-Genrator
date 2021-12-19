# Generated by Django 3.2.6 on 2021-12-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Tag',
            field=models.CharField(choices=[('Python', ((1, 'List'), (2, 'Tuple'), (3, 'Dictionary'), (4, 'Set'), (5, 'OOPS'))), ('Advanced Python', ((1, 'Excel File Handling'), (2, 'CSV file handling'))), ('Django', ((1, 'Middle Ware'), (2, 'Session'))), ('Flask', ((1, 'Decorators'), (2, 'App.run()'))), ('Rest Api', ((1, 'JSON'), (2, 'Mixin'))), ('AWS', ((1, 'Lambda'), (2, 'Boto 3')))], default='Python', max_length=30),
        ),
    ]