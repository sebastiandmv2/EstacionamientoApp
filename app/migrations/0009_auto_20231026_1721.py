# Generated by Django 3.2.22 on 2023-10-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20231026_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrendamiento',
            name='hora_fin',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='arrendamiento',
            name='hora_inicio',
            field=models.TimeField(),
        ),
    ]
