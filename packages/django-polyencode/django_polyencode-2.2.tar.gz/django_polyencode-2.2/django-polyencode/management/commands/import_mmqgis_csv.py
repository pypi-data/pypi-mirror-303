import os
import csv
from django.core.management.base import BaseCommand
from geodata.models import Place, Polygon
from django.template.defaultfilters import slugify


def import_places(geo_choice, path):
    if geo_choice and path:
        places = import_attributes(geo_choice, path)
        import_nodes(geo_choice, path, places)


def import_attributes(geo_choice, path):
    attrs = os.path.join(path, 'attributes.csv')
    places = {}
    with open(attrs, 'rb') as attfile:
        attreader = csv.DictReader(attfile)
        for attrow in attreader:
            if not Place.objects.filter(code=attrow['code']).exists():
                place = Place()
                place.code = attrow['code']
                place.local_lang_name = attrow['local_lang_name']
                place.country_lang_name = 'country_lang_name' in attrow and attrow['country_lang_name'] != 'NULL' and attrow['country_lang_name'] or None
                place.official_name = 'official_name' in attrow and attrow['official_name'] != 'NULL' and attrow['official_name'] or None
                place.lang_academ_name = 'lang_academ_name' in attrow and attrow['lang_academ_name'] != 'NULL' and attrow['lang_academ_name'] or None
                if not Place.objects.filter(local_lang_name=attrow['local_lang_name']).exists():
                    place.slug = slugify(attrow['local_lang_name'])
                else:
                    place.slug = slugify("%s-%s" % (attrow['local_lang_name'], attrow['code']))
                if 'parent_code' in attrow and attrow['parent_code'] != '-':
                    try:
                        place.parent = Place.objects.get(code=attrow['parent_code'])
                    except:
                        print "ERROR: %s [PARENT NOT FOUND]" % (attrow['parent_code'])
                if 'consortium' in attrow and geo_choice == "2" and attrow['consortium'] == "1":
                    place.geotype = "0"
                else:
                    place.geotype = geo_choice
                place.save()
            else:
                place = Place.objects.get(code=attrow['code'])

            places.update({attrow['shapeid']: place})
    return places


def import_nodes(geo_choice, path, places):
    nodes = os.path.join(path, 'nodes.csv')
    polygons = {}
    with open(nodes, 'rb') as nodefile:
        nodereader = csv.DictReader(nodefile)
        for noderow in nodereader:
            if not noderow['shapeid'] in polygons:
                polygons.update({"%s" % noderow['shapeid']: "%s,%s" % (noderow['x'], noderow['y'])})
            else:
                polygons[noderow['shapeid']] += " %s,%s" % (noderow['x'], noderow['y'])

        mem_place = None
        for polygon in polygons.keys():
            place = places[polygon]
            if not mem_place == place:
                Polygon.objects.filter(place=place).delete()
                mem_place = place
            polygon = Polygon(place=place, limits=polygons[polygon])
            polygon.save()


class Command(BaseCommand):
    help = "Import places from mmqgis csv files"

    def add_arguments(self, parser):
        parser.add_argument('-gtype', '--geotype', type=str, help='Calculate this geo type places')
        parser.add_argument('-p', '--path', type=str, help='CSV files path')

    def handle(self, *args, **options):
        import_places(geo_choice=options.get('geotype', None), path=options.get('path', None))
        return 'Done!'
