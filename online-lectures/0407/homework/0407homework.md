# 4월 7일 homework

### 1. 

* (a) forms.ModelForm

* (b) Meta


### 2. 

* 첫 if문의 if문에서

  ```python
  if form.is_valid():
      article = form.save() -> reservation = form.save()
  ```

  그래야지 return 할때 reservation의 id를 넘길 수 있다.

* else문 아래 context가 들여써져있는 것을 빼야한다.

  ```python
  else:
      form = ReservationForm()
  context = {
      'form': form
  }
  ```

  context는 2가지 경우에 대해서 활용하기 위해 if, else문과 같은 위치에 있어야한다.

  하나는 GET요청시 `ReservationForm()` 을 제공하기 위함이다.

  두번째는 POST 요청이면서 `invalid`일 경우 `RservationForm(request.POST)`를  제공하기 위함이다.

### 3. 

* (a) form = ReservationForm(request.POST, instance=reservation)
* (b) form = ReservationForm(instance=reservation)

### 4. 

```html
1) form.as_p ->단락(paragrph)
2) form.as_table ->테이블 행(table)
3) form.as_ul ->목록항목(list item)
```
