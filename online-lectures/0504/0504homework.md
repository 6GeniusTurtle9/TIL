# 5월 4일 homework

### 1.  MTV

* Model : 데이터를 표현하기위한 스키마를 제공한다.
* Template : 사용자에게 정보를 보여준다.HTML로 구현된다.
* View : Request와 Response를 담당하며 데이터를 처리, 가공한다.



### 2. 

* (a) .
* (b) views
* (c) views.index



### 3. 

* (a) settings.py
* (b) TEMPLATES
* (c) STATICFILES_DIRS



### 4. 

* python manage.py makemigrations
* python manage.py showmigration
* python manage.py sqlmigrate `앱이름` 0001
* python manage.py migrate



### 5. 

* F
* T
* F
* T



### 6.

* MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
* MEDIA_URL = '/media/'



### 7

* T
* F
* T
* T
* F



### 8.

* (a) PROTECT

* ProtectedError

### 9.

* ManyToManyField
* related_name
  * 이름을 따로 지정해주지 않으면 중복 에러가 발생할 수 있어서 겹치지 않게 잘 지정한다.

### 10.

* table name : accounts_user_followers 
* field name : id, from_user_id, to_user_id