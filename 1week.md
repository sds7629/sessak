# 새싹반 1주차

몫을 구하는 연산자 -> // 

나머지를 구하는 연산자 -> %

제곱을 하는 연산자 -> **

type을 통해 해당 객체의 타입을 알 수 있음.

몫과 나머지 둘 다 필요한 경우 -> divmod(target, divide)

## 실수

float은 부동 소수점에서 유래되었다.

- 그러면 부동 소수점은 무엇인가?

python에서 실수를 값을 확인할 때 아래와 같이 사용하면 True가 나와야 할 것 같은데 실제 값은 False Why?

```python
0.1 * 3 == 0.3
False
1.2 - 0.1 == 1.1
False
0.1 * 0.1 == 0.01
False
```

대부분의 언어가 비슷하게도 실수를 표현할 때 완전히 같은 값이 아닌 근삿값으로 판별!

```python
print(.1 + .2)
0.30000000000000004
```
그러면 최대한 비슷한 .3의 값을 어떻게 가져와야할까 => 
간단한 방법으로 decimal 모듈을 이용 다른 방법으로는 math.fsum(), 
round(), float.as_integer_ratio(), math.is_close() 등이 있고
엄격하게 값을 비교해야하는 상황이 아니라면 math.is_close()를 써보는 것을 추천

math.fsum() 함수는 생각보다 정확한 값을 주지 않아 비추천!

- 주의 해야할 점으로는 decimal 모듈은 인자로 str값을 줘야 정확하다

```python
import decimal
print(decimal.Decimal('2') + 2)
4
```

여기서 의문점 파이썬에서 말하는 모듈, 내장함수, 메서드, 패키지? 한번 간단한게 정리하고 갑시다

- 모듈은 우리가 사용하는 from ~~ import ~~ 에서 import로 가져오는 파일을 의미함. (제가 맨날 패키지라 말하는 것들 실제 의미는 모듈)

- 그러면 패키지가 뭐냐? 이런 모듈들을 그룹화해놓은 폴더! 보통은 라이브러리라고도 많이 부르는데 라이브러리는 모듈과 패키지를 아우르는 표현? 이라 생각하시면 편합니다! 파이썬 대표적인 패키지는 numpy, pandas 등이 있어요

- 여기서 수강생 분들이 많이 하시는 실수 => 모듈 혹은 패키지 명과 같은 이름의 파일을 생성해서 원하는 모듈을 import하지 못하는 상황이 자주 발생
즉 최대한 모듈 혹은 패키지명과 이름을 다르게 설정하는 것이 좋다.


## 변수

다른 언어의 경우 변수에 값 없이 선언만 하는 것이 가능한데
```java
int a; // 선언 
a = 5 // 할당(초기화)
a = 10 // 재할당
```

파이썬의 경우에는 독립적으로 변수만 따로 선언을 할 수 없고 
변수를 선언함과 동시에 값을 할당해주면 내부적으로 선언을 해주고 할당을 해준다

```python
a = 10 # (선언과 동시에 초기화)
a = 5 # (재할당)
만약 비어있는 값을 넣고 싶다면
a = None
```

변수에 값을 할당한 이후 변수끼리의 계산이 가능해짐 주의해야할 점
python은 다른 자료형과의 연산을 금지하는 것들이 있는데 대표적으로 
str타입과 int, float타입의 연산이다 

```python
a = "1.1"
b = 1.1

a + b

!TypeError: can only concatenate str(not 'float') to str
```

이런식으로 타입에러가 찍히니 조심!


input을 사용할 때 여러개의 변수를 사용하고 싶다면 split을 이용하자
```python
a, b = input("사용할 값").split()

# 공백을 기준으로 값을 나눈다.
```

만약 받은 값을 정수!로 변환하고 싶다면 map함수를 이용하자

```python
a, b = map(int, input("사용할 값").split())
```

map함수는 첫 번째 인자로 함수를, 두 번째 인자로 iterable한 객체를 주어야한다.

> 여기서 iterable이 무엇인가?

iterable은 반복 가능한 객체로 스페셜 메서드인 __iter__ 메서드를 가지고 있음. 대표적인 iterable한 객체로는 list, dict, set, str, bytes, tuple, range 타입들이 있음

