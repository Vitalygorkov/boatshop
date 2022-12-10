from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, CategoryBlog, Tag
from django import forms
from mptt.admin import MPTTModelAdmin


class DescriptionAdminForm(forms.ModelForm):
    content = forms.CharField(label="Текст статьи", widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = DescriptionAdminForm
    list_display = ["title", "category", "created_ad", 'views_simple']
    fields = ["title", "category", "short_description", 'author',
              "content", "photo", "views_simple", "tags"]

    # Для вывода уникальных просмотров
    # def display_views(self, x):
    #     print(x.views.count())
    #     # return 'Id просмотров'.join([ views.id for views in self.views.all()[:3] ])
    #     print("функция display_views")
    #     return x.views.count()
    #
    # display_views.short_description = 'Просмотры'

admin.site.register(CategoryBlog, MPTTModelAdmin)

# @admin.register(CategoryBlog)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("title")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["title"]