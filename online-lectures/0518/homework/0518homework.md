# 5월 18일 homework

### 1. 

* `querySelector()` : 특정 name, id를 제한하지 않고 css를 통해 요소를 찾는다.
  * 반환은 한개의 요소만 가능하며, 동일한 이름을 가진 객체가 있을 경우, 첫번째로 나오는 요소를 반환한다.
* `querySelectorAll()` : 해당 선택자에 해당하는 모든 요소를 가져온다. 반환객체는 nodeList이기에, for 또는 forEach 문을 사용해하만다.
* 공통
  * `#idName` : idName이라는 아이디를 가진 요소를 찾는다.
  * `.className` : className이라는 클래스명을 가진 요소를 찾는다.

### 2. 

* `innerHTML` : DOM 객체의 property로 존재한다. 원하는 만큼 HTML을 삽입할 수 있다. 전체 태그에 합쳐지는 것으로, 지속적으로 전체데이터 + 추가데이터를 새로 쓰는 효과를 보인다.  완전한 문자열을 만들고 할당 해야지 데이터의 파괴(?)가 방지된다.  한마디로, 데이터가 교체된다고 생각하면 된다.

* `appendChild()` : Method이다.  해당 객체의 자식리스트 맨 마지막에 추가 하는 것. 추가한 요소를 return하기도 한다.

### 3. 

* T
* T : `type`은 이벤트의 종류를 나타낸다. 지정된 이벤트가 발생할 때, 알림을 받는 개체가 `listener`이다.
* F : 자바스크립트에서는 함수도 객체이며, 특히 `1급 객체`이다. JS에서 특이한 점은 함수가 값으로 사용될 수 있다는 것이다. 또한, 함수는 함수의 인자로 전달 가능하다.

### 4.  [이벤트 타입](https://developer.mozilla.org/ko/docs/Web/Events)

* `click` : 마우스로 버튼이 눌렸을 때.
* `mouseover` : 마우스가 등록된 element나 자식 element 위로 이동했을 때.
* `mouseout` :  마우스가 등록된 element나 자식 element 밖으로 이동했을 때.
* `keypress` : shift, Fn, CapsLock을 제외한 키가 눌린 상태일 때.
* `keydown` : 키가 눌렸을 때.
* `keyup` : 키 누름이 해제될 때.
* `load` : 진행이 성공했을 때.
* `scroll `: document view나 element가 스크롤되었을때.
* `change` : 값이 바뀌었을 때.