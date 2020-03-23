# Flex

* `flex` 이전에는 배치를 위해서 `float`, `position` 지정을 해야했다.

### flex 주요 개념

* `container`, `item`

  ```html
  <style>
      .cotainer {
          display: flex;
      }
  </style>
  
  <div class="container">
      <div class="item"></div>
      <div class="item"></div>
  </div>
  ```

  

* `main axis`, `cross axis`

* `flex` 정의시:

  * `main axis`을 기준으로 배치가 시작된다. (기본은 `row`)
    * 만약, `row-reverse` 로 지정하게 도니다면, 오른쪽 끝부터 배치가 시작됨.
  * 모든 `item`은 행으로 배치된다.(`flex-direction`:`row`값으로 기본 설정 됨)
  * 모든 `item`은 `cross axis`을 모두 채운다.(`align-items:stretch`가ㅏㅄ으로 기본 설정)
  * 모든 `item`은 본인의 너비 혹은 컨텐츠 영역만큼 너비를 가지게 된다.
    * 경우에 따라서, 본인이 지정받은 너비보다 작을 수 있다.(`flex-wrap: nowrap`이 기본 값이기 때문)
  

### flex 속성

---

1. 
2. 

  

### 2.

### 3. align-items

> 

### 4. order

> 아이템의 순서를 정의할 수 있다.

* 기본값: `0`
* 음수값도 가질 수 있다.



### 5. align-self

> 아이템에 직접  align을 지정할 수 있음