```python
a = [1,2,3]
dir(a) 

['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

iterator 객체는 차례로 값을 꺼낼 수 있는 것들을 의미 -> iterable한 객체를 iter() 함수를 사용해 만들 수 있음
```python
a = [1,2,3]
a_list = iter(a)
type(a_list)  ## list_iterator
next(a_list)
1
next(a_list)
2
```

## Bool

is 와 == 의 차이는 값이 같은지 혹은 객체가 같은지를 비교하는 것에서 차이점이 발생
```python
a = 1
b = 1.0
a == b # True
a is b # False
a is not b # False

---------------------

a = [1, 2, 3]
b = a
a is b # True
a == b # True
c = [1, 2, 3]
a is c # False
a == c # True
```

a는 int타입 b는 float타입으로 같은 객체라 비교할 수 없기 때문에 is를 사용할 경우 False  

### Truthy and Falsy

Truthy와 Falsy가 무엇일까? -> 간단하게 True로 취급되는 값과 False로 취급되는 값을 의미

대표적인 Falsy값들 이외의 값들은 기본석으로 Truthy 오브젝트!
```python
bool(0) # False
bool(0.0) # False
bool(None) # False
bool([]) # False
bool({}) # False
bool("") # False
```

### 그러면 Bool을 이용해 단축평가를 이용해보자
> and 의 경우에 양쪽의 조건식이 모두 True일 때만 True 그러면 여기서 첫번째 조건식이 False일 경우에는 어떻게 될까 -> 뒤의 값을 평가하지 않고 False 반환 즉, 리소스 감소

```python
a = 1
b = 0
if a and b:
    print('hi')
else:
    print('bi')
```

## 시퀀스 자료형

특정 값이 있는지 확인 => in
특정 값이 없다? => not in

시퀀스 객체끼리는 연결이 가능하다 다만 주의해야할 점은 range는 연산이 불가!

```python
a = [1,2,3]
b = [4,5,6]
a + b

-- 
[1,2,3,4,5,6]
```

리스트 슬라이싱 => 0번 인덱스 부터 3번 인덱스까지 가져온다.
```python
a = [1,2,3,4,5,6]
a[0:4]

b = slice(0, 4)
a[b]

--

[1,2,3,4]
[1,2,3,4]
```

## 딕셔너리

키 값이 있는지를 확인할 때는 시퀀스 자료형에서 배운 것과 마찬가지로 in을 사용할 수 있다.

len 함수 역시 사용 가능!


## if 조건

if에서 주의해야할 점은 아래 코드!!
원래 코드와 다른점이 무엇일까요?
```python
a = 6

if a % 2 == 0:
    print('hi')
if a % 3 == 0:
    print('bi')

```

또 Truthy, Falsy 값이 if문에서 많이 사용된다!

```python
if '' :
    print("I'm Falsy")
else:
    print('no')

```


여기서 mutable 과 immutable에 대해서 조금 알아보고 넘어가자
```python
a = 10   # int형 객체가 메모리에 할당 된 이후 a라는 변수가 해당 객체를 바인딩
         # 쉽게 말하면 10이 메모리에 할당 된 이후 a라는 변수가 해당 메모리를 가리킨다(?)
def sol(x:int) -> None:
    x += 1
    print(x)
print(a)
```

mutable은 값이 바뀔 수 있는 것 immutable은 값이 바뀌지 않는 것
그러면 값이 변했을 때 이전에 있던 값은 어떻게 되나요? => 파이썬 가비지 컬렉션에 의해 할당된 값이 소멸

대표적인 immutable 객체 => int, float, str, tuple
대표적인 mutable 객체 => list, dict

다만 주의해야할 점 => 클래스에 선언한 attribute 속성 값은 mutable로 변한다.
```python
a = [10, 20, 30]

def sol(x: list) -> None:
    x[0] = 50

sol(a)
```

그냥 이렇구나~ 하구 넘어가셔도 ok 나중에 클래스 배우고 해보시면 됩니다.

```python
from typing import Optional

class User:
    def __init__(self, value: int | None = None) -> None:
        self.value = value

    # def __init__(self, value: Optional[int] = None) -> None:
    #     self.value = value

    def change_val(self) -> None:
        self.value += 1
```
