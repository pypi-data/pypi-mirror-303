import os
import csv
from django.core.management.base import BaseCommand
from geodata.models import Place


def import_extra_data(path):
    extra = os.path.join(path, 'extra.csv')
    with open(extra, 'rb') as extrafile:
        reader = csv.DictReader(extrafile)
        for row in reader:
            if Place.objects.filter(code=row['code']).exists():
                place = Place.objects.get(code=row['code'])
                place.lat = float(row['lat'])
                place.lon = float(row['lon'])
                place.save()
            else:
                print "ERROR: %s [CITY NOT FOUND]" % (row['name'])


class Command(BaseCommand):
    help = "Import places extra data from csv files"

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='CSV files path')

    def handle(self, *args, **options):
        import_extra_data(path=options.get('path', None))
        return 'Done!'
