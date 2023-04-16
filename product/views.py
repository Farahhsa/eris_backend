from rest_framework.generics import ListAPIView, RetrieveAPIView
from product.models import Category
from .serializer import CategorySerializer, CategoryDetailSer

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSer
    lookup_field = 'name'
    lookup_url_kwarg ='name'