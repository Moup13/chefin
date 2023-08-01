from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.views.generic import ListView

from chefin.settings import POSTER_POS_API_KEY
from django.shortcuts import render
from .helpers import *
from .models import *
import requests
from chefin.settings import POSTER_POS_API_KEY
from cloudipsp import Api, Checkout
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .helpers import *
from .models import *
from store.templatetags.custom_filters import mul_price
from django.http import JsonResponse
from django.shortcuts import redirect
from django.core.cache import cache
from decimal import Decimal
import json
from django.http import HttpResponseBadRequest
from twilio.rest import Client
import re


def vakansii(request):
    vakansii_photo = VakansiiPhoto.objects.all()
    context = {
        'title': 'Про нас',
        'vakansii_photo': vakansii_photo,
    }

    return render(request, 'store/vakansii.html', context)


def about_us(request):
    about_us_photo = About_usPhoto.objects.all()
    context = {
        'title': 'Про нас',
        'about_us_photo': about_us_photo,
    }

    return render(request, 'store/about_us.html', context)


def spivrobitnictvo(request):
    spivrobitnictvo_photo = SpivrobitnictvoPhoto.objects.all()
    context = {
        'title': 'Співробітництво',
        'spivrobitnictvo_photo': spivrobitnictvo_photo,
    }

    return render(request, 'store/spivrobitnictvo.html', context)


def dostavka_ta_oplata(request):
    dostavka_photos = DostavkaPhoto.objects.all()
    context = {
        'title': 'Доставка та оплата',
        'dostavka_photos': dostavka_photos,
    }

    return render(request, 'store/dostavka_ta_oplata.html', context)

def dostavka(request):
    delivery_photo = Delivery_photo.objects.all()
    context = {
        'title': 'Доставка та оплата',
        'delivery_photo': delivery_photo,
    }

    return render(request, 'store/dostavka.html', context)


def menu(request):
    api_key = POSTER_POS_API_KEY
    fill_database(api_key)

    query = request.GET.get('query')
    category = request.GET.get('category')

    products = Product.objects.all()

    if query:
        products = products.filter(name__icontains=query)

    if category:
        products = products.filter(category__icontains=category)

    carousel_photos = CarouselPhoto.objects.all()

    context = {
        'title': 'Chefin',
        'products': products,
        'product_id': products.values_list('product_id', flat=True),
        'carousel_photos': carousel_photos,
    }

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Если заголовок 'HTTP_X_REQUESTED_WITH' содержит значение 'XMLHttpRequest',
        # то это может быть AJAX-запрос
        product_data = []
        for product in products:
            product_data.append({
                'name': product.name,
                'category': product.category,
                # Добавьте другие поля продукта, которые вам необходимы
            })
        return JsonResponse({'products': product_data})

    return render(request, 'store/base.html', context)


def pizza(request):
    products = Product.objects.all()

    query = request.GET.get('query')
    category = request.GET.get('category')
    if query:
        print("query")
        products = products.filter(name__icontains=query)

    if category:
        print("category")
        products = products.filter(category__icontains=category)

    context = {
        'title': 'Піца',
        'products': products,
        'product_id': products.values_list('product_id', flat=True),
    }

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Если заголовок 'HTTP_X_REQUESTED_WITH' содержит значение 'XMLHttpRequest',
        # то это может быть AJAX-запрос
        product_data = []
        for product in products:
            product_data.append({
                'name': product.name,
                'category': product.category,
                # Добавьте другие поля продукта, которые вам необходимы
            })
            print("meta")
        return JsonResponse({'products': product_data})

    return render(request, 'store/pizza.html', context)


def rolu(requests):
    products = Product.objects.all()

    context = {
        'title': 'Роли',
        'products': products,
    }

    return render(requests, 'store/rolu.html', context)


def salat(requests):
    products = Product.objects.all()

    context = {
        'title': 'Салати',
        'products': products,
    }

    return render(requests, 'store/salat.html', context)


def osnovni(requests):
    products = Product.objects.all()

    context = {
        'title': 'Основні страви',
        'products': products,
    }

    return render(requests, 'store/osnovni.html', context)


