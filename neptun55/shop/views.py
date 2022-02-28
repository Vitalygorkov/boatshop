from django.shortcuts import render
from django.views.generic.base import View
from .models import Product, Category


# def get_manufacturer_by_subcategory(category):
#     boats = Boat.objects.all()
#     category_boat = []
#     manufacturer = []
#     for boat in boats:
#         if boat.category.name in category_boat:
#             continue
#         else:
#             category_boat.append([boat.subcategory.name, boat.subcategory.url])
#         if boat.boat_manufacturer.name in manufacturer:
#             continue
#         else:
#             manufacturer.append(boat.subcategory.name)
#     return category_boat



# class BoatsView(View):
#     # Список лодок
#     def get(self, request):
#         boats = Boat.objects.all()
#         categories = Category.objects.all()
#         # subcategories = Subcategory.objects.all()
#         # manufacturers = get_manufacturer_by_subcategory(Boat)
#         return render(request, "shop/index.html", {"boat_list": boats, "category_list": categories })

def index(request):
    categories = Category.objects.all()
    # subcategories = Subcategory.objects.all()
    # manufacturers = get_manufacturer_by_subcategory(Boat)
    return render(request, "shop/index.html", { "category_list": categories })

def show_category(request, category_slug):
    categories = Category.objects.all()
    #categoryID = Category.objects.get(url=category_slug)
    # branch_categories = Category.objects.get(url=category_slug).get_descendants(include_self=True)
    branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
    # print(branch_categories)
    category_products = Product.objects.filter(category__in=branch_categories).distinct()
    return render(request, "shop/details.html", {"category_list": categories,
                                               "category_products": category_products,})
def show_product(request, product_slug,category_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    return render(request, "shop/product.html", {"product": product,
                                                 "category_list": categories,})

# def show_subcategory(request, category_slug, subcategory_slug):
#     pass
#     boats = Boat.objects.all()
#     categories = Category.objects.all()
#     # subcategories = Subcategory.objects.all()
#     # manufacturers = get_manufacturer_by_subcategory(Boat)
#     return render(request, "shop/index.html", {"boat_list": boats, "category_list": categories })