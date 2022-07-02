from os import link
from django.shortcuts import render
from I4G006635NH1.links.models import link

from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from I4G006635NH1.links.serizliers import LinkSerializer

# Create your views here.

class PostListApi():
    queryset = link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi():
    queryset = link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostDetailApi():
    queryset = link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostUpdateApi():
    queryset = link.object.filter(active=True)
    serializer_class = LinkSerializer

class PostDeleteApi():
    queryset= link.objects.filter(active=True)
    serializer_class = LinkSerializer