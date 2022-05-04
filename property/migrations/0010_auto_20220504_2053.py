# Generated by Django 2.2.24 on 2022-05-04 17:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0009_disliker'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_app', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='disliker',
            name='disliker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='disliker',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Flat'),
        ),
    ]
