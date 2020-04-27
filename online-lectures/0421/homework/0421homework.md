# 4월 21일 homework

### 1.  lookup 세가지

* `__contains` : 해당 글자를 포함하는 것을 찾아줌
* `__gt` : greater than으로 ~ 초과를 의미한다. 이상은 `gte`이며 미만, 이하는 `lt`, `lte`이다.
* `__endswith`: 끝나는 글자가 ~인 것을 찾아준다.

### 2.  on_delete 세 가지

* `NO ACTION` : 레코드를 삭제하지 못하게 함
* `CASCADE` : 관련된 레코드를 같이 삭제함
* `SET DEFAULT` : 관련된 레코드의 외래키 값을 기본값으로 변경

### 3. `commit=False`



### 4.  `article.comment_set.all`
