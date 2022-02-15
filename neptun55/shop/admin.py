from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Type_boat, Color, Boat

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ("boat_model", "boat_manufacturer", "type_boat", "type_motor", "price", )
    list_display_links = ("boat_model",)
    list_filter = ("boat_manufacturer", "type_boat", "type_motor", "price", "boat_model")
    search_fields = ("boat_model","boat_manufacturer")
    # readonly_fields = ('get_image',) #вывод фотки в поле редактирования

    #функция Для вывода картинки в админ панели
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="160 height="180"')

    get_image.short_description = "Изображение"



admin.site.register(Type_boat)
# admin.site.register(Boat, BoatAdmin)
admin.site.register(Color)

admin.site.site_title = "Магазин"
admin.site.site_header = "Магазин"