# 5월 25일 exercise

### 1. tutorial.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <div id='app'>
        <!-- v-if : 엘리먼트에 표시할 건지 안할건지 -->
        <p v-if="seen">
            나올랑가?
        </p>
        <!-- v-for : 루프 렌더링 -->
        <ul>
            <li v-for="animal in animals">
                {{ animal.name }} ({{ animal.type}})
            </li>
        </ul>
        <!-- v-on : 이벤트 리스너 추가 -->
        <p>{{ message }}</p>
        <button v-on:click="reverseMessage">뒤집어!!</button>

        <!-- v-model : 사용자 입력값과 뷰 인스턴스 간의 데이터 바인딩 -->
        <input type="text", v-model="userInput">
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        const app = new Vue({
            el: '#app',
            data: {
                seen: false,    // false, 0, 공백 -> 거짓으로 판별
                animals: [
                    { type: '고양이', name: '킹냥'},
                    { type: '강아지', name: '갓독'},
                    { type: '쥐', name: '햄토리'},
                ],
                message: '안녕하세요, 전 범규입니다!',
                userInput: '',
            },
            methods: {
                reverseMessage: function() {
                    // console.log(this)
                    // console.log(this.message)
                    this.message = this.message.split('').reverse().join('')
                },
            },
        })
    </script>
</body>
</html>
```



