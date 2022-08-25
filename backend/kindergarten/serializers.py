from rest_framework import serializers
from kindergarten.models import Class, Child, Teacher

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        # fields = ['class_id', 'class_name']
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__' # ['teacher_id', 'last_name']

