from django.contrib import admin
from .models import Place, Polygon


class PolygonInline(admin.TabularInline):
    model = Polygon
    fields = ('limits', 'encode_points',)
    extra = 1


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('code', 'local_lang_name', 'country_lang_name', 'official_name', 'lang_academ_name', 'geotype', 'parent', 'lat', 'lon', 'countPolygons', 'countPoints')
    list_display_links = ('code', 'local_lang_name')
    ordering = ('local_lang_name', 'geotype')
    search_fields = ['local_lang_name', 'country_lang_name', 'official_name', 'lang_academ_name']
    list_filter = ('geotype',)
    prepopulated_fields = {'slug': ('local_lang_name',)}
    inlines = [PolygonInline, ]

admin.site.register(Place, PlaceAdmin)
