from django.http import JsonResponse
from django.forms.models import model_to_dict

from api.models import Product


def api_home (request, *args, **kwargs):
    model_data = Product.objects.all().first()
    data = {}
    if model_data:
        # data = model_to_dict(model_data)
        data = model_to_dict(model_data,fields=['id', 'name']) #specify only wanted fields
    
    return JsonResponse(data)