"""
    Import data from csv file to database and add the coordinates
"""

from django.core.management import BaseCommand
from src.models import Network, NetworkMobile
from src.utils import convert_lambert93_to_wgs84
import csv





class Command(BaseCommand):
    def handle(self, *args, **options):
        NetworkMobile.objects.all().delete()
        CSV_PATH = 'mobile_operator.csv'
        fix_type = {'Operateur': int, 'X': int, 'Y': int, '2G': int, '3G': int, '4G': int}

        with open(CSV_PATH, newline='') as file:
            for i, row in enumerate(csv.DictReader(file, delimiter=";")):
                try:
                    row = {key: fix_type[key](value) for key, value in row.items()}
                    data = convert_lambert93_to_wgs84(row['X'], row['Y'])

                    operator = Network.objects.get(code=row['Operateur'])
                    NetworkMobile.objects.create(
                        operator=operator,
                        x=row['X'],
                        y=row['Y'],
                        g2=bool(row['2G']),
                        g3=bool(row['3G']),
                        g4=bool(row['4G']),
                        coordinate_x=format(data['coordinate_x'], '.2f'),
                        coordinate_y=format(data['coordinate_y'], '.2f')
                    )
                    print(f"Line {i} has been uploaded")
                except Exception as err:
                    if type(err) is ValueError or type(err) is TypeError:
                        print(f"Line {i+1} cannot be proccess.")
                    return print("Something went wrong!")
            print("Data uploaded successfully!")
