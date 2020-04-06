# 4월 6일 homework

### 1. 

* (a) : 

  ```html
  {% url 'reservations:update' reservation.id %}
  ```

* (b)

  ```html
  {% csrf_token %}
  ```

* (c)

  ```html
  value = {{ reservation.name }}
  ```

* (d)

  ```html
  value = {{ reservation.date }}
  ```

### 2. 

```html
reservation:delete
```

### 3. 

```html
(a) : id
(b) : delete
(c) : reservation:index
```

### 4.  GET vs POST

> GET :  데이터를 쿼리스트링을 통해 전송한다. URL의 끝에 `?`와 함께 이름과 값을 쌍으로 이뤄 보낸다. 예시로 `www.naver.com/resources?name1=value1&name2=value2`로 서버에 요청을 보낸다. 서버에 동일한 요청을 여러번 전송해도, 동일한 결과가 나타나야한다. 서버의 데이터나 상태를 변경하지 않아 주로 조회를 할 때 사용한다.



> POST :  리소스를 생성/변경하기 위해 설계됐다. GET과는 다르게 전송할 데이터를 body에 담아 전송해 길이의 제한 없이 데이터를 전송할 수 있다. 데이터의 내용이 눈에 보이지 않아 GET보다 아주 약간 보안적으로 안전하나 개발자도구로 가능하다. 서버에 동일한 요청을 여러번 전송하면 응답이 다를 수 있다. 주로 생성에 쓰이는 메소드이다.