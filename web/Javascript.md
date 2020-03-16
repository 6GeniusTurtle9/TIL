# Javascript

### 기초

* 변수 선언(var)

* 데이터 타입 분류(typeof)

  * 원시타입(primitive) - 변경 불가능(immutable)

    * boolean -treu, false

    * null

      > 의도적으로 변수에 값이 없다는 것을 명시

    * undefined

      > 선언 이후 할당 하지 않은 변수에 지정된 값
      >
      > 초기화된 값

    * number

    * string

    * symbol(IES6)

  * 객체 타입(object)

    * 일반 객체, function, array, date, RegExp

  * 모든 숫자는 number

    * 정수 타입이 따로 없음(정수 체계는 있음)

  * String -템플릿 문자열

### 문법

* 연산자 `==` vs `===`
   * 동등 연산자(==)
     * 값 비교 및 예상치 않은 변환
   * 일치 연산자(===)  -> 이거 써야함
     * 엄격한 같은 형 비교



### 배열

> 객체 생성 방법
  * 객체는 Key와 Value로 구성된 속성(property)들의 모임
  * 암묵적 형변환
  * 접근은 ` [ ]`로  ex) myObj[name]
  * 객체 리터럴
  * Object 생성자 함수

* 배열 순회
  * for
  * for ... of
  * forEach
  * for ... in 은 속성까지 출력 될 수 있다.

* 배열 메소드
  * sort 메소드에 비교 함수(인자)가 없으면 문자열 기준으로 정렬한다.
    * 비교 함수를 넣어야함.
    * 1, 100, 2, 3 ...순으로 정렬될 수 있다.
  * 문자열 관련 - `join`, `toString`
    
    * 배열이 들어간다! (파이썬이랑 다름)
  * 배열 합치기 - `concat`
   * 원소 삽입/삭제 - `push`, `pop`, `unshift`, `shift`
   * 인덱스 탐색 - `indexOf`
   * 배열 조작 - `splice`
  
      * 원본 배열을 바꿈
    * 배열 자르기 - 'slice' 
        * return으로 원본 배열은 유지
  
  
  
### 함수

* 화살표 함수(ES6) -나중에 다시
* 함수 인자
* 함수 선언문, 표현문, 즉시 실행 함수



### 문서객체모델(DOM)

* DOM 조작

  * 문서의 구조화된 표현 제공!
  * 구조화된 노드와 오브젝트로 문서 표현
  * 주요 객체(중요)
    * window : DOM문서를 표현하는 창. 최상위 객체
      * window 객체는 전역 객체
      * 다양한 함수, 이름공간, 객체 등이 포함
    * document : 페이지 콘텐츠의 진입점 역할. `<body>`등 다른 요소 포함
    * navigator, location, history, screen

* DOM 접근 (중요 2가지로만 쓰자)

  * 단일 Node
    * document.querySelector(selector) `중요`
  * HTMLCollection(live)
    * 모두 live collection이며, 활용시 주의
  * NodeList(non-live)
    * document.querySelectorAll(selector) `중요`
  
* innerHTML, insertAdjacentHTML
  * 아래와 같은 메서드를 통해서도 가능, XSS공격에 취약
  * element.innerHTML(text)
  * element.insertAdjacentHTML(position, text)

  ### 이벤트

* EventTarget.addEventListener(type, listener [, useCapture])
  * type : 이벤트 유형 -click 등
  * listener : 이벤트가 발생했을 때 실행할 콜백 함수(핸들러)
  * useCapture : 기본 값(false), 상위 노드로 전파(버블링), 만약 trute인 경우 하위 노드 전파(캡처링)
* 이벤트 전파
  * 해당 요소에서 전파, 캡처링과 버블링
  * 항상 캡처링부터 시작, 버블링으로 종료
  * useCapture를 통해 특성 상황에 대하여 이벤트 관리 가능

* 이벤트 객체
  * 대표적인 속성과 메소드
    * Event.target : 이벤트가 원래 발생했던 대상
    * .currentTarget : 이벤트가 발생했던 대상
    * .preventDefault() : 이벤트 취소
    * .stopPropagation() : 이벤트 전파 중단