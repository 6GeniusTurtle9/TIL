# 5월 12일 homework

### 1. 

* (a) : DOM


### 2. 

* `var` : 선택적으로 변수 값을 초기화하여 변수를 선언한다.

  * var x = 20;
  * var x; x = 20;

  ```javascript
  // function-scoped (함수내에서도 선언 가능하며, 그러면 함수 내에서만 참조 가능)
  function myfunc () {
      for(var i=0; i<5; i++){
          console.log(i)
      }
  }
  myfunc()
  console.log(i)	// 에러발생
  
  
  for(var j=0; j<5; j++){
      console.log(j)
  }
  console.log(j) 	// 4, 정상출력
  ```

* `let `: 변수의 재선언 불가. 그렇지만  값은 변경 가능

* `const` : 변수의 재선언 불가, 값도 변경 불가능

  ```javascript
  // block-scoped
  let a = '범규'
  let a = '조범규'
  a = '규'		// 가능
  
  const b = '범규'
  const b = '조범규'	// 불가능
  b = '규'		// 불가능
  ```

### 3. 

* T
* T
* F
* F : 설계상 실수는 맞으나 `typeof`로 확인시 null은 object로 나온다.

### 4. 

* `==` : 단순히 일치 여부를 판단한다.
* `===` : 엄격히 일치 여부를 판단하는 것으로, 타입의 일치도 판단한다.