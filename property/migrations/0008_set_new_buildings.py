from django.db import migrations


def set_new_buildings(apps, schema_editor):

    Flat = apps.get_model('property.Flat')
    for flat in Flat.objects.all().iterator():
        flat.new_building = flat.construction_year > 2014
        flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20220504_1940'),
    ]

    operations = [
        migrations.RunPython(set_new_buildings),
    ]
