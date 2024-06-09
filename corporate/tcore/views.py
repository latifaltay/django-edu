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