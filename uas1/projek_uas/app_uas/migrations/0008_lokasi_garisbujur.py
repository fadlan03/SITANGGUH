# Generated by Django 4.1.5 on 2023-01-05 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_uas', '0007_rename_koordinat_lokasi_garis_lintang'),
    ]

    operations = [
        migrations.AddField(
            model_name='lokasi',
            name='garisbujur',
            field=models.CharField(default='some_value', max_length=100),
        ),
    ]
