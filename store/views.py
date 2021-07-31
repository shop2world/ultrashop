from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from .models import *
import json
import datetime
from . 쿠키처리 import *
#추가
from django.views.generic import CreateView, DetailView,TemplateView,View
from django.contrib.auth.forms import UserCreationForm
from .forms import ProductForm


class StoreView(TemplateView):
    template_name = "store/상점.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Data = 장바구니데이타(self.request)
        cartItems = Data['cartItems']
        products = Product.objects.all()
        context['products'] = products
        context['cartItems'] = cartItems
        return context



def store(request):
    Data = 장바구니데이타(request)
    cartItems = Data['cartItems']

    products = Product.objects.all()
    context = {'products':products,'cartItems': cartItems }

    return render(request, 'store/상점.html', context)

class CartView(TemplateView):
    template_name = "store/장바구니.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Data = 장바구니데이타(self.request)
        cartItems = Data['cartItems']
        order = Data['order']
        items = Data['items']
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context



def cart(request):
    Data = 장바구니데이타(request)
    cartItems = Data['cartItems']
    order = Data['order']
    items = Data['items'] 

    context = {'items': items, 'order':order, 'cartItems': cartItems}

    return render(request, 'store/장바구니.html', context)

class CheckoutView(TemplateView):
    template_name = "store/결제.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Data = 장바구니데이타(self.request)
        cartItems = Data['cartItems']
        order = Data['order']
        items = Data['items']
        context['items'] = items
        context['order'] = order
        context['cartItems'] = cartItems
        return context


def checkout(request):
    
    Data = 장바구니데이타(request)
    cartItems = Data['cartItems']
    order = Data['order']
    items = Data['items']  

    context = {'items': items, 'order':order,'cartItems': cartItems}

    return render(request, 'store/결제.html', context)

class UpdatedItemView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)        
        productID = data['productID']
        action = data['action']        
        print('Product:', productID)
        print('Action:', action)

        customer = request.user.customer
        product = Product.objects.get(id=productID)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)   

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()



        return JsonResponse('Item added', safe =False)


def updatedItem(request):
        data = json.loads(request.body)        
        productID = data['productID']
        action = data['action']        
        print('Product:', productID)
        print('Action:', action)

        customer = request.user.customer
        product = Product.objects.get(id=productID)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
        if action == 'add':
            orderItem.quantity = (orderItem.quantity + 1)
        elif action == 'remove':
            orderItem.quantity = (orderItem.quantity - 1)   

        orderItem.save()

        if orderItem.quantity <= 0:
            orderItem.delete()



        return JsonResponse('Item added', safe =False)    



@csrf_exempt


def processOrder(request):
    #print("Data:" , request.body)
    transation_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        
        

    else:
        customer,order = 손님주문(request,data)
        

    total = float(data['form']['total'])
    order.transation_id = transation_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    
    if order.shipping == True:
        ShippingAdress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],



        )            


    return JsonResponse('Payment Completed!', safe =False) 


#추가
class RegistrationView(CreateView):
    template_name = "store/registration.html"
    form_class = UserCreationForm
    success_url = "/"

class ProductDetailView(DetailView):
    template_name = "store/product_detail.html"
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Data = 장바구니데이타(self.request)
        cartItems = Data['cartItems']
        context['cartItems'] = cartItems
        return context



class ProductAddView(CreateView):
    form_class = ProductForm
    template_name = "store/add_product.html"
    success_url = "/"        

    