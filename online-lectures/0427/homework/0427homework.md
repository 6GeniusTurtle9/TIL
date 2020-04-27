# 4월 27일 homework

### 1. 

* F ) 부모 테이블에서 하위 테이블의 데이터를 참조하기 위한 키이다.
* F ) N이 1의 데이터를 참조한다.
* T ) 참조 무결성을 위해 필요한 속성이다.
* F ) 반드시 부모늬 PK일 필요는 없다. null일 수도,  여러개일 수 도 있다.

### 2. 

* answer_id
* articles_question

### 3. 

* Question.Comment_set.all

### 4. 

* `login_required` 제거
* `if request.user.is_authenticated:` 추가
* 405 error가 발생하며, GET방식이라 POST를 넘기지 못함