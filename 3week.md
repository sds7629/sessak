## 람다 표현식
JS로 비교를 하자면 익명 함수!!(Annonymous Function)
람다의 경우 함수를 간단하게 작성할 수 있다!

```python
lambda 인자 : 표현식

##

def add(x: int, y: int) -> int:
    return x + y

이 함수를 lambda 로 표현하자면

add = lambda x , y : x + y
```

람다가 많이 사용되는 곳?
주로 map 함수와 filter에서 사용이 많이된다~
reduce에서도 사용은 됩니다!

```python
new_list = [1,2,3,4,5]

new_list2 = list(map(lambda x: x * 2, new_list))
print(new_list2)
# 2,4,6,8,10

from functools import reduce
new_list3 = list(range(1, 21))
total = reduce(lambda x, y: x + y, new_list3)
print(total)

# 210
```

```python
def is_even(x):
    return x % 2 == 0

result = list(filter(is_even, range(10)))
print(result)

result2 = list(filter(lambda x: x % 2 == 0, range(10)))
print(result2)

## [0,2,4,6,8]
```

## 근데 왜 람다를 사용할까?

람다 표현식의 경우에 기존 def를 사용할 떄보다 메모리, 속도 면에서 향상되어있다~고 나와 있으나 속도 비교를 해보았을 때 유의미하다 생각될 정도의 차이는 전혀 없었습니다! 그렇다면 도대체 왜!? 사용할까

```python
func_by_lambda = lambda x: x + 10

def func_by_def(x):
    return x + 10


print(func_by_lambda)
<function <lambda> at 0x10266a7a0>
print(func_by_def)
<function func_by_def at 0x10266a660>

## 타입이 같지만 function의 이름이 lambda의 경우 정의 되어 있지 않은 것을 확인할 수 있음.

## 이 때 문제점이 객체를 파일로 저장하거나 불러오는 것이 불가능해진다.

## 결론1. map, filter에서 사용 가능한 단순한 함수를 구현해야할 때 사용하는 것은 괜찮습니다.

## 결론2. lambda를 많이 사용하는 것을 지양하세요! 알잘딱깔센!

## 결론3. 여러번 써야하는 함수인 경우 def를 사용하세요
```


## 전역변수, 지역변수

Global Scope, Local Scope라고도 불리는데 함수를 포함 스크립트 단에서 모든 요소가 해당 변수에 접근 할 수 있는 것이 전역 변수

```python
a = 10 # 전역변수

def fu():
    print(a) # 읽을 수는 있어요 주의주의!

fu()
```

```python
def fu():
    """
    Local Scope
    """
    a = 10 # 지역 변수
    print(a)

fu()
print(a) ## is not defined
```

그러면 어떻게 지역 변수를 바꿔야 할까?

```python
a = 10
def fu():
    global a # 전역 변수 a를 사용
    a = 20

fu()
print(a) # 20
```

그러면 def가 중첩되어 있으면 어떻게 될까?? 바로 위 스코프의 변수를 가져오기 위해서는 nonlocal을 사용하면 된다!

```python
def sol():
    a = 1
    def sol2():
        nonlocal a
        a = 10

    sol2()
    print(a)

sol()  # 20
```

## 주의해야할 점!
def는 새로운 scope를 만들지만 if, while, for, try의 경우에는 새로운 scope를 만들지 않으니 조심조심! 또한 global, nonlocal을 사용할 때에는 남용하지 말자!

```python
"""if 스코프 예시"""

a = 10
if a % 2 == 0:
    a = 20

print(a) # 20
```

```python
"""global 남용"""
x =  10
def sol(a, b):
    if a == b:
        global x
        x = 20

    else:
        global x 
        x = 30

"""바꾼 코드"""
x = 10
def sol(a:int, b:int) -> None:
    global x
    if a == b:
        x = 20
    else:
        x = 30
```


## 클로저를 알기위해 일급객체를 알아봅시다!

