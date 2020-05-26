# 5월 26일 workshop

### 1. todo_list_vue.html 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>0526 workshop</title>
  <style>
    /* 취소선 */
    .completed {
      text-decoration: line-through;
      opacity: .7;
    }
  </style>
</head>
<body>
  <!-- 여기에 코드를 작성하시오 -->
  <div id="app">
    <input type="text" v-model="newTodo">
    <button v-on:click="addTodo">+</button><br>
    <button v-on:click="deleteCompleted">완료된 할 일 삭제</button>
    <select v-model="status">
      <option value="all">전체</option>
      <option value="ing">진행중</option>
      <option value="end">완료</option>
    </select>
    <hr>
    <li 
    v-for="todo in computedTodoListByStatus" 
    v-bind:class="{ completed : todo.completed }"
    v-bind:key="todo.id"
    >
      <input type="checkbox" v-model="todo.completed">
      {{ todo.content }}
    </li>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    // 여기에 코드를 작성하시오
    const app = new Vue({
      el: '#app',
      data: {
        todoList: [
          { id: 1, content: 'Vue JS 복습', completed: true},
          { id: 2, content: 'Django 복습', completed: false},
          { id: 3, content: 'JavaScript 복습', completed: false},
        ],
        newTodo: '',
        status: 'all',
      },
      methods: {
        check: function(todo ) {
          todo.completed = !todo.completed
        },
        addTodo: function() {
          this.todoList.push({
            id : Data.now(),
            content: this.newTodo,
            completed: false,
          })
          this.newTodo = ''
        },
        deleteCompleted: function() {
          // filter : 주어진 함수의 테스트를 통과하는 모든 요소를 모아 새로운 배열로 반환
          const notCompletedTodoList = this.todoList.filter(todo => !todo.completed)
          this.todoList = notCompletedTodoList
        },
      },
      computed: {
        computedTodoListByStatus: function() {
          if (this.status === 'ing') {      // 미완료 할 일 목록
            return this.todoList.filter(todo => !todo.completed)
          }
          if (this.status === 'end') {      // 완료 할 일 목록
            return this.todoList.filter(todo => todo.completed)
          }
          return this.todoList   //전체목록
        },
      },
    })
  </script>
</body>
</html>
```

