import time
from unittest import result
# 01. 거스름돈
# 거스름돈 500,100,50,10원이 무한히 존재할 때 N원을 최소 동전개수로 거슬러줄 수 있는 방안

n = 1260
count = 0

#큰 단위의 화폐부터 차례대로 확인
coin_type = [500, 100, 50 ,10]

for coin in coin_type:
    count = count + n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n = n % coin

print(count)


# 02. 큰 수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() 
# 오름차순 정렬

first = data[n-1]
second = data[n-2]

result = 0

start_time = time.time()

while True:
    for i in range(k):
        if m == 0:
            break
        result = result + first
        m = m - 1
    if m == 0:
        break
    result = result + second
    m = m - 1

end_time = time.time()

print(result)
print("경과시간 ", end_time - start_time)


# 03. 숫자 카드 게임
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)


# 04. 1이 될 때까지
n, k = map(int, input().split())
count = 0

while n >= k:
    while n % k != 0:
        n -= 1
        count += 1
    n = n // k
    count += 1

while n > 1:
    n -= 1
    count += 1

print(count)




