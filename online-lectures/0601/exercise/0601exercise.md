# 6월 1일 exercise

* App.vue

  ```javascript
  <template>
    <div id="app">
      <div id="nav">
        <router-link to="/todolist">
        Todo List
        </router-link> |
      </div>
      <router-view/>
    </div>
  </template>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  #nav {
    padding: 30px;
  }
  
  #nav a {
    font-weight: bold;
    color: #2c3e50;
  }
  
  #nav a.router-link-exact-active {
    color: #42b983;
  }
  </style>
  
  ```

* TodoView.vue

  ```javascript
  <template>
    <div>
      <h1>Todo List</h1>
      <hr>
      <!-- TodoInput : 사용자로부터 입력값 받기 -->
      <TodoInput @create-todo="createTodo"/>
      <!-- TodoList : 할 일 목록 -->
      <TodoList :todos="todos" @checked="updateTodo"/>
      <!-- 3. 보여주기 -->
    </div>
  </template>
  
  <script>
  import TodoInput from '../components/TodoInput.vue'
  import TodoList from '../components/TodoList.vue'
  
  export default {
      name: 'TodoView',
      // 2. 등록하기
      components: {
          TodoInput,
          TodoList,
      },
      data() {
          return {
              todos: [
                  { id: 1, content: 'Django 복습', isCompleted: true},
                  { id: 2, content: 'JS 복습', isCompleted: false },
                  { id: 3, content: 'Vue.js 복습', isCompleted: true},
              ],
          }
      },
      methods: {
          updateTodo(todo) {
              todo.isCompleted = !todo.isCompleted
          },
          createTodo(todo) {
              this.todos.push(todo)
          },
      },
  }
  </script>
  
  <style>
  
  </style>>
  ```

  

* TodoInput.vue

  ```javascript
  <template>
    <div>
      <input type="text" v-model="todo" @keypress.enter="createTodo">
      <button @click="createTodo">추가</button>
    </div>
  </template>
  
  <script>
  export default {
      name: 'TodoInput',
      data() {
          return {
              todo: '',
          }
      },
      methods: {
          createTodo() {
              if (this.todo.trim()) {
                  this.$emit('create-todo', {
                      id: Date.now(),
                      content: this.todo,
                      isCompleted: false,
                  })
              }
              this.todo=""
          },
      },
  }
  </script>
  
  <style>
  
  </style>
  ```

* TodoList.vue

  ```javascript
  <template>
    <div>
      <h1>할 일 목록</h1>
      <ul>
          <li v-for="todo in todos" :key="todo.id" :class="{ completed: todo.isCompleted }">
          <input type="checkbox" :checked="todo.isCompleted" @click="checkTodo(todo)">
              {{ todo.content }}
          </li>
      </ul>
      <hr>
  
    </div>
  </template>
  
  <script>
  
  export default {
      name: 'TodoList',
      props: {
          todos: {
              type: Array,
              required: true,
          },
      },
      methods: {
        checkTodo(todo) {
            this.$emit('checked', todo)
        },
      },
  }
  </script>
  
  <style>
  .completed {
      text-decoration: line-through;
  }
  </style>
  ```

  

* index.js

  ```javascript
  import Vue from 'vue'
  import VueRouter from 'vue-router'
import TodoView from '../views/TodoView.vue'
  
  Vue.use(VueRouter)
  
    const routes = [
    {
      path: '/todolist',
      name: 'TodoView',
      component: TodoView
    },
  
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  ```
  
  