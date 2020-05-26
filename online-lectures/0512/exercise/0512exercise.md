# 5월 12일 exercise

### 1-1. 타입(Primitive)

* Number

  * 정수, 소수를 표현 할 수 있다.
    * 13, -5, 3.14 등등
  * 무한대를 표현 할 수 있다.
    * Infinity, -Infinity
  * 숫자가 아님을 표현하는 `NaN`이 있다.

* String(Template Literal)

  * ' ' 또는 ""를  혼용 할 수 있다.

    * const sentence1 = '문장1'
    * const sentence2 = "문장2"

  * 줄 넘김을 위해 `\n`을 썼어야 했지만 `를 써서 줄 넘김을 표현 할 수 있다.

    * const word1 = "한줄짜리"

    * const word2 = `여러줄

      ​				짜리`

  * 문자열 인터폴레이션(String Interpolation)

    * const age = 10
    * const word3 = `철수는 ${age}세입니다.`
    * `${ ... }`으로 사용 가능하다.

* Boolean

  * 논리적인 요소를 나타냄.
  * `true`, `false`를 값으로 가짐

* Empty Value

  * `undefined` : 값을 할당하지 않은 변수. 자동으로 할당된다
  * `null`:  인위적으로 값이 없음을 표시

### 1-2. 연산자 

* 할당 연산자 (연산과 동시에 변수에 할당하는 연산자)

   ```javascript
    let a = 0
    a += 10
    a -= 10
    a *= 3
    a ++
    a --
    //등이 있다.
   ```

* 비교 연잔자

   ```javascript
   3 > 2	// true
   3 < 2	// false
   'A' < 'B'	// true
   'a' < 'A'	// false. 영어 소문자가 대문자보다 큰 값을 가진다
   '가' < '나'	// true
   ```

* 동등 연산자 (`==`, `!=`)

   * 값만 비교

* 일치 연산자 (`===`, `!==`)

   * 타입까지 엄격하게 비교

* 논리 연산자

  * and : &&
  * or : ||
  * not : !

* 삼항 연산자

  * `조건` ? `참인경우` : `거진인경우`

    ```javascript
    true ? '성공' : '실패'
    ```

    

### 2-1 조건문

* if, else if, else

```javascript
let day = 7

if (day === 1) {
  console.log('월요일')
} else if (day === 2) {
  console.log('화요일')
} else if (day === 3) {
  console.log('수요일')
} else if (day === 4) {
  console.log('목요일')
} else if (day === 5) {
  console.log('금요일')
} else if (day === 6) {
  console.log('토요일')
} else {
  console.log('일요일')
}
```

* switch

```javascript
switch(day) {
    case 1: {
        console.log('월요일')
        break
    }
    case 2: {
        console.log('화요일')
        break
    }
    case 3: {
        console.log('수요일')
        break
    }
    case 4: {
        console.log('목요일')
        break
    }
    case 5: {
        console.log('금요일')
        break
    }
    case 6: {
        console.log('토요일')
        break
    }
    case 7: {
        console.log('일요일')
        break
    }
    default: {
        console.log('break잘 걸어라')
    }
}
```



### 2-2 반복문

* while

```javascript
let num = 0
while (num < 6) {
console.log('${num}번');
num += 1
}
```

* for

```javascript
for (let i = 0; i < 6; i++){
console.log(i)
}
```

* for ... of

```javascript
const numbers = [0, 1, 2, 3]

for (const num of numbers) {
console.log(num)
}
```

* for ... in

```javascript
const fruits = {
'apple': 2,
'banana':10,
'tomato':10,
'watermelon':2,
}
for (const fruit in fruits) {
console.log(fruit)
console.log(fruits[fruit])
}
```

* continue

```javascript
for (let i = 0; i < 10; i++) {
if (i === 3) {
    continue
} else {
    console.log(i)
    }
}
```

### 3 .함수

```javascript
// 선언식
function add(num, num2) {
    return num1 + num2
}
console.log(add(1,2))
// 표현식
const sub = function mysub(num1, num2) {
    return num1 - num2
}
console.log(mysub(3, 2))
// 기본값 인자
const greeting = function(name='익명') {
    console.log('안녕, ${name}!')
}

