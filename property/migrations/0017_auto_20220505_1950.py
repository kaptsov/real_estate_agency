
from phonenumbers import parse, is_valid_number_for_region, is_valid_number
from django.db import migrations


def normalize_phones(apps, schema_editor):
    print('yo')
    Flat = apps.get_model('property.Flat')
    bad_num = Flat.objects.get(owners_phonenumber='+70000000000')

    objnum = parse(bad_num.owners_phonenumber, "RU")
    print(objnum)
    if is_valid_number(objnum):
        bad_num.owners_phonenumber_normalized = objnum
        bad_num.save()
    else:
        print('not valid')


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0016_auto_20220504_2239'),
    ]

    operations = [
        migrations.RunPython(normalize_phones),
    ]
