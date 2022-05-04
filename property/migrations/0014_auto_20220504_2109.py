# Generated by Django 2.2.24 on 2022-05-04 18:09

from phonenumbers import parse
from django.db import migrations


def normalize_phones(apps, schema_editor):
    print('yo')
    Flat = apps.get_model('property.Flat')
    for flat in Flat.objects.all():
        flat.owners_phonenumber_normalized = parse(flat.owners_phonenumber, 'RU')
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220504_2109'),
    ]


    operations = [
        migrations.RunPython(normalize_phones),
    ]

