# Vue

### 기본세팅

* Vue 인스턴스 생성
* 엘리먼트 마운트
* Data 선언

```html
 <div id="app">
 </div>
```

```javascript
const app = new Vue({
      el: '#app',
      data: {
        todoList: [
          'Vue JS 복습',
          'Django 복습',
          'JavaScript 복습',
        ]
      }
    })
```

### 배열에 담긴 데이터 루프 수행 (렌더링)

* 배열에 담긴 요소 개수만큼 li 엘리먼트 생성
* 데이터에 추가적인 정보 삽입 (완료 여부 데이터)
* 데이터 렌더링 시 객체 형태로 접근

```html
<div id="app">
    <li v-for="todo in todoList">
      {{ todo.content }} - {{ todo.completed }}
    </li>
 </div>
```

```javascript
const app = new Vue({
      el: '#app',
      data: {
        todoList: [
          { content: 'Vue JS 복습', completed: false},
          { content: 'Django 복습', completed: false},
          { content: 'JavaScript 복습', completed: false},
        ],
      },
    })
```

### `v-if` 디렉티브 활용해서, 완료 여부에 따라 렌더링 구분하기

* completed - false일 때, 할 일 내용을 그대로 출력
* completed - true 일 때, 할 일 내용 뒤에 `[완료]` 텍스트 붙여서 출력

[v-for vs v-if]([https://kr.vuejs.org/v2/guide/list.html#v-for-%EC%99%80-v-if](https://kr.vuejs.org/v2/guide/list.html#v-for-와-v-if))

```html
<div id="app">
   <li v-for="todo in todoList" v-if="!todo.completed">
     {{ todo.content }}
   </li>
   <li v-else>
      {{ todo.content }} [완료]
   </li>
</div>
```

### `v-on` 디렉티브 활용해서, 할 일을 클릭하여 완료 <-> 미완료 상태 바꾸기

```html
  <div id="app">
    <li v-for="todo in todoList" v-if="!todo.completed" v-on:click="check(todo)">
      {{ todo.content }}
    </li>
    <li v-else v-on:click="check(todo)">
      {{ todo.content }} [완료]
    </li>
  </div>
```

```javascript
const app = new Vue({
      el: '#app',
      data: {
        todoList: [
          { content: 'Vue JS 복습', completed: true},
          { content: 'Django 복습', completed: false},
          { content: 'JavaScript 복습', completed: false},
        ],
      },
      methods: {
        check: function(todo) {
          todo.completed = !todo.completed
        },
      },
    })
```

### `v-model` 디렉티브를 활용해서, input값과 태그, Vue 인스턴스 데이터 양방향 데이터 바인딩

```html
<div id="app">
    <input type="text" v-model="newTodo">
    <hr>
    ...
```

```javascript
data: {
    todoList: [
      { content: 'Vue JS 복습', completed: true},
      { content: 'Django 복습', completed: false},
      { content: 'JavaScript 복습', completed: false},
    ],
    newTodo: '',
  },
...
```

### `v-on` 디렉티브를 활용하여, 사용자가 `+` 버튼을 누르면 todoList 배열에 추가

* addTodo  함수 구현
* `+` 버튼 클릭하면 addTodo 함수 실행

```html
<div id="app">
  <input type="text" v-model="newTodo">
  <button v-on:click="addTodo">+</button>
  <hr>
      ...
```

```javascript
methods: {
    check: function(todo) {
      todo.completed = !todo.completed
    },
    addTodo: function() {
      this.todoList.push({
        content: this.newTodo,
        completed: false,
      })
      this.newTodo = ''
    },
  },
  ...
```

### 완료된 할 일 지우기 (기능 구현)

```html
<div id="app">
    <input type="text" v-model="newTodo">
    <button v-on:click="addTodo">+</button>
    <button v-on:click="deleteCompleted">완료된 할 일 삭제</button>
    <hr>
    ...
```

```javascript
methods: {
        check: function(todo) {
          todo.completed = !todo.completed
        },
        addTodo: function() {
          this.todoList.push({
            content: this.newTodo,
            completed: false,
          })
          this.newTodo = ''
        },
        deleteCompleted: function() {
          // filter : 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
          const notCompletedTodoList = this.todoList.filter(todo => {
            return !todo.completed
          })
          this.todoList = notCompletedTodoList
        },
      },
```

### 완료 여부를, 텍스트가 아닌 체크박스로 표현하기

* 완료 여부를 텍스트로 구분하기 위해 필요했던 `v-if`, `v-else` 등을 전부 삭제

* `v-model` 디렉티브를 활용하여 체크박스의 체크 유무를 양방향 데이터 바인딩

[폼 입력 바인딩](https://kr.vuejs.org/v2/guide/forms.html)

```html
<li v-for="todo in todoList">
  <input type="checkbox" v-model="todo.completed">
  {{ todo.content }}
</li>
```

```javascript
      data: {
        todoList: [
          { content: 'Vue JS 복습', completed: true},
          { content: 'Django 복습', completed: false},
          { content: 'JavaScript 복습', completed: false},
        ],
        newTodo: '',
      },
```

### 완료된 할 일 취소선 긋기

```html
  <style>
    /* 취소선 */
    .completed {
      text-decoration: line-through;
      opacity: .7;
    }
  </style>

    <li v-for="todo in todoList" v-bind:class="{ completed : todo.completed }">
      <input type="checkbox" v-model="todo.completed">
      {{ todo.content }}
    </li>
```

```javascript
data: {
    todoList: [
      { content: 'Vue JS 복습', completed: true},
      { content: 'Django 복습', completed: false},
      { content: 'JavaScript 복습', completed: false},
    ],
    newTodo: '',
  },
```

[클래스 스타일 바인딩](https://kr.vuejs.org/v2/guide/class-and-style.html)

### 할 일 목록을 완료 여부에 따라 구분해서 렌더링하기 (all, ing, end)

```html
<select v-model="status">
      <option value="all">전체</option>
      <option value="ing">진행중</option>
      <option value="end">완료</option>
</select>
```

```javascript
todoListByStatus: function() {
          if (this.status === 'ing') {      // 미완료 할 일 목록
            return this.todoList.filter(todo => !todo.completed)
          }
          if (this.status === 'end') {      // 완료 할 일 목록
            return this.todoList.filter(todo => todo.completed)
          }
          return todoList   //전체목록
        },
```

* 콘솔창 테스트 : status 값 변경 후, todoListByStatus 메서드 실행해서 return 값 확인



### 사용자가 보는 할 일 목록을 todoList 원본이 아니라, todoListByStatus 메서드 return 값으로 변경