일급 객체는 몇 가지 조건을 만족하는 객체를 말해요
1. 변수 혹은 자료구조에 담을 수 있어야한다.
2. 매개변수로 전달할 수 있어야 한다.
3. 리턴값으로 사용될 수 있어야 한다.


### 예시 바로 두가시죠

```python
""" 변수 """
def fun(a,b):
    return a + b

a = fun

print(fun)
print(a)

print(fun is a)

print(a(1,2))
print(fun(1,2))
```

```python
""" list 할당 """
def sol(a, b):
    return a + b
def sol2(a, b):
    return a - b

new_list = [sol, sol2]

for i in new_list:
    print(i(3,1))


""" dict 할당 """
new_dict = {
    "add": sol,
    "minus": sol2,
}

result = new_dict['add'](3,1)
result2 = new_dict['minus'](3,1)


""" 매개변수 """
def sol_man(func, a, b):
    print(func(a,b))
```


## 그러면 일급 객체를 알아보았으니 클로저로 가보실까요?
우선 클로저의 정의로는 
- 클로저는 어떤 함수의 내부 함수가 외부 함수의 변수(*프리변수)를 참조할 때, 외부 함수가 종료된 후에도 내부 함수가 외부 함수의 변수를 참조할 수 있도록 어딘가에 저장하는 함수를 의미합니다.

즉, 어떠한 함수의 내부여야하며 해당 내부 함수가 외부 함수의 변수를 참조해야하고, 외부 함수가 내부함수를 리턴해야하는~~ 그런 느낌입니다!

또한 프리변수는 다른 함수에서는 사용되지만 함수 내부에서 선언 되지 않은 변수를 뜻해요! 아리쏭하다면 당신은 정상입니다.


```python
def hello(msg:str) -> func:
    message = "Hello, " + msg

    def say():
        print(message)

    return say

a = hello("jinwoo")
a() # Hello, jinwoo
```

여기서 여러분 머리위에 갈고리 수집해야 됩니다~
1. 함수가 종료가 되었는데 어떻게 'jinwoo'라는 매개변수를 기억할까?

이거를 알아보도록 하시죠

```python
print(dir(a)) # __closure__가 있는지 확인해보세여!
print(dir(a.__closure__))
print(a.__closure__[0].cell_contents)
# Hello, jinwoo
```

그러면 closure 메서드는 클로저 함수에만 있나요? 
답은  ㄴㄴ

```python
def wol():
    return "hi"

print(dir(wol)) # __closure__ 확인
print(wol.__closure__) # 값 확인
```

### 그러면 클로저를 왜 사용할까?
전역변수의 남발을 막기위해!


# 클래스!!!!!!!
드디어 클래스입니다 여러분.. 나 무서워..


### 클래스 속성
속성이 무엇인가요? 클래스에서 속성은 클래스 내부에 포함되어 있는 메서드 혹은 변수!

클래스 속성에 접근하는 경우 모든 클래스에 동일하게 영향이 있습니다.

그러면 self랑 다른게 무엇인가요?

self의 경우에는 인스턴스 속성!!! 

그리고 변수명 앞에 __를 붙이는 경우에는 비공개 속성으로 바꿀 수 있어요 :)

```python
class Sol:
    class_value = 0
    def __init__(self):
        self.instance_value = 0
    def set_instance_value(self):
        self.instance_value = 10
    def set_class_value(self):
        self.class_value = 15

sol1 = Sol()
sol2 = Sol()
```

이거 코드가지고 놀아보는 시간
instanace_value와 class_value를 사용해서 어떤 차이가 발생하는지 궁금하셔야해요~~

그러면 해당 인스턴스가 가지고 있는 속성은 어떻게 확인해요?

```python
sol1.__dict__ 한번 써보는 시간(인스턴스의 속성을 나타내주는 메서드)
```

