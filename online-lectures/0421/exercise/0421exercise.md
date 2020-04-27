# 4월 21일 exercise

### 1.

```shell
In [1]: User.objects.all()                                                                               
Out[1]: SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 LIMIT 21

Execution time: 0.006258s [Database: default]
<QuerySet [<User: User object (1)>, <User: User object (2)>, <User: User object (3)>, <User: User object (4)>, <User: User object (5)>, <User: User object (6)>, <User: User object (7)>, <User: User object (8)>, <User: User object (9)>, <User: User object (10)>, <User: User object (11)>, <User: User object (12)>, <User: User object (13)>, <User: User object (14)>, <User: User object (15)>, <User: User object (16)>, <User: User object (17)>, <User: User object (18)>, <User: User object (19)>, <User: User object (20)>, '...(remaining elements truncated)...']>
```

### 2.

```shell
In [2]: User.objects.get(id=19).age                                                                      
SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE "users_user"."id" = 19

Execution time: 0.005296s [Database: default]
Out[2]: 26
```

### 3.

```shell
In [3]: User.objects.values('age')                                                                       
Out[3]: SELECT "users_user"."age"
  FROM "users_user"
 LIMIT 21

Execution time: 0.001070s [Database: default]
<QuerySet [{'age': 40}, {'age': 36}, {'age': 37}, {'age': 40}, {'age': 30}, {'age': 26}, {'age': 18}, {'age': 33}, {'age': 23}, {'age': 22}, {'age': 15}, {'age': 22}, {'age': 32}, {'age': 35}, {'age': 24}, {'age': 19}, {'age': 34}, {'age': 17}, {'age': 26}, {'age': 17}, '...(remaining elements truncated)...']>
```

### 4.

```shell
In [4]: User.objects.filter(age__lte=40).values('id', 'balance')                                         
Out[4]: SELECT "users_user"."id",
       "users_user"."balance"
  FROM "users_user"
 WHERE "users_user"."age" <= 40
 LIMIT 21

Execution time: 0.005852s [Database: default]
<QuerySet [{'id': 1, 'balance': 370}, {'id': 2, 'balance': 5900}, {'id': 3, 'balance': 3100}, {'id': 4, 'balance': 250000}, {'id': 5, 'balance': 220}, {'id': 6, 'balance': 530}, {'id': 7, 'balance': 390}, {'id': 8, 'balance': 3700}, {'id': 9, 'balance': 43000}, {'id': 10, 'balance': 49000}, {'id': 11, 'balance': 640000}, {'id': 12, 'balance': 52000}, {'id': 13, 'balance': 35000}, {'id': 14, 'balance': 720}, {'id': 15, 'balance': 35000}, {'id': 16, 'balance': 720}, {'id': 17, 'balance': 440}, {'id': 18, 'balance': 94000}, {'id': 19, 'balance': 6100}, {'id': 20, 'balance': 590}, '...(remaining elements truncated)...']>
```

### 5.

```shell
In [5]: User.objects.filter(last_name='김', balance__gte=500).values('first_name')                       
Out[5]: SELECT "users_user"."first_name"
  FROM "users_user"
 WHERE ("users_user"."balance" >= 500 AND "users_user"."last_name" = '김')
 LIMIT 21

Execution time: 0.004913s [Database: default]
<QuerySet [{'first_name': '예진'}, {'first_name': '서현'}, {'first_name': '서영'}, {'first_name': '영일'}, {'first_name': '옥자'}, {'first_name': '광수'}, {'first_name': '성민'}, {'first_name': '정수'}, {'first_name': '서준'}, {'first_name': '은주'}, {'first_name': '미영'}, {'first_name': '우진'}, {'first_name': '순옥'}, {'first_name': '진우'}, {'first_name': '현지'}, {'first_name': '영호'}, {'first_name': '종수'}, {'first_name': '미숙'}, {'first_name': '민재'}, {'first_name': '경자'}]>
```

### 6.

```shell
In [6]: User.objects.filter(first_name__endswith='수', country='경기도').values('balance')               
Out[6]: SELECT "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."country" = '경기도' AND "users_user"."first_name" LIKE '%수' ESCAPE '\')
 LIMIT 21

Execution time: 0.012111s [Database: default]
<QuerySet [{'balance': 590}, {'balance': 370}]>
```

### 7.

```shell
In [7]: User.objects.filter(Q(balance__gte=2000)|Q(age__lte=40)).count()                                 
SELECT COUNT(*) AS "__count"
  FROM "users_user"
 WHERE ("users_user"."balance" >= 2000 OR "users_user"."age" <= 40)

Execution time: 0.002180s [Database: default]
Out[7]: 100
```

