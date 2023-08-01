from django.contrib import admin
from .models import *
from django.utils.translation import gettext as _

# Register your models here.

admin.site.register(Product)
admin.site.register(Basket)



@admin.register(CarouselPhoto)
class CarouselPhotoPhotoAdmin(admin.ModelAdmin):
    verbose_name = _('Фото для Карусели')
    verbose_name_plural = _('Фотографии для Карусели')


@admin.register(Delivery_photo)
class Delivery_photoPhotoAdmin(admin.ModelAdmin):
    verbose_name = _('Фото для доставки')
    verbose_name_plural = _('Фотографии для доставки')


@admin.register(SpivrobitnictvoPhoto)
class SpivrobitnictvoPhotoAdmin(admin.ModelAdmin):
    verbose_name = _('Фото для співробітництва')
    verbose_name_plural = _('Фотографії для співробітництва')


@admin.register(About_usPhoto)
class About_usPhotoAdmin(admin.ModelAdmin):
    verbose_name = _('Фото для "Про нас"')
    verbose_name_plural = _('Фотографії для "Про нас"')


@admin.register(VakansiiPhoto)
class VakansiiPhotoAdmin(admin.ModelAdmin):
    verbose_name = _('Фото для вакансій')
    verbose_name_plural = _('Фотографії для вакансій')
