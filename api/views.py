from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,ListAPIView ,RetrieveAPIView
from .serializers import RegisterSerializer, ListSerializer, DetailsSerializer,UserSerializer
from items.models import Item
from .permissions import IsTrue
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.permissions import AllowAny
# Create your views here.
class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']





class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsTrue]
