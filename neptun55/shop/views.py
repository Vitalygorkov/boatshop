from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet

from shop.serializers import ProductSerializer, CategorySerializer
from .models import Product, Category, Boat
from .filters import BoatFilter, ProductFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']

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
def req_parse_dict(req):
    params = {}
    if req['price__gt'] != '0' or req['price__lt'] != '299999':
        params.update({"price": "open"})
    else:
        params.update({"price": "close"})
    if req['length__gt'] != '0' or req['length__lt'] != '550':
        params.update({"length": "open"})
    else:
        params.update({"length": "close"})
    if req['width__gt'] != '0' or req['width__lt'] != '220':
        params.update({"width": "open"})
    else:
        params.update({"width": "close"})
    if req['cockpit_length__gt'] != '0' or req['cockpit_length__lt'] != '500':
        params.update({"cockpit_length": "open"})
    else:
        params.update({"cockpit_length": "close"})
    if req['cockpit_width__gt'] != '0' or req['cockpit_width__lt'] != '200':
        params.update({"cockpit_width": "open"})
    else:
        params.update({"cockpit_width": "close"})
    if req['load_capacity__gt'] != '0' or req['load_capacity__lt'] != '1200':
        params.update({"load_capacity": "open"})
    else:
        params.update({"load_capacity": "close"})
    if req['boat_weight__gt'] != '0' or req['boat_weight__lt'] != '150':
        params.update({"boat_weight": "open"})
    else:
        params.update({"boat_weight": "close"})
    if req['complete_set_weight__gt'] != '0' or req['complete_set_weight__lt'] != '180':
        params.update({"complete_set_weight": "open"})
    else:
        params.update({"complete_set_weight": "close"})
    if req['maximum_motor_power__gt'] != '0' or req['maximum_motor_power__lt'] != '100':
        params.update({"maximum_motor": "open"})
    else:
        params.update({"maximum_motor": "close"})
    if req['fabric_thickness_side__gt'] != '0' or req['fabric_thickness_side__lt'] != '2000':
        params.update({"fabric_thickness_side": "open"})
    else:
        params.update({"fabric_thickness_side": "close"})
    if req['fabric_thickness_bottom__gt'] != '0' or req['fabric_thickness_bottom__lt'] != '2000':
        params.update({"fabric_thickness_bottom": "open"})
    else:
        params.update({"fabric_thickness_bottom": "close"})
    if req['inflatable_compartments__gt'] != '0' or req['inflatable_compartments__lt'] != '15':
        params.update({"inflatable_compartments": "open"})
    else:
        params.update({"inflatable_compartments": "close"})
    if req['passenger_capacity__gt'] != '0' or req['passenger_capacity__lt'] != '15':
        params.update({"passenger_capacity": "open"})
    else:
        params.update({"passenger_capacity": "close"})
    if req['manufacturer'] != '':
        params.update({"manufacturer": "open"})
    else:
        params.update({"manufacturer": "close"})
    if req['category'] != '':
        params.update({"category": "open"})
    else:
        params.update({"category": "close"})
    if req['bulwark'] != 'unknown':
        params.update({"bulwark": "open"})
    else:
        params.update({"bulwark": "close"})
    if req['keel'] != 'unknown':
        params.update({"keel": "open"})
    else:
        params.update({"keel": "close"})

    return params

def req_parse_dict_product(req):
    params = {}
    if req['price__gt'] != '0' or req['price__lt'] != '299999':
        params.update({"price": "open"})
    else:
        params.update({"price": "close"})
    if req['manufacturer'] != '':
        params.update({"manufacturer": "open"})
    else:
        params.update({"manufacturer": "close"})
    return params


def search_boat(request):
    print('Search_boat view')
    # print(request.GET['price__gt'])
    # print(req_parse_dict(request.GET))
    details_status = req_parse_dict(request.GET)
    print(details_status)
    boat_list = Boat.objects.all().order_by('price')
    boat_filter = BoatFilter(request.GET, queryset=boat_list)
    product_filter = ProductFilter(request.GET, queryset=boat_list)
    categories = Category.objects.all()
    # category_products = Product.objects.filter(category__in=branch_categories).distinct()
    category_cats = Category.objects.filter(url='lodki').get_descendants(include_self=False)
    # print(category_cats)

    return render(request, "shop/details-lodki-search.html", {"category_list": categories,
                                          # "category_products": category_products,
                                          "category_cats": category_cats,
                                          "details_status": details_status,
                                          "filter": boat_filter,
                                          "product_filter": product_filter,})

def search_product(request, category_slug):
    print('Search_product view')
    # print(request.GET['price__gt'])
    # print(req_parse_dict(request.GET))
    branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
    cat_id = Category.objects.filter(url=category_slug)
    details_status = req_parse_dict_product(request.GET)
    print(details_status)
    print(cat_id)

    product_list = Product.objects.filter(category=cat_id[0].id).order_by('price')
    product_filter = ProductFilter(request.GET, queryset=product_list)
    categories = Category.objects.all()
    category_products = Product.objects.filter(category__in=branch_categories).distinct()
    # print((category_products))
    category_cats = Category.objects.filter(url='lodki').get_descendants(include_self=False)
    # print(category_cats)
    # cat_name_url = [cat_id[0].name, category_slug, cat_id[0].url]
    return render(request, "shop/details-search.html", {"category_list": categories,
                                          # "category_products": category_products,
                                          "category_cats": category_cats,
                                          "details_status": details_status,
                                          "filter": product_filter,
                                          "product_filter": product_filter,
                                          "last_category": category_slug,
                                          "cat_name_url": cat_id[0],
                                                        })

