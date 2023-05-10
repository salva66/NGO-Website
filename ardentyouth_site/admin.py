from django.contrib import admin
from .models import Slides, Mission, Vision, Objectives, Purpose, Values, Pcauses, Team, OutlookDets, ArticleDets, GalleryDets, About

# Register your models here.

@admin.register(Slides, Mission, Vision, Purpose, Objectives, Values, Pcauses, Team, OutlookDets, ArticleDets, GalleryDets, About)
class DefaultAdmin(admin.ModelAdmin):
    pass


