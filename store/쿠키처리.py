import json
from . models import *

def 쿠키장바구니(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    except:
        cart = {}    
        print("cart:", cart)
    items = []  
    order = {'get_cart_total':0, 'get_cart_items':0,'shipping':False}  
    cartItems = order['get_cart_items'] 

    for i in cart:
        try:
            cartItems += cart[i]["quantity"]
            
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]["quantity"] )
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                    },
                'quantity':cart[i]["quantity"],   
                'get_total': total
                }

            items.append(item)    
            if product.digital == False:
                order['shipping'] = True
        except:
            pass     
    return{'items': items, 'order':order, 'cartItems': cartItems}

def 장바구니데이타(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all() 
        cartItems = order.get_cart_items
    else:
        CookieData = 쿠키장바구니(request)
        cartItems = CookieData['cartItems']
        order = CookieData['order']
        items = CookieData['items'] 
    return{'items': items, 'order':order, 'cartItems': cartItems}    

def 손님주문(request,data):
    print('사용자가 로그인 안했어요..')  
    print(data)
    print('COOKIES:',request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    print(name,email)
    cookieData = 쿠키장바구니(request)
    items = cookieData['items']
    print(items)

    customer,created = Customer.objects.get_or_create(
        email = email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product =product,
            order = order,
            quantity=item['quantity']
        ) 
    return customer,order