'''
10869 사칙연산
[문제]
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

[입력]
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
- 예제 : 7 3

[출력]
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
- 예제
10
4
21
2
1
'''
# A, B = input().split() # -> int 변환하는 코드가 들어가야한다
A, B = map(int, input().split()) # -> int 변환하는 코드가 들어가야한다
# print("A :", A, "B :", B)

print(A + B)  # (10) 첫째 줄 : A + B -> 73 (우리의 예상은 10인데 왜 73? -> 문자열)
print(A - B)  # (4) 둘째 줄 : A - B
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(A * B)  # (21) 셋째 줄 : A * B
# print(A / B)  # (2 <- 2.3333333....) 넷째 줄 : A / B
# 나머지 없는 정수 형태의 결과값을....
# print(A // B) # 4-1
print(int(A / B)) # 4-2
print(A % B)  # (1) 다섯째 줄 : A % B
