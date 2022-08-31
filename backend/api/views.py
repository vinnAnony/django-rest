import json
from django.http import JsonResponse

from api.models import Product


def api_home (request, *args, **kwargs):
    model_data = Product.objects.all().first()
    
    data = {}

    if model_data:
        data['id'] = model_data.id
        data['imageUrl'] = model_data.imageUrl
        data['name'] = model_data.name
        data['price'] = model_data.price
        data['rating'] = model_data.rating
        data['producer'] = model_data.producer
        data['unit'] = model_data.unit
        data['category'] = model_data.category
        data['isFeatured'] = model_data.isFeatured
    
    return JsonResponse(data)