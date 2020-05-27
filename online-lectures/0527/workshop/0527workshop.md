# 5월 27일 workshop

* Index.vue

  ```javascript
  <template>
    <div class="home">
      <p>사용 가능한 기능</p>
      <p>메뉴추천, 로또번호생성</p>
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  
  
  export default {
    name: 'Index',
    components: {
      
    }
  }
  </script>
  ```

  

* Lotto/vue

  ```javascript
  <template>
    <div>
      <h1>Lotto</h1>
      <button @click="pickNums">숫자생성</button><br><br>
      {{ numbers }}
    </div>
  </template>
  
  <script>
  import _ from 'lodash'
  
  export default {
      name: 'Lotto',
      data: function() {
          return {
              numbers: '',
          }
      },
      methods: {
          pickNums: function () {
              this.numbers = _.sampleSize(_.range(1, 46), 6)
          }
      },
  }
  </script>
  
  <style>
  
  </style>>
  ```

  

* Lunch.vue

  ```javascript
  <template>
    <div>
    <h1>점심 메뉴 고르기!</h1>
    <p>메뉴판 : {{ menus.join(', ')}}</p>
    <button @click="pick">뽑기</button><br><br>
    {{ choice }}
  
    </div>
  </template>
  
  <script>
  import _ from 'lodash'
  export default {
      name: 'Lunch',
      data: function () {
          return {
              menus: ['돈까스', '샌드위치', '마라탕', '된장찌개', '굶기'],
              choice: '',
          }
      },
      methods: {
          pick: function () {
              this.choice = _.sample(this.menus)
          }
      }
  
  }
  </script>
  
  <style>
  
  </style>>
  ```

  

* router/index.js

  ```javascript
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import Index from '../views/Index.vue'
  import Lunch from '../views/Lunch.vue'
  import Lotto from '../views/Lotto.vue'
  
  Vue.use(VueRouter)
  
    const routes = [
      // django -> urls.py 랑 같다
      // path(''. views.index, name="index")
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/lunch',
      name: 'Lunch',
      component: Lunch
    },
    {
      path: '/lotto',
      name: 'Lotto',
      component: Lotto
    },
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router
  ```

  