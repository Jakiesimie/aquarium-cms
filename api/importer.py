import csv

from django.core.management.base import BaseCommand

from aquarium.models import Species
from quiz.models import *

# def importer():
#     files = [
#         'species_13_environment-indicators.csv',
#         'species_14_edge-of-the-sea.csv',
#         'species_15_krakens-lair.csv',
#         'species_16_oceans-drifters.csv',
#         'species_17_rainforests-of-the-sea.csv',
#         'species_18_shark-bay.csv',
#         'species_19_dragons-of-the-sea.csv',
#         'species_20_scavengers-of-the-sea.csv',
#         'species_21_australian.csv',
#         'species_22_flightless-birds.csv',
#         'species_23_open-ocean.csv',
#     ]
#     for pos, file_name in enumerate(files):
def importer():
    file_name = 'species_3_mouth-brooders.csv'

    data = csv.DictReader(open('species/' + file_name))
    for row in data:
        s, created = Species.objects.get_or_create(
            tank_id='3',
            name_eng=row['Common Name EN'],
            name_arabic=row['Common Name AR'],
            scientific_name=row['Scientific Name'],
            distribution_label_eng=row['Geographic Distribution EN'],
            distribution_label_arabic=row['Geographic Distribution AR'],
            description_eng=row['Did You know? EN'],
            description_arabic=row['Did You know? AR'],
        )
        if created:
            s.save()
            print 'OK'