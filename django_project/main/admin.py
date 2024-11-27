from django.contrib import admin
from .models import Students, Course, Rating

# Register your models here.

admin.site.register(Course)
admin.site.register(Rating)


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "surname",
        "sex",
        "active",
        "short_name",
    )
    search_fields = (
        "name",
        "surname",
    )
    list_filter = ("sex",)

    def short_name(self, obj):
        return f"{obj.surname} {obj.name[0]}."

    short_name.short_description = "Короткое имя"
