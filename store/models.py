from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128, blank=True)
    category = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    price_for_view = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    image = models.ImageField(upload_to='products_images', blank=True)
    product_id = models.CharField(max_length=128, null=True, blank=True)

    def to_json(self):
        return {
            'id': self.product_id,
            'name': self.name,
            'image': str(self.image),
            'description': self.description,
            'price': str(self.price),
            # 'product_id': self.product_id,
            # преобразование поля price в строку
        }

    def __str__(self):
        return self.name


class Basket(models.Model):
    customer_id = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина : {self.product.name}'

    def sum(self):
        return int(self.product.price_for_view) * self.quantity


class PromoCode(models.Model):
    code = models.CharField(max_length=128, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class CarouselPhoto(models.Model):
    image = models.ImageField(upload_to='carousel_photos')

    def __str__(self):
        return self.image.name


class DostavkaPhoto(models.Model):
    image = models.ImageField(upload_to='dostavka_photos')

    def __str__(self):
        return self.image.name


class SpivrobitnictvoPhoto(models.Model):
    image = models.ImageField(upload_to='spivrobitnictvo_photo')

    def __str__(self):
        return self.image.name


class About_usPhoto(models.Model):
    image = models.ImageField(upload_to='about_us_photo')

    def __str__(self):
        return self.image.name


class VakansiiPhoto(models.Model):
    image = models.ImageField(upload_to='vakansii_photo')

    def __str__(self):
        return self.image.name




class Delivery_photo(models.Model):
    image = models.ImageField(upload_to='delivery_photo')

    def __str__(self):
        return self.image.name