// 화살표 함수
const arrow = function(name) {
    return 'hello, ${name}!'
}
// 1) function 키워드 삭제
const arrow = (name) => {
    return 'hello, ${name}'
}
// 2) () 생략 (매개변수가 하나인 경우)
const arrow = name => {
    return 'hello, ${name}'
}
// 3) {} & return 생략 (바디 표현식 하나인 경우)
const arrow = name => 'hello, ${name}!'
// 4) 인자가 없으면? -> _ 또는 ()로 표현 가능
const noArgs = () => 'No Args!!'
const noArgs = _ => 'No Args!!'
// 5-1) 객체 리턴? -> return 을 명시적으로 표시
const return Object = () => {
    return {key:'value'}
}
// 5-2) return 표기하기 싫으면 괄호 붙이기
const returnObject = () => ({ key: 'vlaue'})

// 무조건 화살표 함수로만 함수 선언하면..
// 자기 자신의 this, arguments를 바인딩하지 않는다.
```

### 4. 자료구조 (Array & Object)

```javascript
// 4-1 배열(array)
const numbers = [0, 1, 2, 3, 4]
console.log(numbers[0])
console.log(numvers[-1]) // undefined
console.log(numbers.length) // 5

numbers.reverse()
console.log(numbers)	// [4, 3, 2, 1, 0]

numbers.push('a')		// [4, 3, 2, 1, 0, "a"]
numbers.pop()			// [4, 3, 2, 1, 0]

numbers.unshift('b')	// ["b", 4, 3, 2, 1, 0]
numbers.shift()			// [4, 3, 2, 1, 0]

numbers.includes(1)		// true
numbers.includes(50)	// false

numbers.reverse()
numbers.push('a')
numbers.push('b')
numbers.push('c')		// [0, 1, 2, 3, 4, "a", "b", "c"]
numbers.push('a')		// [0, 1, 2, 3, 4, "a", "b", "c", "a"]

// 인덱스 접근
numbers.indexOf('a')	// 5 (앞의 a index 반환)
numbers.indexOf('f')	// -1

// 배열 메서드
numbers.join()			// "0,1,2,3,4,5,a,b,c,a"
numbers.join('')		// "01234abca"
numbers.join('-')		// "0-1-2-3-4-a-b-c-a"
```

```javascript
// 4-2 Object
const me = {
    name: '범규'	// key가 하나의 단어일 때
    'phone number': '01012341234',	//key가 여러 단어일때
    products: {
    	galaxyPhone: 'S20 Ultra'
    	galaxyBook: 'ion'
    	galaxyTab: 'S6'
    	galaxyBud: 'Plus'
	}
}

// 요소 접근
me.name					// me.['name']으로도 접근 가능
me.['phone number']		// key값이 여러 단어일때는, []로 접근
me.products.galaxyBuds

// 배열 반환 메서드
Object.keys(me)
Object.values(me)
Object.entries(me)		// key랑 value 반환

// 객체(오브젝트) 리터럴
let phones = ['galaxy', 'iphone', 'lollipop', 'chocolate']
let notebooks = {
    samsung: ['ion', 'flex'],
    apple: ['macbook pro', 'macbook air']
}
let earphones = null

const electronics = {
    phones,
    notebooks,
    earphones,
}				// 이렇게 작성 가능하게 한 것이 객체 리터럴이다.
console.log(electronics)
console.log(typeof electronics)		// object
```

```javascript
// 4-3 Json (JavaScript Object Notation)
// JSON -> Object
const jsonData = JSON.stringify({
    notebook: 'galaxy ion',
    phoe: 'galaxy S20'
})
console.log(jsonData)
console.log(typeof jsonData)	// string

// Object -> JSON
const parsedData = JSON.parse(jsonData)
console.log(parsedData)
console.log(typeof parsedData)	// object
```

