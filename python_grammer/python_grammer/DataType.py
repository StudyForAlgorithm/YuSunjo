# 정수형, 실수형,

# 소수부가 0일 때는 0 생략 가능
a = 5.
print(a)

# e 다음에 오는 수는 10의 지수부 -- 특정 변수에 10억을 넣어야 할 경우 1e9라고 넣는다.
b = 1e9
print(b)

c = 23.4e1
print(c)

# 실수를 처리 할 때 부동 소수점 방식 사용(부호부 1이면 음수 0이면 양수, )
# 2진수에서는 0.9를 정확히 표현 못함
a = 0.3 + 0.6
print(a)  # 0.89999999..

# round(a) => 소수 첫째자리에서 반올림
a = 0.3 + 0.6
print(round(a, 2))

# /  -> 나누기(소수점까지)
# %  -> 나머지
# // -> 나누기(몫만)
# ** -> 거듭제곱

# 형변환 int() str()

