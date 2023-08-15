from rest_framework import serializers

from storage.models import Bookmark, BMCollection
from users.models import User


class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__'


class BookmarkCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = ('url', )


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BMCollection
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'password')

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
