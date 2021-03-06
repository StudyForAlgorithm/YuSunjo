# 가로의 길이가 N, 세로의 길이가 2
# 1X2, 2X1, 2X2의 덮개로 채우려고 할 때 -> 바닥을 채우는 모든 경우의 수

# 입력: 가로의 길이 N
# 출력: 바닥을 채우는 경우의 수
n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + d[i - 1] * 2) % 796796

print(d[n])
