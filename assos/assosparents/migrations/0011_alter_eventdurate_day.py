# Generated by Django 4.1 on 2022-09-27 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assosparents', '0010_remove_eventdurate_daily_remove_eventdurate_hebdo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdurate',
            name='day',
            field=models.CharField(choices=[('LUNDIS', 'Lundi'), ('MARDIS', 'Mardi'), ('MERCREDIS', 'Mercredi'), ('JEUDIS', 'Jeudi'), ('VENDREDIS', 'Vendredi'), ('SAMEDIS', 'Samedi'), ('DIMANCHES', 'Dimanche')], default='LU', max_length=10),
        ),
    ]