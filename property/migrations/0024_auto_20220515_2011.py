# Generated by Django 2.2.24 on 2022-05-15 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0023_auto_20220515_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(db_index=True, default=False, null=True, verbose_name='Новостройка'),
        ),
    ]
