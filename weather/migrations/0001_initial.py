# Generated by Django 4.2.5 on 2023-10-03 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherPref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minumumTemperature', models.IntegerField(blank=True, null=True)),
                ('maximumTemperature', models.IntegerField(blank=True, null=True)),
                ('setLocation', models.JSONField(blank=True, default=list, null=True, verbose_name='locationPref')),
                ('toNofify', models.BooleanField(default=False, verbose_name='Notify User')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
