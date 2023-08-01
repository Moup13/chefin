from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('rolu', rolu, name='rolu'),
    path('pizza', pizza, name='pizza'),
    path('salat', salat, name='salat'),
    path('osnovni', osnovni, name='osnovni'),
    path('soups', soups, name='soups'),
    path('zakyski', zakyski, name='zakyski'),
    path('garniry', garniry, name='garniry'),
    path('hot', hot, name='hot'),
    path('cold_drinks', cold_drinks, name='cold_drinks'),
    path('beer', beer, name='beer'),
    path('vakansii', vakansii, name='vakansii'),
    path('about_us', about_us, name='about_us'),
    path('spivrobitnictvo', spivrobitnictvo, name='spivrobitnictvo'),

    path('dostavka_ta_oplata', dostavka_ta_oplata, name='dostavka_ta_oplata'),
    path('dostavka', dostavka, name='dostavka'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)