### 8.

```shell
In [8]: User.objects.filter(phone__startswith='010').count()                                             
SELECT COUNT(*) AS "__count"
  FROM "users_user"
 WHERE "users_user"."phone" LIKE '010%' ESCAPE '\'

Execution time: 0.003349s [Database: default]
Out[8]: 21
```

### 9.

```shell
In [9]: User.objects.filter(first_name='옥자', last_name='김').update(country='경기도')                  
BEGIN

Execution time: 0.000111s [Database: default]
UPDATE "users_user"
   SET "country" = '경기도'
 WHERE ("users_user"."first_name" = '옥자' AND "users_user"."last_name" = '김')

Execution time: 0.009677s [Database: default]
Out[9]: 1
```

### 10.

```shell
In [10]: User.objects.filter(first_name='진호', last_name='백').delete()                                 
BEGIN

Execution time: 0.000098s [Database: default]
DELETE
  FROM "users_user"
 WHERE ("users_user"."first_name" = '진호' AND "users_user"."last_name" = '백')

Execution time: 0.005905s [Database: default]
Out[10]: (1, {'users.User': 1})
```

### 11.

```shell
In [11]: User.objects.order_by('-balance').values('first_name', 'last_name', 'balance')[:4]              
Out[11]: SELECT "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."balance"
  FROM "users_user"
 ORDER BY "users_user"."balance" DESC
 LIMIT 4

Execution time: 0.005903s [Database: default]
<QuerySet [{'first_name': '순옥', 'last_name': '김', 'balance': 1000000}, {'first_name': '은주', 'last_name': '김', 'balance': 950000}, {'first_name': '미경', 'last_name': '이', 'balance': 890000}, {'first_name': '동현', 'last_name': '이', 'balance': 790000}]>
```

### 12.

```shell
In [12]: User.objects.filter(phone__contains='123', age__lt=30)                                          
Out[12]: SELECT "users_user"."id",
       "users_user"."first_name",
       "users_user"."last_name",
       "users_user"."age",
       "users_user"."country",
       "users_user"."phone",
       "users_user"."balance"
  FROM "users_user"
 WHERE ("users_user"."age" < 30 AND "users_user"."phone" LIKE '%123%' ESCAPE '\')
 LIMIT 21

Execution time: 0.002937s [Database: default]
<QuerySet [<User: User object (93)>]>
```

### 13

```shell
In [13]: User.objects.filter(phone__startswith='010').values('country').distinct()                       
Out[13]: SELECT DISTINCT "users_user"."country"
  FROM "users_user"
 WHERE "users_user"."phone" LIKE '010%' ESCAPE '\'
 LIMIT 21

Execution time: 0.001441s [Database: default]
<QuerySet [{'country': '충청북도'}, {'country': '경상북도'}, {'country': '경기도'}, {'country': '제주특별자치도'}, {'country': '경상남도'}, {'country': '전라남도'}, {'country': '강원도'}, {'country': '전라북도'}]>
```

### 14.

```shell
In [14]: User.objects.aggregate(Avg('age'))                                                              
SELECT AVG("users_user"."age") AS "age__avg"
  FROM "users_user"

Execution time: 0.003229s [Database: default]
Out[14]: {'age__avg': 28.343434343434343}
```

### 15.

```shell
In [15]: User.objects.filter(last_name='박').aggregate(Avg('balance'))                                   
SELECT AVG("users_user"."balance") AS "balance__avg"
  FROM "users_user"
 WHERE "users_user"."last_name" = '박'

Execution time: 0.003793s [Database: default]
Out[15]: {'balance__avg': 196114.2857142857}
```

### 16.

```shell
In [16]: User.objects.filter(country='경상북도').aggregate(Max('balance'))                               
SELECT MAX("users_user"."balance") AS "balance__max"
  FROM "users_user"
 WHERE "users_user"."country" = '경상북도'

Execution time: 0.002400s [Database: default]
Out[16]: {'balance__max': 400000}
```

### 17.

```shell
In [17]: User.objects.filter(country='제주특별자치도').order_by('-balance').values('first_name')[0]      
SELECT "users_user"."first_name"
  FROM "users_user"
 WHERE "users_user"."country" = '제주특별자치도'
 ORDER BY "users_user"."balance" DESC
 LIMIT 1

Execution time: 0.002828s [Database: default]
Out[17]: {'first_name': '순옥'}
```

