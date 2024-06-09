from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def merhaba(request):
    result = "Merhaba Django"
    return HttpResponse(result)

def welcome_user(request):
    user_name = "Latif Altay"
    return render(request, 'welcome_user.html', {'user_name':user_name})

def website_info(request):
    context_data={
        'name': 'Latif Altay',
        'company': 'ELEYSEC',
        'website': 'latifaltay.com'
    }
    return render(request, 'website_info.html', context_data)


def website_home(request):
    return render(request, 'website_home.html')


def category_detail_view(request, category_slug):
    return render(request, 'category_detail.html', {'category_name': category_slug})


def category_detail_view_id(request, category_id):
    return render(request, 'category_detail_id.html', {'category_id': category_id})

def category_detail_view_name(request, category_isim):
    return render(request, 'category_detail_name.html', {'category_isim': category_isim})
