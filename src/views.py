from rest_framework import generics
from rest_framework.response import Response
from .serializer import NetworkMobilesSerializer
from .models import NetworkMobile
from .utils import get_data_from_api_address


class NetworkMobileListView(generics.ListAPIView):
    queryset = NetworkMobile.objects.all()
    serializer_class = NetworkMobilesSerializer

    def list(self, request, *args, **kwargs):
        address = self.request.query_params.get('address')
        zipcode = self.request.query_params.get('zipcode')
        data = ""
        try:
            if address and zipcode:
                new_address = f"{address.replace(' ', '+')}&postcode={zipcode}"
            else:
                new_address = address.replace(' ', '+')

            data = get_data_from_api_address(new_address)['features']
        except Exception as err:
            if err is type(KeyError) or err is type(AttributeError):
                return Response({'Error': 'Invalid address'}, status=400)

        if not data:
            return Response({'Message': 'Address not found'}, status=200)
        context = {}
        for row in data:
            coordinates = dict(row)['geometry']['coordinates']
            queryset = self.queryset.filter(
                coordinate_x=round(coordinates[1], 2),
                coordinate_y=round(coordinates[0], 2)).distinct('operator__code')

            if not queryset:
                """ The data provided on csv is not yet completed, 
                if coordinate y doesn't match with the data
                this will search approximately 2.22km radius.
                Note: according to the internet 0.02 coordinate is approximately 1.11km 
                """
                queryset = self.queryset.filter(
                    coordinate_x__lte=round(coordinates[1] + 0.02, 2),
                    coordinate_x__gte=round(coordinates[1] - 0.02, 2),
                    coordinate_y__lte=round(coordinates[0] + 0.02, 2),
                    coordinate_y__gte=round(coordinates[0] - 0.02, 2)).distinct('operator__code')
            serializer = self.get_serializer(queryset, many=True)
            if len(queryset) == 0:

                return Response({
                    f"Message: No approximately network on this {address.replace('+', ' ')}, {zipcode}."},
                    status=200)
            context[dict(row)['properties']['city']] = serializer.data
        if len(context) > 1:
            return Response({'message': 'Multiple address has been found.', 'data': context},
                            status=200)
        return Response(context, status=200)
