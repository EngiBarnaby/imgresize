from rest_framework import serializers
from myapp.models import UserImage

class ImageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserImage
        fields = '__all__'