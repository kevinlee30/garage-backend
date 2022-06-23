from rest_framework import serializers
from .models import Ambassador, Event, Workshop, Project, StartUp

#When using Google Drive backend, URLs automatically generate with an extra parameter so the file is downloaded
#trimDefaultURL removes the parameter, so the URL just serves the file instead of trying to download it.
def trimDefaultURL(url):
    if url.endswith("&export=download"):
        return url[:-16]
    else:
        return url

class AmbassadorSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    class Meta:
        model = Ambassador
        fields = ['url', 'name', 'desc', 'displayImageUrl']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        return trimDefaultURL(obj.contentVideo.url)
        
    class Meta:
        model = Event
        fields = ['url', 'name', 'date', 'desc', 'article', 'link', 'isFlagshipEvent', 'displayImageUrl', 'contentVideoUrl']

class WorkshopSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        return trimDefaultURL(obj.contentVideo.url)
        
    class Meta:
        model = Workshop
        fields = ['url', 'name', 'date', 'desc', 'article', 'link', 'displayImageUrl', 'contentVideoUrl']
        
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        return trimDefaultURL(obj.contentVideo.url)
        
    class Meta:
        model = Project
        fields = ['url', 'name', 'desc', 'article', 'link', 'displayImageUrl', 'contentVideoUrl']
        
class StartUpSerializer(serializers.HyperlinkedModelSerializer):
    #Uses a method field to just get the image/file URL, without other data
    displayImageUrl = serializers.SerializerMethodField()
    def get_displayImageUrl(self, obj):
        return trimDefaultURL(obj.displayImage.url)
        
    contentVideoUrl = serializers.SerializerMethodField()
    def get_contentVideoUrl(self, obj):
        return trimDefaultURL(obj.contentVideo.url)
        
    class Meta:
        model = StartUp
        fields = ['url', 'name', 'desc', 'article', 'link', 'displayImageUrl', 'contentVideoUrl']

        
    
    
    