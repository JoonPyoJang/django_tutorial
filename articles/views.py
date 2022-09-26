import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{'name':'족발', 'price': 30000},
            {'name':'햄버거', 'price': 7000},
            {'name':'치킨', 'price': 21000},
            {'name':'초밥', 'price': 16000},]
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'name':name,
        'menus':menus,
    }
    return render(request, 'dinner.html',context)