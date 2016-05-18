from django.contrib import admin
from import_export import resources
from .models import Map, Tank, Habitat, Trivia, Species
from quiz.models import Quiz, Image


class QuizInline(admin.options.StackedInline):
    model = Quiz
    extra = 1


# class TriviaInline(admin.options.TabularInline):
#     model = Trivia
#     extra = 1


class MapAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image_tag', 'created_at', 'updated_at', 'is_current')
    list_display_links = ('title',)
    list_filter = ('id',)
    search_fields = ('id', 'title', 'image', 'created_at', 'updated_at', 'is_current')


class TankAdmin(admin.ModelAdmin):
    inlines = [QuizInline]
    list_display = (
        'tank_id', 'name_eng', 'name_arabic', 'habitat', 'direction_label_eng',
        'direction_label_arabic', 'direction',
    )
    # list_editable = ('tank_quiz',)
    list_display_links = ('name_eng',)
    list_filter = ('id', 'tank_id',)
    search_fields = (
        'id', 'tank_id', 'name_eng', 'name_arabic', 'habitat', 'direction_label_eng', 'direction_label_arabic', 'direction',
    )


class HabitatAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (('name_eng', 'name_arabic',), 'image', ('description_eng',
        'description_arabic',), 'trivia', ('knowledge_eng', 'knowledge_arabic'),)
        }),
    )


    list_display = (
        'id',
        'name_eng',
        'name_arabic',
        'image_tag',
        'description_eng',
        'description_arabic',
        'knowledge_eng',
        'knowledge_arabic',
    )
    list_display_links = ('name_eng',)
    list_filter = ('id', 'name_eng', 'name_arabic')
    search_fields = (
        'id',
        'name_eng',
        'name_arabic',
        'image',
        'description_eng',
        'description_arabic',
        'knowledge_eng',
        'knowledge_arabic',
    )


class TriviaAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', ('text_eng', 'text_arabic'))
        }),
    )

    list_display = (
        'id', 'name', 'text_eng', 'text_arabic',
    )
    list_filter = ('id',)
    search_fields = ('id',)


class SpeciesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'tank',
        'name_eng',
        'name_arabic',
        'scientific_name',
        'image_tag',
        'distribution_label_eng',
        'distribution_label_arabic',
        'distribution_image_tag',
        'description_eng',
        'description_arabic',
    )
    list_display_links = ('tank',)
    list_filter = ('id',)
    search_fields = (
        'id',
        'tank',
        'name_eng',
        'name_arabic',
        'scientific_name',
        'image',
        'distribution_label_eng',
        'distribution_label_arabic',
        'distribution_image',
        'description_eng',
        'description_arabic',
    )



admin.site.register(Map, MapAdmin)
admin.site.register(Tank, TankAdmin)
admin.site.register(Habitat, HabitatAdmin)
admin.site.register(Trivia, TriviaAdmin)
admin.site.register(Species, SpeciesAdmin)

