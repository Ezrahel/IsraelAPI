from os import link
from django.shortcuts import render
from I4G006635NH1.links.models import link

from rest_framework.generics import GenericAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from I4G006635NH1.links.serizliers import LinkSerializer

# Create your views here.

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import models 
from . import serializers

import datetime 

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




class ActiveLinkView(APIView):
    """
    Returns a list of all active (publicly accessible) links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        qs = models.Link.public.all()
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    
class RecentLinkView(APIView):
    """
    Returns a list of recently created active links
    """
    def get(self, request):
        """ 
        Invoked whenever a HTTP GET Request is made to this view
        """
        seven_days_ago = timezone.now() - datetime.timedelta(days=7)
        qs = models.Link.public.filter(created_date__gte=seven_days_ago)
        data = serializers.LinkSerializer(qs, many=True).data
        return Response(data, status=status.HTTP_200_OK)