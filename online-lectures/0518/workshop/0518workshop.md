# 5월 18일 workshop

### 1. todo_list.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>0518 exercise & workshop</title>
</head>
<body>
  <h2>Add New Todo</h2>
  <p></p>
  <hr>

  <h2>Todo List</h2>
  <ul></ul>
  <hr>

  <h2>Completed Tasks</h2>
  <ul></ul>
  <hr>

  <script>
    // 1. 폼 만들기
    const todoForm = document.createElement('form')

    // 1-1. Label
    const todoFormLabel = document.createElement('label')
    todoFormLabel.setAttribute('for', 'todo')
    todoFormLabel.innerText = 'Add New Todo'
    // 더 정확한 라벨링은 다른 방법으로 해결하자(콜론, 띄어쓰기 등)

    // 1-2. Input-text
    const todoFormInput = document.createElement('input')
    todoFormInput.setAttribute('type', 'text')
    todoFormInput.setAttribute('id', 'todo')

    // 1-3 Input-Submit
    const todoFormSubmit = document.createElement('input')
    todoFormSubmit.setAttribute('type', 'submit')
    todoFormSubmit.setAttribute('value', 'Add')

    // append -> 여러개 추가, return X
    // appendChild -> 한개 추가, 추가한 요소를 return
    todoForm.append(todoFormLabel, todoFormInput, todoFormSubmit)
    document.getElementsByTagName('p')[0].appendChild(todoForm)

    // 2. todo list 만들기
    const createTodo = (todo) => {
      const newTodo = document.createElement('li')

      const todoLabel = document.createElement('label')
      todoLabel.innerText = todo

      const todoCheckbox = document.createElement('input')  // 완료 여부 체크박스
      todoCheckbox.setAttribute('type', 'checkbox')

      const todoInputEdit = document.createElement('input')
      todoInputEdit.setAttribute('type', 'text')

      const editButton = document.createElement('button')
      editButton.innerText = 'Edit'
      const deleteButton = document.createElement('button')
      deleteButton.innerText = 'Delete'

      // ---------------Workshop------------------
      // 2. 완료 (삭선 긋기 + 위치 이동)
      todoCheckbox.addEventListener('change', function(event){
        if (event.target.checked) {   // 체크박스 true
          todoLabel.style.textDecoration = 'line-through'
          completedList.appendChild(newTodo)
        } else {  // 체크박스  False
          todoLabel.style.textDecoration = 'none'
          todoList.appendChild(newTodo)
        }
      })

      // 3. 수정
      editButton.addEventListener('click', function(event){
        if (todoInputEdit.value) {
          todoLabel.innerText = todoInputEdit.value
        }
        todoInputEdit.value = null
      })

      // 4. 삭제
      deleteButton.addEventListener('click', function(event) {
        newTodo.remove()
      })

      // -----------------------------------------


      newTodo.append(todoCheckbox, todoLabel, todoInputEdit, editButton, deleteButton)
      // document.querySelector('ul').appendChild(newTodo)
      return newTodo
    }
    
    todos = [
      'Django ModelForm 복습',
      'Javascript DOM 조작 복습',
      'Django static, media 복습',
    ]

    const todoList = document.querySelector('ul')
    // for (let i=0; i<todos.length; i++) {
    //   const newTodo = createTodo(todos[i])
    //   document.querySelector('ul').appendChild(newTodo)
    // }
    todos.forEach(todo => {
      todoList.appendChild(createTodo(todo))
    })

    // workshop
    // 1. 할 일 추가
    todoForm.addEventListener('submit', function(event) {
      event.preventDefault()
      if (todoFormInput.value.trim()) {
        todoList.appendChild(createTodo(todoFormInput.value))   // 공백 거름
      } else {
        alert('공백 말고 값을 입력해주세요.')
      }
      todoFormInput.value = null
    })

    // 2. 할 일 완료
    const completedList = document.getElementsByTagName('ul')[1]  // 완료한 테스크가 이동할 위치

  </script>
</body>
</html>
```

