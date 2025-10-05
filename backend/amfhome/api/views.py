import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from products.models import ProductsModel
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from products.serializers import ProductsSerializers

# Create your views here.
# -------------------------------------------------------------------------------------------------------

# api home without model
# -----------------------------------------------------------------------------------------------------------------

# def api_home(request, *args, **kwargs):
    
#     # here we get the data from the 'params'
#     print(request.GET)
#     print(request.POST)
    
#     # reading the data from json
#     body = request.body
#     print('debugging body', body)
    
#     # creating an empty dictionary
#     data = {}
    
#     try:
#         # converting string json data to json data: de-serialzation
#         data = json.loads(body)
        
#     except:
#         pass
    
#     print(data)
    
#     # adding "key:value" pair to the data dictionary
#     data['params'] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
    
#     return JsonResponse(data)


# api home with model
# -------------------------------------------------------------------------------------------------------------

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductsSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)




    

