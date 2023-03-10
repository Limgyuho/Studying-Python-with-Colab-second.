# -*- coding: utf-8 -*-
"""파이썬 기본 공부 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1s3s0RFuXlJ3oNqap42Ms04_FvmeKMPMx
"""

# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_dan(dan,limit): #매개변수-지역변수 매겨변수와 인자의 개수가 맞아야 한다
  print("== {}단 ==".format(dan))
  i = 1
  while i <= limit:
    print("{} * {} = {}".format(limit, i, limit * i))
    i += 1

print_dan(1,1) #매개변수와 인자의 개수가 같아야 한다
print_dan(2,2)
print_dan(3,3)
print_dan(4,4)
print_dan(5,5)
print_dan(6,6)
print_dan(7,7)
print_dan(8,8)
print_dan(9,9)

# 문제 : 매개변수의 개수를 맞춰주세요.
# 조건 : 함수호출 시 사용한 인자에 따라 함수를 적절하게 잘 만들어 주세요.
# 조건 : 오류가 나지 않으면 성공입니다.
def a():
  print("a실행")
def b(a,b,c):
  print("a: {},b : {},c : {}".format(a,b,c))
def c (a,b,c,d):
  print("a: {},b : {},c : {},d : {}".format(a,b,c,d))


a()
b(1, 2, 3)
c("안녕", 1 == 1, 550, 600)

# 문제 : 입력받은 정수의 모든 약수를 출력하는 함수를 구현해주세요.

def print_divisors(num):
  i = 1
  # 구현

  while i<= num:
    if num % i == 0:
      print(i)
    i+=1

print_divisors(1000)

#함수의 리턴
#함수의 리턴이 사용되면 아래의 코드는 실행하지 않는다 
#def plus(a,b):
#  print(a+b)
#  return 10

#s = plus(20,30)
#print("s : {}".format(s))

#함수안에 조건문이 있으면 조건에 따라 리턴을 사용가능하다
#def plus(a,b):
#  if a+b == 50:
#    return a+b

#  return a-b

#s = plus(30,30)
#print("s : {}".format(s))

#리턴에 조건문을 넣어 코드를 더욱 줄일 수 있다
def is_adult(age):
  return age > 19

print("20 is adult? : {}".format(is_adult(20)))
#.format(is_adult(20))의 인자가 매개변수에 들어가
#리턴의 결과값을 출력해준다

# 문제 : 5칙연산을 수행하는 함수를 만들어주세요.

# plus 함수 구현

def plus(a,b):

  return a+b

print("3 더하기 5는 {} 입니다.".format(plus(3, 5)))
# 출력 => 3 더하기 5는 8 입니다.

# plus_3_nums 함수 구현

def plus_3_nums(a,b,c):
  
  return a+b+c

print("3 더하기 5 더하기 7은 {} 입니다.".format(plus_3_nums(3, 5, 7)))
# 출력 => 3 더하기 5 더하기 7은 15 입니다.

# minus 함수 구현

def minus(a,b):
  
  return a-b

print("10 빼기 5 는 {} 입니다.".format(minus(10, 5)))
# 출력 => 10 빼기 5 는 5 입니다.

# multiply 함수 구현
def multiply(a,b):
  
  return a*b


print("10 곱하기 5 는 {} 입니다.".format(multiply(10, 5)))
# 출력 => 10 곱하기 5 는 50 입니다.

# mod 함수 구현

def mod(a,b):
  
  return a%b

print("4를 3으로 나눈 나머지는 {} 입니다.".format(mod(4, 3)))
# 출력 => 4를 3으로 나눈 나머지는 1 입니다.

# div 함수 구현

def div(a,b):
  
  return a//b

print("4를 3으로 나눈 몫은 {} 입니다.".format(div(4, 3)))
# 출력 => 4를 3으로 나눈 몫은 1 입니다.

# div2 함수 구현

def div(a,b):
  
  return a/b

#print("4를 3으로 나눈 결과는 {} 입니다.".format(div2(4, 3)))
# 출력 => 4를 3으로 나눈 결과는 1.3333333333333333 입니다.

# 문제 : 온도단위 섭씨를, 화씨로 바꿔주는, 함수 c_to_f 를 구현해주세요.
# 조건 : 공식 = 섭씨온도 * (9 / 5) + 32 => 화씨온도

def c_to_f(c):
 
  return c * (9 / 5) + 32

print(c_to_f(10))
# 출력 => 50.0
print(c_to_f(20))
# 출력 => 68.0
print(c_to_f(30))
# 출력 => 86.0

# 문제 : 입력받은 정수가 짝수인지 아닌지 판별해주는 함수 구현

def is_even(num):
  
  return num % 2 ==0
  

print("10은(는) 짝수인가요? : {}\n".format(is_even(10)));
print("11은(는) 짝수인가요? : {}\n".format( is_even(11)));

# 문제 : 입력받은 정수가 3의 배수인지 알려주는 함수 구현
def is_3_multiple(num):
  return num % 3 ==0

print("10은(는) 3의 배수인가요? : {}\n".format(is_3_multiple(10)))
print("12은(는) 3의 배수인가요? : {}\n".format(is_3_multiple(12)))

#문제 : 입력받은 정수가 100보다 큰지 알려주는 함수 구현

def is_bigger_than_100(num):
  
  return num >100

print("128은(는) 100보다 큽니다. : {}\n".format(is_bigger_than_100(128)));
print("28은(는) 100보다 큽니다. : {}\n".format(is_bigger_than_100(28)));