근데 여기서 궁금한점이 있어야해요
그러면 메서드가 뭘까~
```python
def sol1():
    return 1

class Sol:
    def test(self) -> int:
        return 0

sol = Sol()

print(type(sol1))  # function
print(type(sol.test)) # method

즉 클래스 내부에 있는 함수를 메서드라한다~
```

그러면 다음!

```python
__dict__ <얘는 뭘까>
```


얘는 처음 들어보시는 분들도 계시고 아시는 분들도 계실테지만 Magic Method 혹은 Special Method라고 부릅니다~~ 저는 스페셜이라 자주 불러요~ 그러면 어떻게 사용되는 것일까

```python
class Sol:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b

sol = Sol()
sol1 = Sol()

print(sol)
sol + sol1
sol - sol1

```
되는게 있나요? 그러면 아래로 가보시져

```python
class Sol:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f'a는 {self.a}이고 b는 {self.b}야'

    def __add__(self, s: object) -> object:
        new_a = self.a + s.a
        new_b = self.b + s.b
        return Sol(new_a, new_b)

    def __sub__(self, s:object) -> object:
        new_a = self.a - s.a
        new_b = self.b - s.b
        return Sol(new_a, new_b)

    def __repr__(self) -> str:
        return f'Sol(a={self.a}, b={self.b})'

sol = Sol(1,2)
sol1 = Sol(3,4)
print(sol)
sol + sol1
sol1 - sol
sol

이와 같이 스페셜 메서드를 직접 구현함으로써 다양한 기능을 이용할 수 있다!
```

```python
여기서 여러분이 해보셔야할 것

class Sol:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b

sol1 = Sol(1,2)
sol2 = Sol(1,2)

sol1 == sol2
```

```python
class Sol:
    def __init__(self, a:int, b:int) -> None:
        self.a = a
        self.b = b

    def __eq__(self, other: object) -> bool:
        if other.__class__ == self.__class__:
            return(self.a, self.b) == (other.a, other.b)

sol1 = Sol(1,2)
sol2 = Sol(1,2)
sol1 == sol2
```


정적 메서드와 클래스 메서드?
@staticmethod
@classmethod

우선 클래스 메서드부터!
```python
class Sol:
    
    def __init__(self, name:str, age:int) -> None:
        self.name = name    
        self.age = age
    
    @classmethod
    def fList(cls, li:list) -> object:
        """
        cls는 여기서 Sol을 의미합니다~
        """
        return cls(li[0], li[1])
    
    @classmethod
    def fDict(cls, dic:dict) -> object:
        return cls(dic['name'], dic['age'])

sol1 = Sol.fList(['jinwoo', 44])
sol2 = Sol.fDict({
    'name': 'jinwoo',
    'age': 45
})


이런식으로 들어오는 값이 달라도 classmethod를 사용해 인스턴스를 만들 수 있습니다~
```

정적 메서드 => 원래 클래스의 메서드는 처음인자에 self를 주는 것이 문법이지만 staticmethod 데코레이터를 붙여주면 첫 번째 인자가 할당되지 않음! 
```python
class Sol:
    @staticmethod
    def textTolist(text:str) -> list:
        li = text.split()
        return li

sol = sol()
## 보통 유틸리티 메서드를 구현할 때 많이 사용합니다~
```

클래스 상속 => 어떠한 클래스의 기능을 그대로 물려받으면서 다른 기능을 추가할 때 사용

상속을 해주는 클래스 => 부모 클래스, 기반 클래스
상속을 받는 클래스 => 파생 클래스, 자식 클래스

우선 부모의 기능을 이어받는걸 확인(상속!)
```python

class Animal:
    def __init__(self ) -> None:
        self.isanimal = True
    def isAnimal(self) -> bool:
        return self.isanimal
    
class Dog(Animal):
    def __init__(self) -> None:
        self.isanimal = False

dog = Dog()
dog.isAnimal()
```


부모 클래스의 속성을 사용하고 싶을 때?
```python
class A:
    def __init__(self):
        self.a = 1


class B(A):
    def __init__(self):
        super().__init__()

b.a
```

