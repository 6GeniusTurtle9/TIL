# 4월 20일 homework

### 1. 알맞는 용어

* 관계형 데이터베이스에서 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것  -`스키마`
* 열과 행의 모델을 사용해 조직된 데이터 요소들의 집합 -`테이블`
* 고유한 데이터 형식이 지정되는 열 -`칼럼`
* 단일 구조 데이터 항목을 가리키는 행  - `레코드`
* 각 행의 고유값 -`기본키`

### 2. (4)SELECT

### 3. RDBMS vs NOSQL

* RDBMS(Relational Database Management System)

  > SQL(Structured Query Language)를 사용해 RDBMS에서 데이터를 검색, 저장, 수정, 삭제 등이 가능하다.  데이터 스키마에 따른 관계를 통해 테이블간 연결을 사용, 효율적인 데이터 관리가 가능

* NOSQL(Not Only SQL)

  > 스키마가 없어 자유로운 데이터 관리가 가능. 테이블간 관계를 형성 할 필요가 없어 형태나 구조를 신경 쓸 필요가 없다. 다만, 자유롭게 데이터 수정(추가)이 가능해 중복 데이터가 생성 될 수 있다.

### 4. 틀린 문장

* (3) INSERT INTO classmates values(address='seoul', age=20, name='홍길동');

  -> Error: no such column: address

### 5. `%` vs `_`

* `%`는 앞, 뒤, 또는 중간에 글자 수에 상관없이 탐색한다.
* `_`는 그 수 만큼의 글자를 탐색한다.

