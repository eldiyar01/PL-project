from django.contrib import admin
from .models import University, Club, Gallery, Project


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    pass


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass
