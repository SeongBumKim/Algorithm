# 01-1 L,R,U,D Move
n = int(input())
plans = input().split()
x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
movetype = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(movetype)):
        if plan == movetype[i]:
            mx = x + dx[i]
            my = y + dy[i]
    if mx < 1 or my < 1 or mx > n or my > n:
        continue

    x, y = mx, my

print(x, y)


# 01-2 Time
N = int(input())
count = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)


# 02 왕실의 나이트
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
        count += 1

print(count)


# 03 게임 개발
N, M = map(int, input().split())
x, y, direction = map(int, input().split())

d = [[0] * M for _ in range(N)]
d[x][y] = 1

array = []
for i in range(N):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] == 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: 
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)