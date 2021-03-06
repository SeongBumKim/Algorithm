# 모든 데이터를 하나씩 확인하여 합계 계산
array = [3,5,1,2,4]
sum = 0

for i in array:
    sum += i

print(sum)
# 시간 복잡도 O(N)

for i in array:
    for j in array:
        temp = i*j
        print(temp)
# 시간 복잡도 O(N^2)

#소스코드 시간 측정
import time
start_time = time.time() # 측정 시작
#프로그램 소스 코드
end_time = time.time() 
print("time :", end_time-start_time)

#선택 정렬과 기본 정렬 라이브러리의 수행시간 비교
from random import randint
import time

    #배열에 10,000개의 정수 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100 사이의 랜덤한 정수

    #선택 정렬 프로그램 성능 측정
start_time = time.time()

    #선택 정렬 프로그램 소스코드
for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와이프

end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정:", end_time-start_time) #수행시간 출력

#배열을 다시 무작위로 초기화
array = []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100 사이의 랜덤한 정수

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

array.sort()

end_time = time.time()
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)

    

