from django.contrib import admin
from django.urls import path, include
from univers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('about/', views.about_us, name='about'),
    path('abiturientlar/', views.abiturientlar, name='abiturientlar'),
    path('contacts/', views.contacts, name='contacts'),
    path('habarlar/', views.habarlar, name='habarlar'),
    path('meyilnamalar/', views.meyilnamalar, name='meyilnamalar')
]