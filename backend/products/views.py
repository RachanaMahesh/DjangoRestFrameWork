from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Product
from .serializer import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateView.as_view()

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"

product_detail_view = ProductDetailView.as_view()

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        serializer.save(content = instance.content)

product_update_view = ProductUpdateView.as_view()

class ProductDestroyView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

product_destroy_view = ProductDestroyView.as_view()

# class ProductListView(generics.ListAPIView):
#     """ DO NOT USE THIS"""
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# product_list_view = ProductListView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request, pk = None, *args, **kwargs):

    if(request.method == "GET"):
        if pk is not None:
            # Detail View
            obj = get_object_or_404(Product, pk = pk)
            data = ProductSerializer(obj, many = False).data
            return Response(data)
        #List View
        queryset = Product.objects.all()
        data = ProductSerializer(queryset, many = True).data
        return Response(data)
    if(request.method == "POST"):
        # create view
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save(content = content)

            return Response(serializer.data)
        return Response({"message" : "Invalid Date"},status=400 )




        



