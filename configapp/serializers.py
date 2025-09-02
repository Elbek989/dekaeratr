from rest_framework import serializers
from .models import *
class ActorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Actor
        fields="__all__"

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

class CommitSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommitMovie
        fields = "__all__"