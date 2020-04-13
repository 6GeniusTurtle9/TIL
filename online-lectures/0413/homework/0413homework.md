# 4월 13일 homework

### 1.  `from django.contrib.auth.models import User`

```python
class User(AbstractUser):

    """

    Users within the Django authentication system are represented by this

    model.


    Username and password are required. Other fields are optional.

    """

    class Meta(AbstractUser.Meta):

        swappable = 'AUTH_USER_MODEL'
```

### 2. 

```python
from django.contrib.auth.forms import UserCreationForm
```

### 3. 

```python
from django.views.decorators.http import require_POST
```

