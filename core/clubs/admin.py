from django.contrib import admin
from .models import University, Club, Gallery, Project, ProjectGallery


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    ordering = ("abbreviation",)
    search_fields = ("title__startswith",)


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("university", "title", "faculty", "type")
    search_fields = ("title__startswith",)
    list_filter = ("type", "university", "faculty", )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("club", "title", "author", "start_date", "end_date")
    search_fields = ("title__startswith",)
    list_filter = ("club", "author", "start_date", "end_date")


@admin.register(ProjectGallery)
class ProjectGalleryAdmin(admin.ModelAdmin):
    pass

