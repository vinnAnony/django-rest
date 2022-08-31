from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import Product

@api_view(["GET"])
def api_home (request, *args, **kwargs):
    """ This is now a Django RestFramework View """

    # if request.method != "POST":
    #     return Response({"detail": "GET not allowed"}, status=405)

    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        data = model_to_dict(model_data,fields=['id', 'name'])

    return Response(data)