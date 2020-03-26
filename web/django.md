# django

> 파이썬 웹 프레임워크

## 설치

```bash
$ pip install django==2.1.15
```

* 수업에서는 `2.1.15` 를 기준으로 진행 예정입니다.

## django 프로젝트 시작

### 프로젝트 생성

```bash
$ django-admin startproject {프로젝트명}
```

### 서버실행

* `django_intro` 폴더의 `settings.py` 파일에 아래와 같이 수정한다.

  ```python
  # 28번째 라인
  ALLOWED_HOSTS = ['*']
  ```

* 반드시 서버 실행시 명령어가 실행되는 디렉토리를 확인할 것.

```bash
~/ $ cd django_intro/
~/django_intro/ $ python manage.py runserver 8080
```

* 실행된 서버는 우측의 영역의 url을 클릭한다.

  ![Screen Shot 2020-03-26 at 오전 10.27](C:/TurtleLab/SSAFY/django_intro(다운)/images/Screen Shot 2020-03-26 at 오전 10.27.png)

* 서버 종료는 터미널에서 `ctrl + c` 함께 입력한다.









