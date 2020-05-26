# 5월 25일 workshop

### 1. get_cat_image_vue.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WorkShop</title>
    
</head>
<body>
    <!-- Axios & Vue.JS 로 고양이 페이지 만들기 -->
    <div id="app">
        <h1>냥냥이</h1>
        <button @click="getCatImage">눌러라냥</button>
        <hr>
        <img :src="catImage" v-bind:style="catStyle">
    </div>

    <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: "#app",
            data: {
                catImage:'',
                catStyle:{
                    height: '300px',
                },
            },
            methods: {
                getCatImage: function () {
                    axios.get('https://api.thecatapi.com/v1/images/search')
                    .then(response => {
                        const catImage = document.createElement('img')
                        this.catImage = response.data[0].url
                    })
                    .catch(error => {
                        console.log(error)
                    })
                },
            },
        })
    </script>
    <!-- 스타일 관련-> https://kr.vuejs.org/v2/guide/class-and-style.html -->
</body>
</html>
```


