from .models import Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductSerializer


@api_view(['GET'])
def products_list_api_view(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product_api_view(request, id):
    post = get_object_or_404(Product, id=id)
    serializer = ProductSerializer(post)
    return Response(serializer.data)


@api_view(['POST'])
def create_post_api_view(request):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=200)


@api_view(['DELETE'])
def delete_product_api_view(request, id):
    post = get_object_or_404(Product, id=id)
    post.delete()
    return Response(status=204)


@api_view(['PUT', 'PATCH'])
def update_product_api_view(request, id):
    product = get_object_or_404(Product, id=id)
    partial = True if request.method == 'PATCH' else False
    serializer = ProductSerializer(product, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=201)

















