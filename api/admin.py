from django import forms
from django.contrib import admin
from .models import Ambassador, Event, Workshop, Project, StartUp

class AmbassadorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = Ambassador
        fields = '__all__'
@admin.register(Ambassador)
class AmbassadorAdmin(admin.ModelAdmin):
    form = AmbassadorForm
    list_display = ('name', 'desc', 'displayImage')
    fields = ['name', 'desc', 'displayImage']



class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Event
        fields = '__all__'
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    form = EventForm
    list_display = ('name', 'date', 'desc', 'article', 'isFlagshipEvent', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'date', 'desc', 'article', 'isFlagshipEvent', 'displayImage', 'contentVideo', 'link']



class WorkshopForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Workshop
        fields = '__all__'
@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    form = WorkshopForm
    list_display = ('name', 'date', 'desc', 'article', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'date', 'desc', 'article', 'displayImage', 'contentVideo', 'link']



class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Project
        fields = '__all__'
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    list_display = ('name', 'desc', 'article', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'desc', 'article', 'displayImage', 'contentVideo', 'link']  



class StartUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contentVideo'].required = False
    class Meta:
        model = Project
        fields = '__all__'
@admin.register(StartUp)
class StartUp(admin.ModelAdmin):
    form = StartUpForm
    list_display = ('name', 'desc', 'article', 'displayImage', 'contentVideo', 'link')
    fields = ['name', 'desc', 'article', 'displayImage', 'contentVideo', 'link']   

# Register your models here
