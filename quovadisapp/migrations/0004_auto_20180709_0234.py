# Generated by Django 2.0.6 on 2018-07-09 02:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quovadisapp', '0003_auto_20180707_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomimage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='quovadisapp.Room'),
        ),
    ]
