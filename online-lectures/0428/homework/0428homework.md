# 4월 28일 homework

### 1. 

* T) 
* T)
* F )  하나만 작성할 수도 있다.

### 2. 

```html
(a) user
(b) article.like_users.all
```



### 3. 

```python
(a) username
(b) followers
(c) filter
(d) remove
(e) add
```



### 4. Error 

* 모델을 변경하면서 예전 User를 참조하도록 되있기 때문에 발생한다.
* settings.py에 `AUTH_USER_MODEL = 'accounts.User' `를 추가하고 아래와 같이 작성한다.

```python
from django.contrib.auth import get_user_model

User = get_user_model()
```



### 5. related_name 필수인 이유

* related_name은 지정을 해주지 않을 경우, 자동으로 생성 되는데, 이름이 중복될 수 있어 에러가 발생할 수 있다. 이름을 따로 지정해줘야 중복에 의한 에러 발생을 막을 수 있다.

### 6.

```html
(a) person.followings.all
(b) person.followers.all
(c) user
(d) person
```

