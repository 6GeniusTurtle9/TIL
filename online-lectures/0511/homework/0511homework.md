# 5월 11일 homework

### 1. 

* T
* T
* T (계층관계를 나타낼때 사용한다)
* F

### 2. 

* 200 : 서버가 요청을 제대로 처리함
* 400 : 서버가 요청의 구문을 인식 못함
* 401 : 인증이 필요해서 요청을 제공하지 않음. 인증 안됨의 의미
* 403 : 서버가 요청을 거부함. 사용자가 권한을 갖고 있지 않기 때문.
* 404 : 서버에 존재하지 않는 페이지에 대한 요청이 있을때 보여준다.
* 500 : 서버에 오류가 발생해 요청을 수행 할 수 없음.

### 3. 

```python
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'address']
```

