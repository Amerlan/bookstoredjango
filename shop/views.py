import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View

from .models import *
# Create your views here.


class BookListView(ListView):
    paginate_by = 6

    def get_queryset(self):
        return Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        count = 0
        if self.request.user.is_authenticated:
            order = Order.objects.get(customer=self.request.user.customer, complete=False)
            for _ in OrderItem.objects.filter(order=order):
                count += _.quantity
        context['order_count'] = count
        return context

    template_name = 'shop.html'

class BookDetailView(DetailView):
    model = Book
    slug_field = 'id'
    template_name = 'product-details.html'

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        count = 0
        if self.request.user.is_authenticated:
            order = Order.objects.get_or_create(customer=self.request.user.customer, complete=False)[0]
            for _ in OrderItem.objects.filter(order=order):
                count += _.quantity
        context['order_count'] = count
        return context

class IndexView(View):
    books = Book.objects.order_by('-id')[:9]
    def get(self, request):
        count = 0
        if self.request.user.is_authenticated:
            order = Order.objects.get_or_create(customer=request.user.customer, complete=False)[0]
            for _ in OrderItem.objects.filter(order=order):
                count += _.quantity
        return render(request, 'index.html', {'books': self.books, 'order_count': count})

def updateCart(request):
    data = json.loads(request.body)
    book_id = data['product_id']
    method = data['method']
    if 'qty' in data:
        qty = data['qty']
    else:
        qty = 1
    books = Book.objects.get(id=book_id)
    order = Order.objects.get_or_create(customer=request.user.customer, complete=False)[0]
    orderItem = OrderItem.objects.get_or_create(order=order, book=books)[0]
    if method == 'add':
        orderItem.quantity += qty
    elif method == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('OK', safe=False)


def get_cart(request):
    context = {}
    if request.user.is_authenticated:
        order = Order.objects.get_or_create(customer=request.user.customer, complete=False)[0]
        orderItems = OrderItem.objects.filter(order=order)
        count = 0
        total = 0
        for _ in orderItems:
            count += _.quantity
            total += _.quantity * _.book.price
        context = {
            'order': order,
            'orderItems': orderItems,
            'order_count': count,
            'total': total
        }
    return context


def show_cart(request):
    cart_details = get_cart(request)
    return render(request, 'cart.html',
                  cart_details)

def show_checkout(request):
    context = {}
    if request.user.is_authenticated:
        order = get_cart(request)['order']
        total = get_cart(request)['total']
        qty = get_cart(request)['order_count']
        context = {
            'order': order,
            'total': total,
            'order_count': qty
        }
    return render(request, 'checkout.html', context)

def checkout_order(request):
    data = request.POST
    order = Order.objects.get(customer=request.user.customer, complete=False)
    order.recepientName = data['name'] + ' ' + data['lastname']
    order.number = data['number']
    order.address = data['address']
    order.zipCode = data['zipcode']
    order.comment = data['comment']
    order.complete = True
    order.save()
    return redirect('/')
