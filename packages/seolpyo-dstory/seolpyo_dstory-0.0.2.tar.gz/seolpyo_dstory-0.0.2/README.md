# 프로젝트 문의 / 제안
프로젝트와 관련한 내용은 <https://django.seolpyo.com/>에 이야기해주시면 감사합니다.

또한 패키지의 상세 설명을 설표의장고 사이트에서 확인하실 수 있습니다.

# 프로젝트 설명
패키지명은 Django + Tistory를 합친 DSTORY(디스토리)로 명명했습니다.


## 프로젝트의 목적
백업파일을 이용하여 티스토리 블로그에 작성한 글들을 Django로 이전하여 운영할 수 있도록 합니다.

티스토리와 동일한 url 구조(숫자 주소 + 문자 주소 + rss + 사이트맵)를 사용합니다.

태그, 카테고리, 공지사항, 서식, 페이지 정보를 가져올 수 있으며, 티스토리 블로그 로그인 정보를 이용해 임의로 설정한 문자 주소, 보호 글의 비밀번호 등의 정보도 가져올 수 있습니다.

# 사용방법
## 패키지 설치
디스토리 패키지를 설치합니다.

tqdm, requests, bs4(BeautifulSoup), selenium, django, django-summenote 패키지가 함께 설치됩니다.
```
>> pip install seolpyo-dstory
```

## 장고 프로젝트 생성
mysite라는 폴더를 생성하고, 폴더 안에 장고 프로젝트를 생성합니다.
```
>> mkdir mysite
>> cd mysite
>> django-admin startproject config .
```

## 기초 설정
1. mysite > config 에 settings 폴더를 만든 다음, settings.py를 settings 폴더로 이동시킵니다.
1. mysite > config > settigns 폴더에 ```__init__.py``` 를 만들고, 다음과 같이 작성합니다.

seolpyo_dsotry.settings 파일은 장고의 기초설정을 빠르게 하기 위해 작성된 파일입니다.
```
# config/settings/__init__.py
from .settings import *
from seolpyo_dstory.settings import *

BASE_DIR = BASE_DIR.parent
for i in apps:
  if i not in INSTALLED_APPS: INSTALLED_APPS.append(i)

TEMPLATES[0]['OPTIONS']['context_processors'].append(processor)
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```


※ 별도의 이용자 모델이 있는 경우, AUTH_USER_MODEL 선언해주어야 합니다. 위 설정을 사용하면 'seolpyo_dstory.User'를 사용하게 됩니다.

## 손쉬운 애드센스 코드 추가
애드센스를 사용하려는 경우, 다음과 같이 ca-pub 번호를 추가하면 됩니다.

ca-pub 번호를 추가하는 것으로 head 영역의 script 태그를 추가하고, ads.txt 페이지를 생성합니다.

예를 들어 ca-pub번호가 ca-pub-123456789라면 다음과 같이 설정하면 됩니다.
```
# config/settings.py
DSTORY_CONTEXT['adsense'] = '123456789'
```

## 손쉬운 구글 애널리틱스 코드 추가
구글 애널리틱스를 사용하는 경우

예를 들어 측정ID가 G-A1B2C3D4라면 다음과 같이 설정하면 됩니다.
```
# config/settings.py
DSTORY_CONTEXT['ga'] = 'A1B2C3D4'
```

구글 태그매니저를 사용하는 경우

예를 들어 컨테이너ID가 GTM-X1Y2Z3라면 다음과 같이 설정하면 됩니다.
```
# config/settings.py
DSTORY_CONTEXT['gtm'] = 'X1Y2Z3'
```

## 손쉬운 네이버 사이트 인증
네이버 웹마스터도구에서 html 파일 업로드를 선택한 다음, 요구하는 url의 코드 번호를 삽입합니다.
예를 들어 요구하는 url이 naverA1B2C3D4E5F6G7H8I9.html이라면 다음과 같이 설정하면 됩니다.
```
# config/settings.py
DSTORY_NAVER = 'A1B2C3D4E5F6G7H8I9'
```

## urls.py 변경하기

mysite > config > urls.py를 열어 내용을 다음과 같이 변경합니다.
```
# config/urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('seolpyo_dstory.urls')),
]

if not settings.DEBUG:
    handler400 = 'seolpyo_dstory.views.handler'
    handler403 = 'seolpyo_dstory.views.handler'
    handler404 = 'seolpyo_dstory.views.handler'
    handler500 = 'seolpyo_dstory.views.handler'

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static('media/', document_root=(settings.BASE_DIR / 'media/'))
```

## 마이그레이션
관리자를 추가하기 위해 마이그레이션을 생성하고, 적용합니다.
```
>> python manage.py makemigrations
>> python manage.py migrate
```

### 관리자 추가하기
티스토리 백업파일을 이용한 복구에는 관리자 계정이 필요합니다.

createsuperuser 명령을 통해 관리자를 추가합니다.

user 생성시 비밀번호를 입력하더라도 마스킹 문자(*)가 노출되지 않을 수 있습니다.
```
>> python manage.py createsuperuser
```

## 티스토리 백업파일을 이용해 글 복구하기
이 패키지는 티스토리 블로그 이사를 위한 2가지 방법을 제공합니다.

하나는 백업파일만을 이용한 단순 복구, 다른 하나는 백업파일과 티스토리 블로그에 접속해 공개설정, 비밀번호, 문자 주소 등의 정보를 가져와 적용하는 것입니다.

티스토리 백업파일은 글의 공개 여부나 보호글의 비밀번호, 임의로 설정한 문자 주소 정보를 제공하지 않습니다.

다운로드한 티스토리 백업파일을 mysite 폴더에 이동시킨 다음, tistory.zip이라는 이름으로 변경합니다.

### 백업파일을 통한 단순복구
장고 shell을 실행하고, 다음 명령어를 입력합니다.
```
>> python manage.py shell
>> from seolpyo_dstory.utils import restore as r
>> r()
```

### 백업파일과 티스토리 블로그를 통한 복구
장고 shell을 실행하고, 다음 명령어를 입력합니다.

복구 과정에서 티스토리에 로그인하기 위한 로그인 아이디와 로그인 비밀번호를 요구합니다.

user 생성시와 마찬가지로 비밀번호 입력시 마스킹 문자(*)가 표시되지 않을 수 있습니다.

2단계 인증을 사용 중인 경우 로그인에 실패하기 때문에 2단계 인증을 사용하지 않는 계정이어야 합니다.
```
>> python manage.py shell
>> from seolpyo_dstory.utils import restore2 as r
>> r()
```

## 확인하기
장고 프로젝트를 실행하고, 복구된 글을 확인해봅니다.

로컬 서버에서 실행하는 경우 기본 주소는 127.0.0.1:8000입니다.
```
>> python manage.py runserver
```

# 그 외 설정들
여러 설정들을 만들고 적용할 수 있도록 했습니다.

디스토리 설정들과 장고 사이트 호스팅 관련 정보는 [설표의장고](https://django.seolpyo.com/)에서 확인하실 수 있습니다.


# 샘플 이미지
다음은 해당 패키지를 통해 티스토리 블로그를 이사하여 운영 중인 사이트의 샘플 이미지입니다.

샘플 사이트 : <https://dstory.seolpyo.com/>

티스토리 블로그 : <https://white-seolpyo.tistory.com/>

![이미지 1](https://github.com/white-seolpyo/seolpyo-dstory/blob/main/img1.png?raw=true)

![이미지 2](https://github.com/white-seolpyo/seolpyo-dstory/blob/main/img2.png?raw=true)

