# Generated by Django 4.1.5 on 2023-01-06 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_uas', '0008_lokasi_garisbujur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lokasi',
            name='garisbujur',
            field=models.CharField(default='', max_length=100),
        ),
    ]
