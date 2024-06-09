from django.urls import path
from .views import index, about, merhaba, welcome_user, website_info, website_home, category_detail_view, category_detail_view_id, category_detail_view_name

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('merhaba', merhaba, name="merhaba"),
    path('welcome_user', welcome_user, name='welcome_user'),
    path('website_info', website_info, name='website_info'),
    path('home', website_home, name='home'),
    path('category/<slug:category_slug>/', category_detail_view, name='category_detail_view'),
    path('categoryid/<int:category_id>/', category_detail_view_id, name='category_detail_view_id'),
    path('categoryisim/<str:category_isim>/', category_detail_view_name, name='category_detail_view_name'),
]
