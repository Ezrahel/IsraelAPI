from datetime import datetime
from rest_framework import serializers
from .models import Complaint, Evidence, Attachment, Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:

        model = Link

        fields = "__all__"