from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data


class ListSerializer(serializers.ModelSerializer):

    favourited = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    added_by = UserSerializer()
    class Meta:
        model = Item
        fields = ['image', 'name', 'description', 'added_by','favourited','detail']
        
    def get_favourited(self, obj):
        return obj.favoriteitem_set.count()

class DetailsSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'favourited_by']

    def get_favourited_by(self, obj):
        return UserSerializer(obj.favoriteitem_set.all(), many=True).data
