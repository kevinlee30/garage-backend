from django.shortcuts import render
from .serializers import AmbassadorSerializer, EventSerializer, WorkshopSerializer, ProjectSerializer, StartUpSerializer
from .models import Ambassador, Event, Workshop, Project, StartUp

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.
class HomeView(APIView):
    def get(self, request):
        return Response({
            "Ambassadors": reverse( "ambassador-list", request=request),
            "Events": reverse( "event-list", request=request),
            "Workshops": reverse( "workshop-list", request=request),
            "Projects": reverse( "project-list", request=request),
            "StartUps": reverse( "startup-list", request=request)
        })

class AmbassadorListView(generics.ListAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
class AmbassadorDetailView(generics.RetrieveAPIView):
    queryset = Ambassador.objects.all()
    serializer_class = AmbassadorSerializer
        
class EventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
class EventDetailView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class WorkshopListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
class WorkshopDetailView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
        
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class ProjectDetailView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class StartUpListView(generics.ListAPIView):
    queryset = StartUp.objects.all()
    serializer_class = StartUpSerializer
class StartUpDetailView(generics.ListAPIView):
    queryset = StartUp.objects.all()
    serializer_class = StartUpSerializer