def soups(requests):
    products = Product.objects.all()

    context = {
        'title': 'Супи',
        'products': products,
    }

    return render(requests, 'store/soups.html', context)


def zakyski(requests):
    products = Product.objects.all()

    context = {
        'title': 'Закуски',
        'products': products,
    }

    return render(requests, 'store/zakyski.html', context)


def garniry(requests):
    products = Product.objects.all()

    context = {
        'title': 'Гарніри',
        'products': products,
    }

    return render(requests, 'store/garniry.html', context)


def hot(requests):
    products = Product.objects.all()

    context = {
        'title': 'Гарячі страви',
        'products': products,
    }

    return render(requests, 'store/hot.html', context)


def cold_drinks(requests):
    products = Product.objects.all()

    context = {
        'title': 'Холодні напої',
        'products': products,
    }

    return render(requests, 'store/cold_drinks.html', context)


def beer(requests):
    products = Product.objects.all()

    context = {
        'title': 'Розливне пиво',
        'products': products,
    }

    return render(requests, 'store/beer.html', context)


def dostavka_ta_oplata(requests):
    context = {
        'title': 'Доставка та оплата',

    }

    return render(requests, 'store/dostavka_ta_oplata.html', context)


def cart_info(request):
    # Получение текущей корзины из сессии пользователя
    basket = request.session.get('basket', {})
    basket_items = []
    for product_id, item in basket.items():
        item['id'] = product_id
        basket_items.append(item)

    # Получение списка значений product_poster из товаров в корзине
    product_posters = [item['product_poster'] for item in basket_items]

    # Возврат информации о товарах в корзине в формате JSON
    return JsonResponse({'items': basket_items, 'product_posters': product_posters})


def basket_add(request, product_id):
    # Получение данных из тела запроса
    data = json.loads(request.body)
    comment = data.get('comment')
    product_poster = data.get('product_poster')
    price = data.get('price')
    name = data.get('name')
    image = data.get('image')
    description = data.get('description')
    skidka = data.get('skidka')
    category = data.get('category')
    # print('category_basket_add',category)

    # Создание JSON-представления товара с комментарием и постером
    product_json = {
        'comment': comment,
        'product_poster': product_poster,
        'price': price,
        'name': name,
        'image': image,
        'description': description,
        'skidka': skidka,
        'category': category,
    }

    # Получение или инициализация корзины в сессии пользователя
    basket = request.session.get('basket', {})

    # Проверка, что товар уже присутствует в корзине
    if str(product_id) in basket:
        return JsonResponse({'success': False, 'message': 'Product already exists in the basket.'})

    # Добавление товара в корзину
    basket[str(product_id)] = product_json

    # Сохранение значения category в сессии
    request.session['category'] = category

    # Обновление корзины в сессии пользователя
    request.session['basket'] = basket
    request.session.modified = True

    return JsonResponse({'success': True})


def zayvka(request):
    category = request.session.get('category', None)

    print("category", category)
    context = {
        'category': category,
    }
    return render(request, 'store/zayvka.html', context)


def promocod(request):
    data = json.loads(request.body)
    promocod = data.get('promocod')

    try:
        promo_code = PromoCode.objects.get(code=promocod)
        discount = promo_code.discount
        response_data = {'success': True, 'discount': discount}
    except PromoCode.DoesNotExist:
        response_data = {'success': False}

    return JsonResponse(response_data)


def promoprice(request):
    request.session['basket'] = {}
    request.session.modified = True

    return JsonResponse({'success': True})


def basket_remove(request, product_id):
    # Получение текущей корзины из сессии пользователя
    basket = request.session.get('basket', {})

    # Проверка, что товар с данным ID присутствует в корзине
    if str(product_id) in basket:
        del basket[str(product_id)]
        request.session['basket'] = basket
        request.session.modified = True

        return JsonResponse({'success': True})

    return JsonResponse({'success': False, 'message': 'Product not found in the basket.'})


