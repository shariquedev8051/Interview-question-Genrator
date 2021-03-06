# Generated by Django 3.2.6 on 2021-12-19 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Programms', models.TextField()),
                ('Answer', models.TextField(blank=True, null=True)),
                ('Link', models.URLField(blank=True, null=True)),
                ('Tag', models.CharField(choices=[('Python', ((1, 'List'), (2, 'Tuple'), (3, 'Dictionary'), (4, 'Set'), (5, 'OOPS'))), ('Advanced Python', ((1, 'Excel File Handling'), (2, 'CSV file handling'))), ('Django', ((1, 'Middle Ware'), (2, 'Session'))), ('Flask', ((1, 'Decorators'), (2, 'App.run()'))), ('Rest Api', ((1, 'JSON'), (2, 'Mixin'))), ('AWS', ((1, 'Lambda'), (2, 'Boto 3')))], default='Python', max_length=30)),
            ],
        ),
    ]
