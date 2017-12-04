from django.shortcuts import render, get_object_or_404
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import OrderCreated
from django.core.mail import send_mail
from .models import Order
from magaz import settings


def OrderCreate(request,):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            assert isinstance(cart, object)
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            subject = 'Заказ c номером {}'.format(order.id)
            message = 'Дорогой, {}, вы успешно сделали заказ.\nНомер вашего заказа {}'.format(order.first_name, order.id)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])

            request.session['order_id'] = order.id
            return render(request, 'orders/order/created.html', {'order': order})


    form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form,
                                                        })