# def search_boat_category(request, category_slug):
#     boat_list = Boat.objects.all()
#     boat_filter = BoatFilter(request.GET, queryset=boat_list)
#     categories = Category.objects.all()
#     #categoryID = Category.objects.get(url=category_slug)
#     # branch_categories = Category.objects.get(url=category_slug).get_descendants(include_self=True)
#     branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
#     current_category = categories.filter(url=category_slug).get_ancestors(include_self=True)
#     # print(current_category[0].url)
#     cat_url_list  = current_category
#     print(cat_url_list)
#     print('lodki-search category')
#
#     category_products = Product.objects.filter(category__in=branch_categories).distinct()
#     try:
#         category_cats = current_category[0].get_descendants(include_self=False)
#         # print(category_cats)
#     except Exception as e:
#         print("Ошибка:" + str(e))
#     use_template = "shop/details.html"
#     if current_category[0].url != 'lodki':
#         use_template = "shop/details.html"
#     else:
#         use_template = "shop/details-lodki-search.html"
#         print('lodki-search template')
#     print(use_template)
#     return render(request, use_template, {"category_list": categories,
#                                           "category_products": category_products,
#                                           "category_cats": category_cats,
#                                           "cat_url_list": cat_url_list,
#                                           "filter": category_products,})


# def search_boat(request):
#     boat_list = Boat.objects.all()
#     boat_filter = BoatFilter(request.GET, queryset=boat_list)
#     categories = Category.objects.all()
#     return render(request, "shop/details-lodki.html", {"category_list": categories,
#                                           "filter": boat_filter, })

def index(request):
    categories = Category.objects.all()

    # return render(request, "shop/index.html", { "category_list": categories })
    return redirect("/lodki/")

def contacts(request):
    categories = Category.objects.all()

    return render(request, "shop/contacts.html", { "category_list": categories })
def success(request):
    categories = Category.objects.all()

    return render(request, "shop/success.html", { "category_list": categories })

# def show_category(request, category_slug):
#     print(category_slug)
#     print("text_show")
#     categories = Category.objects.all()
#     #categoryID = Category.objects.get(url=category_slug)
#     # branch_categories = Category.objects.get(url=category_slug).get_descendants(include_self=True)
#     branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
#     current_category = categories.filter(url=category_slug).get_ancestors(include_self=True)
#     print(current_category)
#     print("text_show_category")
#     category_products = Product.objects.filter(category__in=branch_categories).distinct()
#     return render(request, "shop/details.html", {"category_list": categories,
#                                                "category_products": category_products,})

def show_category(request, category_slug):
    sale_products = Product.objects.exclude(sale= 0)
    print(sale_products)
    # print('Show_category view')
    categories = Category.objects.all()
    #categoryID = Category.objects.get(url=category_slug)
    # branch_categories = Category.objects.get(url=category_slug).get_descendants(include_self=True)
    branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
    current_category = categories.filter(url=category_slug).get_ancestors(include_self=True)
    # print(current_category[0].url)
    cat_url_list  = current_category
    # print(cat_url_list)
    category_products = Product.objects.filter(category__in=branch_categories).distinct()
    boat_products = Boat.objects.filter(category__in=branch_categories).distinct().order_by('price')
    # boat_list = Boat.objects.all()
    boat_filter = BoatFilter(request.GET, queryset=boat_products)
    product_filter = ProductFilter(request.GET, queryset=category_products)
    category_cats = ''
    print("show category")
    try:
        category_cats = current_category[0].get_descendants(include_self=False)
        # print(category_cats)
    except Exception as e:
        print("Ошибка category_cats:" + str(e))
    use_template = "shop/details.html"
    try:
        if current_category[0].url == 'lodki':
            use_template = "shop/details-lodki.html"
    except Exception as e:
        print("Ошибка current_category:" + str(e))
    # curr_cat = ''
    # try:
    #     curr_cat = current_category[0].url
    #     print(curr_cat)
    # except Exception as e:
    #     print("Ошибка curr_cat:" + str(e))
    # use_template = "shop/details-lodki.html"
    # if curr_cat != 'lodki':
    #     use_template = "shop/details.html"
    # else:
    #     use_template = "shop/details-lodki.html"
    #     boat_filter = BoatFilter(request.GET, queryset=category_products)
    # print(use_template)
    return render(request, use_template, {"category_list": categories,
                                          "category_products": category_products,
                                          "category_cats": category_cats,
                                          "cat_url_list": cat_url_list,
                                          "filter": boat_filter,
                                          "product_filter": product_filter,
                                          "last_category": category_slug,
                                          "sale_products": sale_products,
                                          })

def show_product(request, product_slug,category_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    # prod1 = product.get_ancestors(asceding=True, include_self=False)
    template_render = "shop/product.html"
    # print(categories.filter(name=product.category).get_ancestors(include_self=True)[0].name)

    if categories.filter(name=product.category).get_ancestors(include_self=True)[0].name == 'Лодки':
        product = Boat.objects.get(slug=product_slug)
        template_render = "shop/product-lodki.html"
    print("show_product")

    return render(request, template_render, {"product": product,
                                                           "category_list": categories, })

# def show_subcategory(request, category_slug, subcategory_slug):
#     pass
#     boats = Boat.objects.all()
#     categories = Category.objects.all()
#     # subcategories = Subcategory.objects.all()
#     # manufacturers = get_manufacturer_by_subcategory(Boat)
#     return render(request, "shop/index.html", {"boat_list": boats, "category_list": categories })