# Python 3. 함수
​
​
​
1. Palindrome은 앞에서부터 읽었을 때와 뒤에서부터 읽었을 때 같은 단어를 뜻한다. 따라서, ‘a’ ‘nan’ ’토마토’ 모두 palindrome에 해당합니다.
​
   단어를 입력받아 Palindrome을 검증하고 True나 False를 리턴하는 함수 palindrome(word)를 만들어보세요.
​
* code
​
```python
word = input()
​
def palindrome(word):
    if word==word[::-1]:
        return True
    else:
        return False
   
​
result = palindrome(word)
print(result)
​
'''
print(''.join(reversed(word)))
print(word[::-1])
'''
​
```
​
​
​
* teacher's code (더 정석적인 방법)
​
```python
def palindrom(word):
    list_word=list(word)
    
    for i in range(len(list_word)//2):
        if list_word[i]!=list_word[-i-1]:
            return False
​
    return True
```
​
​
​
* result
​
```python
토마토
True
​
abcd
False
```