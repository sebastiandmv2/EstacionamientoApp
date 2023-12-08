# Generated by Django 3.2.22 on 2023-10-26 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comuna', models.CharField(max_length=50)),
                ('codigo_postal', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('costo_por_hora', models.IntegerField(default=0)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dueno')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=7)),
                ('modelo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('descripcion', models.TextField()),
                ('monto_recaudado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estacionamiento')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Arrendamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('precio', models.IntegerField()),
                ('hora_inicio', models.TimeField(default='00:00')),
                ('hora_fin', models.TimeField(default='00:00')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estacionamiento')),
            ],
        ),
    ]
