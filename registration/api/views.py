from django.shortcuts import render
from registration.models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework import generics
from django.views.generic import TemplateView

# Create your views here.
class AboutView(TemplateView):
    template_name = "registration/about.html"

class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = StudentSerializer
    #queryset = Student.objects.all()
    def get_queryset(self):
        return Student.objects.all()
 ####listing the items######
class StudentListView(generics.ListAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def get_queryset(self):
        return Student.objects.all()

#### creating the items######
class StudentCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    def get_queryset(self):
        return Student.objects.all()
