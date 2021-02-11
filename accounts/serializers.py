from rest_framework import serializers
from accounts.models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'