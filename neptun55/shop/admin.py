from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Type_boat, Color, Boat, Photo_boat, Category, Type_bottom, Manufacturer, Reviews,VideosBoats


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    list_display_links = ("name",)


class ReviewInline(admin.StackedInline):
    """Отзывы на странице лодки"""
    fields = ("name", "email", "text", "parent")
    model = Reviews
    extra = 1
    # readonly_fields = ("name", "email")

class Photo_boatInline(admin.StackedInline):
    model = Photo_boat
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="320" height="240"')

    get_image.short_description = "Изображение"

class VideosInline(admin.StackedInline):
    model = VideosBoats
    extra = 1

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    list_display = ("boat_model", "boat_manufacturer", "type_boat", "type_motor", "price", )
    list_display_links = ("boat_model",)
    list_filter = ("boat_manufacturer", "type_boat", "type_motor", "price", "boat_model")
    search_fields = ("boat_model","boat_manufacturer")
    inlines = [VideosInline, Photo_boatInline, ReviewInline,]
    save_on_top = True
    save_as = True



@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к лодке"""
    list_display = ("name", "email", "parent", "product", "id")
    # readonly_fields = ("name", "email")

@admin.register(Photo_boat)
class Photo_boatAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "get_image", "boat",)
    list_display_links = ("title",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="320" height="240"')

    get_image.short_description = "Изображение"

@admin.register(VideosBoats)
class VideosAdmin(admin.ModelAdmin):
    list_display = ("video", "boat")

admin.site.register(Type_boat)
admin.site.register(Manufacturer)
admin.site.register(Type_bottom)


# admin.site.register(Boat, BoatAdmin)
admin.site.register(Color)

admin.site.site_title = "Магазин"
admin.site.site_header = "Магазин"