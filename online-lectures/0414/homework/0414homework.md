# 4월 14일 homework

### 1. 

```python
is_superuser = models.BooleanField
is_staff = models.BooleanField
is_active = models.BooleanField
```



### 2.  최대 30자 저장 가능

### 3. 

```python
(a) AuthenticationForm
(b) login
(c) form.get_user()
```



### 4. `.is_authenticated`



### 5. `AnonymousUser`



### 6. `PBKDF2_SHA256`



### 7.

```python
from. django.contrib.auth import logout
```

import 한 `logout`의 이름을 그래도 써서 아래 def logout과 충돌이 발생한다.

문제 해결을 위해 아래와 같이 이름을 바꿔서 불러와야한다.

```python
from. django.contrib.auth import logout as auth_logout
```



