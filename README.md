# 샵투월드 오픈소스 무료 한국형 쇼핑몰 프로젝트


누구나 가질 수 있는 쇼핑몰!초간단 오픈소스 장고 쇼핑몰!쇼핑몰 복잡할 필요 없다.물건 팔면 된다.

-------------

삶의 주축이 온라인이 된 시대 , 그러나 쇼핑몰 운영을 위해
호스팅, 도메인, 프로그램 사용료 등 매달 돈이 듭니다.


온라인 시대에도 누구나 온라인 쇼핑몰을 못가지던 이유
-------------
```
유지비.(호스팅, 도메인, 프로그램 사용료 등)
복잡한 사용법을 별도로 배워야 함.
```

샵투월드의 오픈소스 쇼핑몰 프로젝트는 무료 호스팅을 기반으로
강력한 장고 기반의 오픈소스 쇼핑몰을 구현해 갑니다.


초보자도 쉽게 설치하는 설치가이드 =>
샵투월드 한국형 오픈 소스 초간단 울트라쇼핑몰 - 무료 웹호스팅 이용 쇼핑몰 운영하기
[누구나 가지는 무료 호스팅 장고 쇼핑몰 따라 만들기(유튜브)](https://youtu.be/2C0HY57eIac)

[결과물: 울트라 쇼핑몰](https://shop2world.pythonanywhere.com/)

쇼핑몰 시작 준비물
-------------
```
결제 처리를 위한 페이팔 이메일
https://developer.paypal.com/developer/applications/
```

쇼핑몰 실제 사용 예
-------------
```
레슨비 결제를 위한 쇼핑몰
건설 배관 등 서비스업 결제 처리를 쇼핑몰
기타 등등 무궁 무진
```

쇼핑몰 무료 호스팅 이용 설치 방법
-------------

[설치 방법 동영상 안내](https://youtu.be/2C0HY57eIac)

```
1 다운로드
git clone https://github.com/shop2world/ultrashop.git

2가상환경 만들기
python3 -m venv venv

3가상환경 실행시키기
source venv/bin/activate

4 디렉토리 이동 
cd ultrashop

5 디팬던시 설치 - 조금 시간 걸림(몇분)
pip install -r requirements.txt

6 파이썬 버전 확인
python --version

7 앱 만들기 시작 - 뱀눌러 Web > Add new web app>Manual Configration

8python 버전 선택

9셋팅
Source code: 콘솔에서 pwd 로 현재 디렉토리 확인 /home/shop2world/ultrashop
Working directory: /home/shop2world/ultrashop

10 Virtualenv 폴더 확인 후 지정
Virtualenv:
/home/shop2world/venv

10  셋팅 파일(settings.py) 수정  위한 이동
/home/본인ID/ultrashop/shop2shop/settings.py


시큐리티키
settings.py
SECRET_KEY = ''

여러분 도메인 넣기 (단따옴표) 사용

예)
ALLOWED_HOSTS = ['shop2world.pythonanywhere.com']



11Static files
python manage.py collectstatic
(venv) 20:47 ~/ultrashop (master)$ python manage.py collectstatic
155 static files copied to '/home/본인ID/ultrashop/staticfiles'.

12 WSGI configuration file: 
아래 내용 복사해서 그대로 붙여 넣기
```

``` C

# +++++++++++ DJANGO +++++++++++
# To use your own Django app use code like this:
import os
import sys

# assuming your Django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'shop2shop.settings'

## Uncomment the lines below depending on your Django version
###### then, for Django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older Django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

```
```
13 자물쇠 보안 
Forcing HTTPS => Enabled

14 어드민 접속
자신의 도메인뒤에 admin붙이면 됨
예)
https://shop2world.pythonanywhere.com/admin/

15 어드민 관련 설명
상품 등록 삭제 작업 : Products
주문된 주문 확인: Order items
배송주소:Shipping adress
고객:Customers
가입한 회원 :사용자(들)
댓글:Comments


16페이팔 API 키 적용


My apps & credentials
https://developer.paypal.com/developer/applications/

/home/shop2world/ultrashop/store/templates/store/결제.html

```




또한 이 쇼핑몰은 누구나 쉽게 배워서 원하는 기능을 레고처럼 쉽게
추가해 나갈 수 있습니다.
예를 들어 상품 댓글을 레고처럼 추가하시고 싶으신 분은
다음의 강의를 참고하시면 됩니다.
[장고 댓글 만들기](https://youtu.be/4ydUqjSB6yw)
마찬가지로 검색기능을 추가하고 싶으면 다음의 강의를 참고하시면 됩니다.
[장고 검색 만들기](https://youtu.be/BeyCNjG-vUU)


주요 기능과 특징
-------------
  
  ```
  페이팔 클라이언트ID만 넣으면 즉시 결제 처리가 가능한 완성된 쇼핑몰
  샵투페이(https://shop2pay.net) 형태의 단순 명료한 구조로 누구나 쉽게 운영과 확장 가능.
  로그인, 회원가입, 로그아웃, 장바구니로 향할 수 있는 메뉴가 있습니다.
  회원가입이나 로그인 하지 않으 비회원의 주문 처리도 가능합니다.
  상품의 사진과 관리자가 지정한 상품의 이름과 설명이 포함됩니다.
  수량을 선택할 수 있고, 선택한 제품을 장바구니에 담고 결제로 진행 할 수 있습니다.
  선택한 상품의 수량에 따라 가격을 정해 구매할 수 있습니다.
  레트로 풍의 친근한 디자인
  ```

부가 기능
-------------
```
  댓글은 공유삭제 기능으로 관리자가 승인 안한 스팸 댓글은 회원끼리 제거 처리하는 재미를 드립니다.
```





물음표에 도전한다. 누구나 배워 스스로 원하는 기능을 만든다. 강의형 오픈소스 쇼핑몰
-------------
또한 여러분은 배워서 이 쇼핑몰을 기본 부터 여러분의 것으로 만들어 갈 수 있습니다.
관련 왕초보 분을 위한 파이썬 장고 강의 안내입니다.
이 강의는 기존 실전 장고 쇼핑몰 강의에 어려움이 있는
장고 초보자분을 위해 기초 부터 진행됩니다.

샵투월드의 오픈소스 한국형 장고 쇼핑몰 프로젝트를 기반으로
진행되며
핵심 기능부터 기초부터 시작되기 때문에
레고처럼 여러분들은 쇼핑몰들의 기능을 추가해 갈 수 있습니다.

여러분은 강의가 끝나면 호스팅 서버에 쇼핑몰을 운영하실 수 있으며
핵심 기능들을 익히므로 추가 기능들을 계속 이해할 수 있습니다.

[왕초보 파이썬 장고 (Python Django) 쇼핑몰 따라 만들기](https://www.shop2school.com/course/%ec%99%95%ec%b4%88%eb%b3%b4-%ed%8c%8c%ec%9d%b4%ec%8d%ac-%ec%9e%a5%ea%b3%a0-python-django-%ec%87%bc%ed%95%91%eb%aa%b0-%eb%94%b0%eb%9d%bc-%eb%a7%8c%eb%93%a4%ea%b8%b0/)

<img src="https://www.shop2school.com/wp-content/uploads/2021/07/logo768500.jpg" alt="왕초보 파이썬 장고 (Python Django) 쇼핑몰 따라 만들기"></img>

