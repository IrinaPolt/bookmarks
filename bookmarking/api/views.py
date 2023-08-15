import requests
from bs4 import BeautifulSoup
from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.response import Response

from storage.models import Bookmark, BMCollection
from .serializers import (
    CollectionSerializer,
    BookmarkCreateSerializer,
    BookmarkSerializer
)


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookmarkCreateSerializer
        else:
            return BookmarkSerializer
    
    def perform_create(self, serializer):
        link = serializer.validated_data.get('url')
        page = requests.get(link)
        soup = BeautifulSoup(page.content, 'html.parser')

        data = {}
        fields = ['title', 'description', 'url', 'type', 'image']

        for field in fields:
            check = soup.find('meta', {'property': f'og:{field}'})
            if check != None:
                data[field] = check.get('content', '')
            else:
                continue

        if len(data) == 0:
            data['title'] = soup.find('title').text
            description = soup.find('meta', {'name': 'description'})
            if description:
                data['description'] = description.get('content', '')
            data['url'] = link

        serializer = BookmarkSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            obj = Bookmark.objects.create(**data)
            return Response(data=obj, status=HTTPStatus.CREATED)
        else:
            return Response(status=HTTPStatus.BAD_REQUEST)


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = BMCollection.objects.all()
    serializer_class = CollectionSerializer
