# Generated by Django 2.0.6 on 2018-07-15 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quovadisapp', '0004_auto_20180709_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quovadisapp.Category'),
        ),
    ]
