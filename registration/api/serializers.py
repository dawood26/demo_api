from rest_framework import serializers
from registration.models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id','first_name','last_name','phone','email')