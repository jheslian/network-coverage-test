from pyproj import Proj, transform
from rest_framework.response import Response
from src.models import Network
import requests


def create_networks():
    data = {
        20801: 'Orange',
        20810: 'SFR',
        20815: 'Free',
        20820: 'Bougyues',
    }
    for k, v in data.items():
        Network.objects.create(code=k, name=v)

def convert_lambert93_to_wgs84(x, y):
    """
    Args:
        x (int): latitude
        y (int): longitude


    Returns:
        dict: gps coordinates
    """
    LAMBERT93 = Proj('epsg:2154')
    WGS84 = Proj('epsg:4326')
    x1, y1 = x, y
    coordinate_x, coordinate_y = transform(LAMBERT93, WGS84, x1, y1)
    data = {'coordinate_x': coordinate_x, 'coordinate_y': coordinate_y}
    return data


def get_data_from_api_address(address):
    """ Retrieve data using 'api-adresse' - an api that retrieves data from a query address

    Args:
        address (str): address to query

    Returns:
        dict: data such as geometry/properties etc of an address
    """

    try:
        url = f'https://api-adresse.data.gouv.fr/search/?q={address}'
        resp = requests.get(url)
    except Exception as err:
        if type(err) is AttributeError:
            return Response({'Error': 'Address must be filled.'}, status=400)

        return Response({'Error': 'Something went wrong.'}, status=500)

    return resp.json()
