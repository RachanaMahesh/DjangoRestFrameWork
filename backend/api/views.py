import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import ProductSerializer


# print("----------------- PART - 8 ----------------")

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data ={}
#     if instance:
#         data = ProductSerializer(instance).data # without serializing output willl be in

#     return Response(data)

print("----------------- PART - 9 ----------------")

@api_view(["POST"])
def api_home(request, *args, **kwargs):

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = serializer.data
        print(instance)
        return Response(data)
    return Response({"message" : "Invalid Date"},status=400 )
    


# Create your views here.
# def api_home(request, *args, **kwargs):
    # print("----------------- PART - 5 ----------------")
    # body = request.body
    # print(body) # returns b'' as django ignore body data for get request
    # data = {}
    # # try:
    # #     data['body'] = json.loads(body)
    # # except:
    # #     pass
    # data['headers'] = dict(request.headers)
    # print(dict(request.headers))
    # data['content_type'] = request.content_type
    # print(request.content_type)
    # data['params'] = dict(request.GET)

    # print("----------------- PART -6 ----------------")
    # data = {}
    # model_data = Product.objects.all().order_by("?").first()
    # data['id'] = model_data.id
    # data['title'] = model_data.title
    # data['content'] = model_data.content
    # data['price'] = model_data.price

    # print("----------------- PART - 7 ----------------")
    # model_data = Product.objects.all().order_by("?").first()
    # data ={}
    # if model_data:
    #     data = model_to_dict(model_data)
    # # data = model_to_dict(model_data, fields= ["id","title"])
    # # return JsonResponse(data) # dict to Json 

    # # print(data)
    # # data = dict(data)
    # # json_data_str = json.dumps(data)
    # return HttpResponse(data, headers = {"conten-type":"application/json"})

   
