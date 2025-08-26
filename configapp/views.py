from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from .models import *
from .serializers import *
#
# @api_view(["GET","POST"])
# def actor_get_post(request):
#     if request.method=="GET":
#         actors=Actor.objects.all()
#         serializer=ActorSerializers(actors,many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     elif request.method=="POST":
#         serializer=ActorSerializers(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#
# @api_view(["PUT"])
# def actor(request,pk):
#     actor=get_object_or_404(Actor,pk=pk)
#     serializer=ActorSerializers(actor,data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class ActorApi(APIView):
    def post(self,request):
        serializer=ActorSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    def get(self,request):
        actors = Actor.objects.all()
        serializer=ActorSerializers(actors,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ActorDetailApi(APIView):
    def get(self,request,pk):
        actor=get_object_or_404(Actor,pk=pk)
        serializer = ActorSerializers(actor)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def put(self,request,pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer=ActorSerializers(actor,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)

class MovieApi(APIView):
    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        actors = Movie.objects.all()
        serializer = MovieSerializers(actors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class MovieDetailApi(APIView):
    def get(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = MovieSerializers(actor)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        actor = get_object_or_404(Actor, pk=pk)
        serializer = MovieSerializers(actor, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class MovieDataAPI(APIView):
    def get(self, request, start_year = None, end_year=None):
        if end_year and end_year:
            movies = Movie.objects.filter(year__range=(start_year, end_year))
        elif start_year:
            movies = Movie.objects.filter(year=start_year)
        else:
            movies = Movie.objects.annotate(count_actor = Count('actor')).filter(count_actor__lt = 3).prefetch_related('actor')
        serializer = MovieSerializers(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.
