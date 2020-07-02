from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from myapp.models import UserImage
from .serializers import ImageListSerializer

class ImageListView(APIView):
    def get(self, request):
        images = UserImage.objects.all()
        serializer = ImageListSerializer(images, many=True)
        return Response(serializer.data)

class ImageDetailView(APIView):
    def get(self, request, pk):
        image = UserImage.objects.get(id=pk)
        serializer = ImageListSerializer(image)
        return Response(serializer.data)

class ImageChangeView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ImageListSerializer
    queryset = UserImage.objects.all()

class ImageCreateView(generics.CreateAPIView):
    serializer_class =  ImageListSerializer
