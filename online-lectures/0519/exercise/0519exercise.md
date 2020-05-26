# 5월 19일 exercise

### 1. get_dog_image.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>exercise</title>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
  <h1>Dog Image(s)</h1>
  <hr>

  <h2>강아지</h2>
  <div class="dogs"></div>
  <button id="dog">강아지</button>

  <script>
    // // 함수 사용시
    // const createDogImage = function(image){
    //   // 3. Image Element 생성
    //   console.log(response.data.message)
    //       const dogImage = document.createElement('img')
    //       dogImage.src = image
    //       dogImage.style.height = '300px'
    //       return dogImage
    // }


    // 1. 버튼 클릭 -> 이벤트 발생
    const getDogButton = document.querySelector('#dog')
    getDogButton.addEventListener('click', function(event){
      // 2. Dog API 요청 -> 강아지 사진 주소 가져옴
      axios.get('https://dog.ceo/api/breeds/image/random')
        .then(response => {
          // 함수 사용시
          // createDogImage(response.data.message)

          // 3. Image Element 생성
          console.log(response.data.message)
          const dogImage = document.createElement('img')  // 강아지 이미지 생성 함수
          dogImage.src = response.data.message
          dogImage.style.height = '300px'
          // <img src=" " style="height: 300px;">
          // 4. 생성한 Image Element를 append!
          document.querySelector('.dogs').append(dogImage)
        })
        .catch(error => {
          console.log(error)
        })
    })
  </script>
</body>
</html>
```



### 2. 멍멍이+킹냥이 .html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>exercise</title>
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
</head>
<body>
  <h1>Animal Image(s)</h1>
  <hr>

  <h2>멍멍이</h2>
  <div class="dogs"></div>
  <button id="dog">멍멍이</button>

  <h2>킹냥이</h2>
  <div class="cats"></div>
  <button id="cat">킹냥이</button>

  <script>
    const getDogButton = document.querySelector('#dog')
    getDogButton.addEventListener('click', function(event){
      axios.get('https://dog.ceo/api/breeds/image/random')
        .then(response => {
          console.log(response.data.message)
          const dogImage = document.createElement('img')
          dogImage.src = response.data.message
          dogImage.style.height = '300px'
          document.querySelector('.dogs').append(dogImage)
        })
        .catch(error => {
          console.log(error)
        })
    })

    const getCatButton = document.querySelector('#cat')
    getCatButton.addEventListener('click', function(event) {
        axios.get('https://api.thecatapi.com/v1/images/search')
        .then(response => {
            const catImage = document.createElement('img')
            catImage.src = response.data[0].url
            catImage.style.height = '300px'
            document.querySelector('.cats').append(catImage)
        })
        .catch(error => {
            console.log(error)
        })
    })
  </script>
</body>
</html>
```

