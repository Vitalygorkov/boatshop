from django.urls import path

from . import views

urlpatterns = [
    # path("", views.BoatsView.as_view()),
    path('', views.index, name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('<category_slug>/contacts/', views.contacts, name='contacts'),
    path('<category_slug>/', views.show_category, name='category'),
    path('<category_slug>/<product_slug>/', views.show_product, name='product'),
    # path('<category_slug>/<subcategory_slug>', views.show_subcategory, name='subcategory'),
    # path(r'^categories/$', views.show_category, name='category'),
]