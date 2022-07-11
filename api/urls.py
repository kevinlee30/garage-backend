#Urls for api access

from django.urls import path, include
from .views import (
    HomeView, 
    AmbassadorListView, EventListView, WorkshopListView, ProjectListView, StartUpListView, 
    AmbassadorDetailView, EventDetailView, WorkshopDetailView, ProjectDetailView, StartUpDetailView
)

urlpatterns = [
    path('', HomeView.as_view(), name="api-root"),
    path('ambassadors/', AmbassadorListView.as_view(), name="ambassador-list"),
    path('events/', EventListView.as_view(), name="event-list"),
    path('workshops/', WorkshopListView.as_view(), name="workshop-list"),
    path('projects/', ProjectListView.as_view(), name="project-list"),
    path('startups/', StartUpListView.as_view(), name="startup-list"),
    
    path('ambassadors/<int:pk>', AmbassadorDetailView.as_view(), name="ambassador-detail"),
    path('events/<int:pk>', EventDetailView.as_view(), name="event-detail"),
    path('workshops/<int:pk>', WorkshopDetailView.as_view(), name="workshop-detail"),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name="project-detail"),
    path('startups/<int:pk>', StartUpDetailView.as_view(), name="startup-detail"),
]