def profile(request):
    # Получаем текущую корзину из сессии пользователя
    basket = request.session.get('basket', {})
    basket_items = []
    for product_id, item in basket.items():
        item['id'] = product_id
        basket_items.append(item)

    context = {
        'title': 'Корзина',
        'baskets': basket_items,
        'mul_price': mul_price,
        'savedValue': 1,
    }

    return render(request, 'store/baskets.html', context)


global_data = {}


def inform(request):
    global global_data

    if request.method == 'POST':
        try:
            body = json.loads(request.body.decode('utf-8'))
            value = body.get('value')
            basketIds = body.get('basketIds')
            totalPriceElement = body.get('totalPriceElement')
            comment = body.get('comments')
            name_po_id = body.get('name')
            skidka = body.get('skidka')
            category = body.get('category')
            print('комент')
            print(comment)

            request.session['category'] = category
            if basketIds is not None:
                # Обработка значения quantity
                # ...

                # Создание словаря
                global_data = {
                    'value': value,
                    'basketIds': basketIds,
                    'totalPriceElement': totalPriceElement,
                    'comment': comment,
                    'name_po_id': name_po_id,
                    'skidka': skidka,
                    'category': category,

                }

                # Возвращаем успешный словарь с данными
                # return {'status': 'success', 'data': global_data}
                return JsonResponse({'status': 'success', 'data': global_data})

        except json.JSONDecodeError:
            pass

    # Возвращаем JSON-ответ об ошибке
    return {'status': 'error', 'message': 'Ошибка'}