그러면 만약에 상속이 두 번 이상 되었을 때 super()를 사용하면 어떻게 될까?

```python
class A:
    def __init__(self):
        self.a = 1


class B(A):
    def __init__(self):
        self.b = 2

class C(B):
    def __init__(self):
        super().__init__()


c = C()

c.a
```
다중 상속도 단일 상속과 다른건 없습니다!



## 추상클래스

구현되지 않은 클래스를 작성하여 해당 클래스를 상속 받을 때 모든 메서드를 재정의 해야하는 기능!!

```python
from abc import *

#sol은 이해하기 힘들 것 같아서 여기서는 바꿀게영 :)
class Family(metaclass = ABCMeta):
    @abstractmethod
    def family_name(self):
        pass


class You(Family):
    pass

a = You()

```


```python
from abc import *

#sol은 이해하기 힘들 것 같아서 여기서는 바꿀게영 :)
class Family(metaclass = ABCMeta):
    @abstractmethod
    def family_name(self):
        pass

class You(Family):
    def family_name(self):
        print("lee")


a = You()
```


## 예외처리

코드 발생중 에러가 진짜진짜 많이 나는데 해당 에러를 처리하기 위한 try except!

```python
def div(x:int) -> int:
    return 10 / x

try:
    div(0)  # 얘를 시도하고 에러가 발생하면

except: # 여기로 이동
    print("예외 발생!")
```

근데 어떤 에러가 나는지 알고 싶다? 내가 깔쌈하게 하고 싶다! 하시는분

```python
def div(x:int) -> int:
    return 10 /x

try:
    div(0)

except Exception as e: #해당 에러에 대한 내용을 e라 명명
    print(e)
```

아니면 특정 에러에 대해서만 예외 처리를 하겠다! 하시는 분은

```python
def div(x: int) -> int:
    return 10 /x 

try:
    div(0)

except ZeroDivisionError: # 이러면 ZeroDivisionError <- 이 에러에 대해서만 아래 print문이 실행
    print("0으로 나눌수 없셈")
```

try except 구문에서의 else 와 finally얘내는 의미만 정확하게 알면 됩니다

else => try 구문이 정상적으로 실행 되었을 때 실행되는 블럭

finally => try 구문이 실행이 되던 혹은 안되던 무조건 마지막에 실행되는 블럭

```python
# 이건 코딩 도장이 가장 이해가 잘가게 설명되어 있어서 가져왔어용
try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')
```

만약 내가 에러를 만들고 싶다!
```python

class FirstNameException(Exception):
    def __init__(self):
        super().__init__('첫 번째 성이 kim이 아닙니다')


def check_first():
    try:
        x = input("당신의 첫번째 이름")
        if x != "kim":
            raise FirstNameException
        print(x)

    except Exception as e:
        print(e)

check_first()
```


## 이터레이터!
제가 1주차에 iterable을 설명 드렸었는데요 iteralbe한 객체들로는 list, dict, set, str, bytes, tuple, range 등이 있다 말씀 드렸음둥

여기서 이 객체들의 공통점 => for문을 돌릴 수 있다~ and iterator로 바꿀 수 있다!

그래서 이터레이터는 뭔데?
iterable하고 __next__로 다음 값을 반환할 수 있으면 이터레이터
아니면 그냥 iterable한 객체~

그러면 iterator 객체는 어떻게 만들어요?
```python
a = [1,2,3,4,5]
a = iter(a)

print(a.__next__())
...
# 마지막에 도달 후 __next__()를 호출하면 StopIteration 에러 발생
```

### iterator는 언제 써요? For문을 잘 생각해보시면~

```python
for i in range(10):
    print(i)

여기서 for문은 내부적으로 in 뒤에오는 iterable한 값을 iterator로 만들어 __next__를 사용해 순회를 도는 방식이고 Stopiteration이 발생하면 탈출!
```


