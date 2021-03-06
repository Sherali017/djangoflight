# Generated by Django 3.2.4 on 2021-06-27 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirportModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'airport',
                'verbose_name_plural': 'airports',
            },
        ),
        migrations.CreateModel(
            name='FlightModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='Flight.airportmodel')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='Flight.airportmodel')),
            ],
            options={
                'verbose_name': 'flight',
                'verbose_name_plural': 'flights',
            },
        ),
    ]