def some_view(request, name, number, street, home_number, home_gear, home_room, delivery_time, delivery_count,
              comment_do_zakaza, cassa_type, type_rozrahynky, type_dostavki, dont_call):
    address = f'{street} {home_number}'
    if home_gear:
        address += f' поверх:{home_gear}'
    if home_room:
        address += f' квартира:{home_room}'

    url = 'https://joinposter.com/api/incomingOrders.createIncomingOrder?token=847348:69182830ed3e1fbe65630bb6152856fb'

    # Получение данных из global_data
    basket_ids = global_data['basketIds']
    values = global_data['value']
    comment = global_data['comment']
    name_po_id = global_data['name_po_id']
    totalPriceElement = global_data['totalPriceElement']
    totalPriceElement = str(totalPriceElement.replace('.', ''))
    skidka = global_data['skidka']
    category = global_data['category']

    print('category', category)

    # print("skidka=",skidka)
    # print("skidka=",type(skidka))

    products = []

    for basket_id, value, comment, name_po_id in zip(basket_ids, values, comment, name_po_id):
        product = {
            'product_id': int(basket_id),
            'count': int(value),
            'comment': str(comment),
            'name_po_id': str(name_po_id),

        }
        products.append(product)
    oplata_gotivkoi = 'Оплата: Готівкою при отриманні, '
    oplata_online = 'Оплата: Онлайн, '
    oplata_kartoi_pri_poluchenii = 'Оплата: Сплатити картою при отриманні, '

    if type_dostavki == '3':
        cassa_type = '2'

    if dont_call == None:
        print("звонить")
    else:
        dont_call = ", Мені можна не телефонувати для підтвердження замовлення"

    # if skidka:
    #     discount = int(totalPriceElement) * (skidka / 100)
    #     totalPriceElement = int(totalPriceElement) - discount
    #
    #     discount = int(totalPriceElement) * (skidka / 100)
    #     discounted_price = int(totalPriceElement) - discount
    #
    # print(discounted_price)

    spot_id = 2 if "Піца" in category else 1

    if cassa_type == '1':

        if type_rozrahynky == '1':
            comment_obsh = oplata_gotivkoi  # Сначала добавляем значение oplata_gotivkoi
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call
            print("spot_id = 2")
            incoming_order = {
                'spot_id': 2,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,
                'service_mode': type_dostavki,
                "comment": comment_obsh,

                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            promoprice(request)
            print(response.text)

        if type_rozrahynky == '2' or type_rozrahynky == None:
            comment_obsh = oplata_online
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call

            incoming_order = {
                'spot_id': 2,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,
                'service_mode': type_dostavki,
                "payment": {
                    "sum": totalPriceElement,
                    "currency": "UAH",
                    "type": 1
                },
                "comment": comment_obsh,

                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            promoprice(request)
            print(response.text)

        if type_rozrahynky == '3':
            comment_obsh = oplata_kartoi_pri_poluchenii  # Сначала добавляем значение oplata_gotivkoi
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call

            incoming_order = {
                'spot_id': 2,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,
                'service_mode': type_dostavki,
                "comment": comment_obsh,

                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            promoprice(request)
            print(response.text)

    else:
        if type_rozrahynky == '1':
            comment_obsh = oplata_gotivkoi  # Сначала добавляем значение oplata_gotivkoi
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call

            print("spot_id = 1")
            incoming_order = {
                'spot_id': spot_id,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,

                'service_mode': str(type_dostavki),
                "comment": comment_obsh,
                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            promoprice(request)
            print(response.text)

        if type_rozrahynky == '2' or type_rozrahynky == None:
            comment_obsh = oplata_online
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call

            incoming_order = {
                'spot_id': spot_id,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,
                'service_mode': type_dostavki,
                "payment": {
                    "sum": totalPriceElement,
                    "currency": "UAH",
                    "type": 1
                },
                "comment": comment_obsh,

                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            promoprice(request)
            print(response.text)

        if type_rozrahynky == '3':
            comment_obsh = oplata_kartoi_pri_poluchenii  # Сначала добавляем значение oplata_gotivkoi
            comment_obsh += ''.join(
                [f"{product['name_po_id']}: {product['comment']}, " for product in products if product['comment']])
            if comment_do_zakaza:
                comment_obsh += f'Комментарий из заявки: {comment_do_zakaza}, Кількість персон: {delivery_count}'
            if delivery_count:
                comment_obsh += f'Кількість персон: {delivery_count}'
            if dont_call:
                comment_obsh += dont_call

            print("spot_id = 1")
            incoming_order = {
                'spot_id': spot_id,
                'phone': number,
                'delivery_time': delivery_time,
                'products': products,
                'service_mode': type_dostavki,
                "comment": comment_obsh,
                "first_name": name,
                "address": address

            }
            headers = {'Content-Type': 'application/json'}

            response = requests.post(url, data=json.dumps(incoming_order), headers=headers)
            print(response.text)

            # account_sid = "AC84773f43db66f087b9c2b2faf7d3071e"
            # account_token = "b72489f848397ac65db40168dffdabfd"
            # sender = '+13254409650'
            # receiver = '+380667096085'
            # new_total_price_element = str(totalPriceElement)[:-2]
            # text = f'Ваше зомвлення прийнято на сумму {new_total_price_element} грн'
            #
            # client = Client(account_sid, account_token)
            #
            # message = client.messages.create(
            #     body=text,
            #     from_=sender,
            #     to=receiver
            # )
            promoprice(request)
            print('Собшения отправлено')

    return redirect('menu')

def is_valid_number(number):
    print("валидатор сработал")
    # Add your custom validation logic here
    # For example, check if the number follows a specific pattern
    # If the number is valid, return True; otherwise, return False
    # Replace the condition below with your actual validation logic
    return len(number) == 10
def gotivka(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        home_gear = request.POST.get('home_gear')
        home_room = request.POST.get('home_room')
        delivery_time = request.POST.get('delivery_time')
        delivery_count = request.POST.get('delivery_count')
        comment_do_zakaza = request.POST.get('comment_do_zakaza')
        cassa_type = request.POST.get('checker_zaklad1')

        type_rozrahynky = request.POST.get('type_rozrahynky')
        type_dostavki = request.POST.get('type_dostavki')

        dont_call = request.POST.get('dont_call')
        print('пошло дело')
        print(type_dostavki)
        if type_dostavki == '1' or type_dostavki == '2' or type_dostavki == '3':
            pattern = r'^\+\d{12}$'  # The pattern checks for exactly 13 characters, starting with "+"
            print(street)
            print(home_number)
            if type_dostavki == '2' or type_dostavki == '1':
                if re.match(pattern, number):
                    print('dont_call', dont_call)
                    inform(request)
                    some_view(request, name, number, street, home_number, home_gear, home_room, delivery_time, delivery_count,
                              comment_do_zakaza, cassa_type, type_rozrahynky, type_dostavki, dont_call)
                    return redirect('/')
                else:
                    validator = 2
                    return render(request, 'store/zayvka.html', {'validator': validator})
            elif type_dostavki == '3':
                if re.match(pattern, number) and street != '' and home_number != '':
                    print('dont_call', dont_call)
                    inform(request)
                    some_view(request, name, number, street, home_number, home_gear, home_room, delivery_time, delivery_count,
                              comment_do_zakaza, cassa_type, type_rozrahynky, type_dostavki, dont_call)
                    return redirect('/')
                else:
                    validator = 1
                    return render(request, 'store/zayvka.html', {'validator': validator})
        else:
            validator = 1
            return render(request, 'store/zayvka.html', {'validator': validator})


def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        street = request.POST.get('street')
        home_number = request.POST.get('home_number')
        home_gear = request.POST.get('home_gear')
        home_room = request.POST.get('home_room')
        delivery_time = request.POST.get('delivery_time')
        delivery_count = request.POST.get('delivery_count')
        comment_do_zakaza = request.POST.get('comment_do_zakaza')
        cassa_type = request.POST.get('checker_zaklad1')
        type_rozrahynky = '2'
        type_dostavki = request.POST.get('type_dostavki')

        print('пошло дело add_to_cart')
        print(type_rozrahynky)

        print("---------------")

        global_data['name'] = name
        global_data['number'] = number
        global_data['street'] = street
        global_data['home_number'] = home_number
        global_data['home_gear'] = home_gear
        global_data['home_room'] = home_room
        global_data['delivery_time'] = delivery_time
        global_data['delivery_count'] = delivery_count
        global_data['comment_do_zakaza'] = comment_do_zakaza
        global_data['cassa_type'] = cassa_type
        global_data['type_rozrahynky'] = type_rozrahynky
        global_data['type_dostavki'] = type_dostavki

        # for i,j in global_data.items():
        #     print(i,j)

        price = global_data['totalPriceElement']
        price = str(price.replace('.', ''))

        api = Api(merchant_id=1396424, secret_key='test')
        checkout = Checkout(api=api)
        data = {
            "currency": "UAH",
            "amount": price,

        }
        url = checkout.url(data).get('checkout_url')

        return redirect(url)


def fondy_callback(request):
    if request.method == 'POST':
        # Получение данных об обратном вызове от Фонди
        status = request.POST.get('order_status')
        payment_id = request.POST.get('payment_id')
        # Другие необходимые данные об оплате

        name = global_data.get('name')
        number = global_data.get('number')
        street = global_data.get('street')
        home_number = global_data.get('home_number')
        home_gear = global_data.get('home_gear')
        home_room = global_data.get('home_room')
        delivery_time = global_data.get('delivery_time')
        delivery_count = global_data.get('delivery_count')
        comment_do_zakaza = global_data.get('comment_do_zakaza')
        cassa_type = global_data.get('cassa_type')
        type_rozrahynky = request.POST.get('type_rozrahynky')
        type_dostavki = request.POST.get('type_dostavki')

        # Проверка статуса оплаты
        if status == 'approved':
            inform(request)
            some_view(request, name, number, street, home_number, home_gear, home_room, delivery_time, delivery_count,
                      comment_do_zakaza, cassa_type, type_rozrahynky, type_dostavki)
            return redirect('/')

    # Если оплата неуспешна или другой метод запроса, верните HTTP-ответ с кодом 400 (Bad Request)
    return HttpResponse(status=400)


class Search(ListView):
    template_name = 'store/search_results.html'
    context_object_name = 'news'
    paginate_by = 45

    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        if query:
            self.queryset = Product.objects.filter(Q(name__icontains=query) | Q(category__icontains=query))
            if self.queryset.exists():
                # Получаем все объекты соусов из модели Product
                sauces = Product.objects.filter(category='Cоус')
                saucesrol = Product.objects.filter(category='Соус роли')
                # Передаем соусы в контекст данных
                return render(request, self.template_name, {'news': self.queryset, 'sauces': sauces, 'saucesrol': saucesrol,})
        return redirect('menu')
