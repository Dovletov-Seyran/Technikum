from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, about, abiturientlar, contacts, meyilnamalar, more_news, habarlar

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about,  name='about'),
    path('abiturientlar/', abiturientlar, name='abiturientlar'),
    path('contacts/', contacts, name='contacts'),
    path('meyilnamalar/', meyilnamalar, name='meyilnamalar'),
    path('habarlar/', habarlar, name='habarlar'),
    path('more_news', more_news, name='more_news'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
