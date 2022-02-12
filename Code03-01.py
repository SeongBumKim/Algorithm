# 전역 변수부
katok = ['다현', '정연', '쯔위', '사나', '지효']

#메인코드부
print(katok)

#데이터 추가 (맨 뒤)
katok.append(None)
katok[5] = '모모'
print(katok)

#데이터 삽입
katok.append(None)
katok[6] = katok[5]
katok[5] = None
katok[5] = katok[4]
katok[4] = None
katok[4] = katok[3]
katok[3] = None
katok[3] = '미나'
print(katok)

#데이터 삭제
katok[4] = None
katok[4] = katok[5]
katok[5] = katok[6]
katok[6] = None
del (katok[6])
print(katok)
