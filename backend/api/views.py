from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Product
from api.serializer import ProductSerializer

@api_view(["GET"])
def api_home (request, *args, **kwargs):
    """ This is now a Django RestFramework View """

    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405)

    instance = Product.objects.all().first()
    data = {}
    if instance:
        # data = model_to_dict(instance,fields=['id', 'name','price','discount_price'])
        data = ProductSerializer(instance).data

    return Response(data)