## Generator 제너레이터!
제너레이터 => 이터레이터를 생성하는 객체
모든 제너레이터는 전부 이터레이터이다! 제너레이터를 만드는 방법이 있는데 우선 컴프리헨션 및 yield 키워드를 사용하는 것!

앞에서 사용한 컴프리헨션을 써볼까요
```python
a = (i for i in range(10))
type(a) #어떻게 나오는지 확인해보세여!
```

그 다음! yield를 사용!
```python
def sol():
    for i in range(10):
        yield i

new = sol()
type(new)
```

yield는 값을 밖으로 전달 후 해당 yield에서 함수를 정지시킨다!!
```python
def sol():
    print("1전")
    yield 1
    print("1후 2전")
    yield 2
    print('2후 3전')
    yield 3
    print('3후')

new = sol()

print(new.__next__())
print(new.__next__())

# 이것도 한번 타이핑해보세여! 이해하기 편하실 거에요
```

그러면 계속 for문을 돌려야 값을 돌릴 수 있나요?
No!!
```python
def sol():
    li = [1,2,3,4,5]
    for i in li:
        yield i

new = sol()
print(new.__next__())
print(new.__next__())

# for문 귀찮아! 해서 만들어 놓은 것이 yield from

def sol1():
    li = [1,2,3,4,5]
    yield from li

new1 = sol1()
print(new1.__next__())
print(new1.__next__())

```

generator의 특징 하나 지연 평가(lazy evaluation) 제너레이터는 값을 반환할 규칙! 어디까지 반환을 했는지에 대한 상태값을 가지고 있지만 모든 값에 대해 메모리를 할당하지 않는다!

```python
def sol():
    num = 1
    while True:
        yield num
        num = num + 2

new = sol()

이렇게 무한 반복하는 코드가 있을 때 무한 반복하는 코드를 작성한다면 혹은 데이터가 너무 큰 값이 들어온다면 메모리가 비명을 지를텐데 이를 generator로 만들면 지연평가를 통해 메모리 낭비를 막을 수 있다!
```


## 코루틴 (얘는 많이 복잡해요.. 지금 이해 안가시면 천천히 보셔도 괜찮습니다.)
코루틴 => 루틴이 메인루틴과 종속적인 관계가 아닌 대등한 관계로 서로를 순차적으로 호출할 수 있게 되어 있는 함수! 제너레이터의 특별한 형태라 생각하시면 됩니다!

```python
def simple_coroutine():
    while True:
        print('코루틴 시작')
        x = yield
        print('받은 값: ', x)

new = simple_coroutine()
new.__next__()

new.send(10)
```


```python
def sol_send():
    while True:
        get_value = yield
        print(f"값은 {get_value}입니다")
        yield get_value

gen = sol_send()
values = [1,2,3,4,5]
for value in values:
    gen.__next__()
    gen.send(value)
```

여기서 보면 이전에 사용했던 yield값을 확인할 수 있습니다!


그러면 메인루틴과 서브루틴은 무엇?
```python
def add(a:int ,b:int) -> int: #서브루틴
    c = a + b
    return c


def calc() -> int: # 메인루틴
    x= add(1,2) 
    return x


calc()
```

마지막 보시면 좋을 코드..
```python
def coroutine2(x:int):
    print(f'>> 시작 값: {x}')
    y = yield x 
    print(f'>> Y 값: {y}')
    z = yield x + y
    print(f'>> Z 값: {z}')
    yield z + x + y



cr2 = coroutine2(10)
new = cr2.__next__() 
print('next1: ', new)

send_y = cr2.send(100) 
print('next2: ', send_y)

send_z = cr2.send(777) 
print('next3: ', send_z)
```


### 코루틴 종료하기

```python
def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end = '')
    except GeneratorExit:
        print()
        print('코루틴 종료')

co = number_coroutine()
co.__next__()

for i in range(10):
    co.send(i)

co.close()
```