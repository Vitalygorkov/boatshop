from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Product, Category, Boat
from .filters import BoatFilter

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

def search_boat(request):
    print('Search_boat view')
    boat_list = Boat.objects.all()
    boat_filter = BoatFilter(request.GET, queryset=boat_list)
    categories = Category.objects.all()
    # category_products = Product.objects.filter(category__in=branch_categories).distinct()
    category_cats = Category.objects.filter(url='lodki').get_descendants(include_self=False)
    # print(category_cats)

    return render(request, "shop/details-lodki.html", {"category_list": categories,
                                          # "category_products": category_products,
                                          "category_cats": category_cats,
                                          "filter": boat_filter,})

def search_boat_category(request, category_slug):
    boat_list = Boat.objects.all()
    boat_filter = BoatFilter(request.GET, queryset=boat_list)
    categories = Category.objects.all()
    #categoryID = Category.objects.get(url=category_slug)
    # branch_categories = Category.objects.get(url=category_slug).get_descendants(include_self=True)
    branch_categories = Category.objects.filter(url=category_slug).get_descendants(include_self=True)
    current_category = categories.filter(url=category_slug).get_ancestors(include_self=True)
    # print(current_category[0].url)
    cat_url_list  = current_category
    print(cat_url_list)
    print('lodki-search category')

    category_products = Product.objects.filter(category__in=branch_categories).distinct()
    try:
        category_cats = current_category[0].get_descendants(include_self=False)
        # print(category_cats)
    except Exception as e:
        print("Ошибка:" + str(e))
    use_template = "shop/details.html"
    if current_category[0].url != 'lodki':
        use_template = "shop/details.html"
    else:
        use_template = "shop/details-lodki-search.html"
        print('lodki-search template')
    print(use_template)
    return render(request, use_template, {"category_list": categories,
                                          "category_products": category_products,
                                          "category_cats": category_cats,
                                          "cat_url_list": cat_url_list,
                                          "filter": category_products,})


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
    boat_products = Boat.objects.filter(category__in=branch_categories).distinct()
    # boat_list = Boat.objects.all()
    boat_filter = BoatFilter(request.GET, queryset=boat_products)
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
                                          "filter": boat_filter,})

def show_product(request, product_slug,category_slug):
    categories = Category.objects.all()
    product = Product.objects.get(slug=product_slug)
    # prod1 = product.get_ancestors(asceding=True, include_self=False)
    template_render = "shop/product.html"
    # print(categories.filter(name=product.category).get_ancestors(include_self=True)[0].name)

    if categories.filter(name=product.category).get_ancestors(include_self=True)[0].name == 'Лодки':
        product = Boat.objects.get(slug=product_slug)
        template_render = "shop/product-lodki.html"


    return render(request, template_render, {"product": product,
                                                           "category_list": categories, })

# def show_subcategory(request, category_slug, subcategory_slug):
#     pass
#     boats = Boat.objects.all()
#     categories = Category.objects.all()
#     # subcategories = Subcategory.objects.all()
#     # manufacturers = get_manufacturer_by_subcategory(Boat)
#     return render(request, "shop/index.html", {"boat_list": boats, "category_list": categories })