from django.contrib import admin
from import_export import resources
from .models import Grade, Quiz, Image, Test


# Inlines
# class ImageInline(admin.options.TabularInline):
#     model = Image
#     extra = 1


# Admin
class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    # list_filter = ('',)
    search_fields = ('id', 'name')


class QuizAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', ('tank', 'grade', 'type', 'position'))
        }),
        ('Text', {
            'classes': ('wide'),
            'fields': (('text_eng', 'text_arabic'),)
        }),
        ('Image Table', {
            'classes': ('wide',),
            'fields': ('image_table_eng', 'image_table_arabic'),
        }),
        ('Images', {
            'classes': ('wide',),
            'fields': ('images',)
        }),
    )

    # inlines = [ImageInline]
    list_editable = ['grade', 'type', 'position',]
    list_display = (
        'id', 'name', 'tank', 'grade', 'type', 'position', 'text_eng', 'text_arabic',
        'image_table_eng', 'image_table_arabic', 'created_at',
    )

    list_display_links = ('id',)
    list_filter = ('name', 'tank', 'grade', 'type', 'position', 'image_table_eng', 'image_table_arabic', 'created_at')
    search_fields = ('id', 'name', 'tank', 'grade', 'type', 'created_at')



class ImageAdmin(admin.ModelAdmin):
    # fields = ( 'image_tag', )
    # readonly_fields = ('image_tag',)
    list_display = ('id', 'image_tag', 'image',)


# class TestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text')


admin.site.register(Grade, GradeAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Image, ImageAdmin)
# admin.site.register(Test, TestAdmin)

