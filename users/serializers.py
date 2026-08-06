from rest_framework import serializers
from .models import User, Tier

class TierSerializer(serializers.ModelSerializer):

  class Meta:
    model = Tier
    fiels = ['name', 'max_requests', 'window_seconds']


class UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ['name', 'email','tier']



