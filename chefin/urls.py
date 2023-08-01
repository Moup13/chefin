from django.contrib import admin
from django.urls import path, include
from store.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu, name='menu'),
    path('chefin/', include('store.urls')),

    path('profile/', profile, name='profile'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),

    path('baskets/remove/<int:product_id>/', basket_remove, name='basket_remove'),

    path('add_to_cart/', add_to_cart, name='add_to_cart'),

    path('search/', Search.as_view(), name='search'),

    path('inform/', inform, name='inform'),
    path('cart/info/', cart_info, name='cart_info'),
    path('zayvka/', zayvka, name='zayvka'),
    path('gotivka/', gotivka, name='gotivka'),
    path('promocod/', promocod, name='promocod'),
    path('promoprice/', promoprice, name='promoprice'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
