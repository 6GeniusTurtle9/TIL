# 6월 1일 workshop

* App.vue

  ```javascript
  <template>
    <div id="app">
      <SearchBar
        @input-submit="onInputSubmit"
      />
      <VideoList
        :videos="videos"
      />
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  import SearchBar from './components/SearchBar.vue'
  import VideoList from './components/VideoList.vue'
  const API_KEY = process.env.VUE_APP_YOUTUVE_API_KEY
  const API_URL = 'https://www.googleapis.com/youtube/v3/search'
  
  export default {
    name: 'App',
    components: {
      SearchBar,
      VideoList,
    },
    data() {
      return {
        videos: [],
      }
    },
    methods: {
      onInputSubmit(inputValue) {
        axios.get(API_URL, {
          params: {
            key: API_KEY,
            part: 'snippet',
            type: 'videos',
            q: inputValue
          }
        })
        .then(res => {
          this.videos = res.data.items
        })
        .catch(error => {
          console.log(error)
        })
      },
    },
  }
  </script>
  
  <style>
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  
  ```

  

* SearchBar.vue

  ```javascript
  <template>
    <div>
      <input 
      type="text"
      @keypress.enter="onInput"
      >
    </div>
  </template>
  
  <script>
  export default {
      name: 'SearchBar',
      methods: {
          onInput(event) {
              this.$emit('input-submit', event.target.value)
          },
      },
  }
  </script>
  
  <style>
  
  </style>
  ```
  
  
  
* VideoList.vue

  ```javascript
  <template>
    <div>
      <h1>이 곳은 Video List 컴포넌트입니다</h1>
      {{ videos.length }}
    </div>
  </template>
  
  <script>
  export default {
      name: 'VideoList',
      props: {
          videos: {
              type: Array,
          }
      }
  }
  </script>
  
  <style>
  
  </style>
  ```
  

