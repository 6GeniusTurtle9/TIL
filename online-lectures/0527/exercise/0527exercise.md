# 5월 27일 workshop

* Index.vue

  ```javascript
  <template>
    <div>
      <p>사용 가능한 기능</p>
      <p>메뉴 추천, 로또번호생성</p>
    </div>
  </template>
  
  <script>
  export default {
    
  }
  </script>
  
  <style>
  
  </style>>
  ```

* Lotto.vue

  ```javascript
  <template>
    <div>
      <h1>Lotto</h1>
      <button @click="picknums">숫자생성</button> <br><br>
      {{ numbers }}
    </div>
  </template>
  
  <script>
  import _ from 'lodash'
  
  export default {
      data: function () {
          return {
              numbers: '',
          }
      },
      methods:{
          picknums: function () {
          this.numbers = _.sampleSize(_.range(1,46), 6)
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
      <p>점심 메뉴 골라라</p>
      {{ menus.join(', ') }}<br><br>
      <button @click="pick">뽑으시오</button><br>
      <p>{{ choice }}</p>
    </div>
  </template>
  
  <script>
  import _ from 'lodash'
  
  
  export default {
      data: function () {
          return {
              menus: ['돈까스', '에그드랍', '쫄면', '마라탕', '양자강'],
              choice: '',
          }
      },
      methods: {
          pick: function () {
              this.choice = _.sample(this.menus)
          }
      },
  }
  </script>
  
  <style>
  
  </style>>
  ```