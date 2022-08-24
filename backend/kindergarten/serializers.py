from rest_framework import serializers
from kindergarten.models import Class

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        # fields = ['class_id', 'class_name']
        fields = '__all__'
