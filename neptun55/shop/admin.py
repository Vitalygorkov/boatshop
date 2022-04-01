from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe
from .models import Color, Boat, Photo_product, Category, Product, Manufacturer, Reviews,VideosProducts


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name", "description")
#     list_display_links = ("name",)

# class CategoryAdmin(admin.ModelAdmin):
#     fields = ['name', 'parent']

admin.site.register(Category, MPTTModelAdmin)

class ReviewInline(admin.StackedInline):
    """Отзывы на странице лодки"""
    fields = ("name", "email", "text", "parent")
    model = Reviews
    extra = 1
    # readonly_fields = ("name", "email")

class Photo_productInline(admin.StackedInline):
    model = Photo_product
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="320" height="240"')

    get_image.short_description = "Изображение"

class VideosInline(admin.StackedInline):
    model = VideosProducts
    extra = 1

class DescriptionAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'

@admin.register(Boat)
class BoatAdmin(admin.ModelAdmin):
    form = DescriptionAdminForm
    prepopulated_fields = {'slug': ('name',),}
    list_display = ("name", "manufacturer", "price", )
    list_display_links = ("name",)
    list_filter = ("manufacturer", "price", "name")
    search_fields = ("name","manufacturer")
    inlines = [VideosInline, Photo_productInline, ReviewInline,]
    save_on_top = True
    save_as = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = DescriptionAdminForm
    prepopulated_fields = {'slug': ('name',), }
    list_display = ("name", "manufacturer", "price", )
    list_display_links = ("name",)
    list_filter = ("manufacturer", "price", "name")
    search_fields = ("name","manufacturer")
    inlines = [VideosInline, Photo_productInline, ReviewInline,]
    save_on_top = True
    save_as = True


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к лодке"""
    list_display = ("name", "email", "parent", "product", "id")
    # readonly_fields = ("name", "email")

@admin.register(Photo_product)
class Photo_productAdmin(admin.ModelAdmin):
    list_display = ("get_image", "product",)
    list_display_links = ("product",)
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="320" height="240"')

    get_image.short_description = "Изображение"

@admin.register(VideosProducts)
class VideosAdmin(admin.ModelAdmin):
    list_display = ("video", "product")


admin.site.register(Manufacturer)
admin.site.register(Color)

admin.site.site_title = "Магазин"
admin.site.site_header = "Магазин"