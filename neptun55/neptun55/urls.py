"""neptun55 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from rest_framework.routers import SimpleRouter
from contact_form.views import FormView
from shop.views import ProductsView, ProductView, CategoryView, BoatView, BoatsView, PhotoView, VideoView
from blog.views import PostsView, PostView, CategoryBlogView, TagView

router = SimpleRouter()

router.register('api/v1/category', CategoryView)
router.register('api/v1/photo', PhotoView)
router.register('api/v1/video', VideoView)
router.register('api/v1/products', ProductsView)
router.register('api/v1/product', ProductView)
router.register('api/v1/boat', BoatView)
router.register('api/v1/boats', BoatsView)
router.register('api/v1/contactform', FormView)
router.register('api/v1/post', PostView)
router.register('api/v1/posts', PostsView)
router.register('api/v1/CategoryBlog', CategoryBlogView)
router.register('api/v1/tag', TagView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    # path('captcha/', include('captcha.urls')),
    # path('', include("contact_form.urls")), # Добавил по https://fixmypc.ru/post/sozdaem-formu-obratnoi-sviazi-v-django-s-pochtovym-uvedomleniem/
    # path("contact/", include("contact_form.urls")),
    # path("contact_view/", include("contact_form.urls")), - убрал форму на старой версии
    # path("", include("shop.urls")),
    # path("", include("contact_form.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)