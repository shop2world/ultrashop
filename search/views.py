from django.shortcuts import render
from store.models import Product
from django.db.models import Q

# filter 함수의 Q함수: OR조건으로 데이터를 조회하기 위해 사용하는 함수
# objects.filter() 는 특정 조건에 해당하면 객체 출력 .get('kw') 은 kw만 반환
# __icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어 있는지 검사. 사용법 "필드명"__icontains = 조건값

def searchResult(request):
    if 'kw' in request.GET:
        query = request.GET.get('kw')
        products = Product.objects.all().filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )  

    return render(request, 'search.html', {'query':query, 'products':products} )      
