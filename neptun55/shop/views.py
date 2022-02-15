from django.shortcuts import render
from django.views.generic.base import View
from .models import Boat


class BoatsView(View):
    # Список лодок
    def get(self, request):
        boats = Boat.objects.all()
        return render(request, "shop/index.html", {"boat_list": boats})
