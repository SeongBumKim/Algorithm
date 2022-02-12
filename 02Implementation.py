# # 01-1 L,R,U,D Move
# n = int(input())
# plans = input().split()
# x, y = 1, 1

# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# movetype = ['L', 'R', 'U', 'D']

# for plan in plans:
#     for i in range(len(movetype)):
#         if plan == movetype[i]:
#             mx = x + dx[i]
#             my = y + dy[i]
#     if mx < 1 or my < 1 or mx > n or my > n:
#         continue

#     x, y = mx, my

# print(x, y)


# # 01-2 Time
# N = int(input())
# count = 0

# for h in range(N + 1):
#     for m in range(60):
#         for s in range(60):
#             if '3' in str(h) + str(m) + str(s):
#                 count += 1

# print(count)


# 02 왕실의 나이트

