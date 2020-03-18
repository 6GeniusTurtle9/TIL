# CSS

### CSS selector(선택자)

* 기초 선택자
* 고급 선택자
* 되는 것과 하면 안되는 것을 잘 알자



### CSS 상속

* 속성(프로퍼티) 중에는 상속 되는 것과 아닌 것이 있다.
  * Text관련 요소 상속
  * Box model, position 관련은 상속 안됨
* MDN에서 확인하기



### CSS 적용 우선순위(중요)

* 중요도
  * !important
* 우선 순위
  * 인라인/id선택자/class선택자
  * id는 문서에서 한번만 등장->우선!!
* 소스 순서



### 크기 단위

* px(픽셀)

* em vs rem(root em)

* viewport

* vh, vw

  

### 문서표현(하)

* 변형 서체(`<strong>`, `<em>`)

* 컬러, 배경(background-image, background-color)

* 목록 꾸미기

  

### Box model(중요!)

* 구성(margin)

  * content-padding-border-margin

    콘텐츠가 제일 안 쪽

  * box-sizing: border-box

    * 실제 너비를 설정할 수 있다

* 마진 상쇄



### DIsplay 속성

* display: block
  * 줄바꿈
  * 옆에 마진이 자동으로 생김
  * 너비는 기본 100%
  * 너비를 가질 수 없다면 마진을 다 줌(자동으로)
* display: inline

* display: inline-block
  * 

기초문법 /선택자 및 우선순위/ 박스모델/디스플레이/포지션



### 레이아웃

* position
  * static: 드폴트 값(기준 위치)
    * 기본적인 배치 순서는 좌측상단
    * 부모 요소내에서 배치시, 부모 요소의 위치를 기준으로 배치
  * 좌표 프로퍼티(top, bottom, left, right)를 사용해 이동 가능(음수도 가능)
    * ....빠르다
  * relative
  * 
  * absolute
    * 조심히 써야한다! 위치가 바뀌기 때문
    * 본인이 있어야할 공간을 없애버림
  * fixed
    * 문서 전체에서의 특정 위치 고정
* float
  * box model의 네모형이 아닌 형태를 만들어줌
  * clear한 요소의 margin이 제대로 표현 되지 않는 문제
  * 자식 요소의 float 속성으로 인해 부모 영역의 높이가 사라지는 문제
    * 떠있는 것으로 보면 된다 
   * float : 요소를 띄워서 좌우측으로 배치시키는 속성 (주로 수평 정렬에 사용됨)
   * z-index : 요소가 겹쳐지는 경우, 겹쳐지는 순서를 지정하는 속성 (가상의 Z축이 있다고 생각하고, z-index 속성값을 부여해서 순서대로 쌓는다고 생각하셔요!)







* 네비게이션
  * 텍스트 네비게이션(추후 실습)
* animation

