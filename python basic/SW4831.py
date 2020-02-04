# -*- coding: utf-8 -*-

T= int(input())
for i in range(T):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))   # 충전소가 설치된 정류장 입력


    chargeCount = 0
    busRange = K
    chargeStation = 0
    busStation = []

    for num in range(N+1):               # 버스 정류장 생성
        if num in M_list:
            busStation.append(1)
        else:
            busStation.append(0)

    M_list.append(N)          # 종점을 충전소 리스트에 입력

    for x in range(1, N):

        if busStation[x] == 1:
            busRange -= 1               # 다음 정류장에 도착했기 때문에 거리 -1
            
            if busRange < 0:           # 버스 이동 가능거리가 초과 했을 경우 0으로 변환 후 for문 종료 
                chargeCount = 0
                break

            if (M_list[chargeStation + 1] - M_list[chargeStation]) > busRange:

                chargeCount += 1
                busRange = K

            chargeStation += 1           # 충전소를 지나면서 충전소 숫자를 더함
        else:
            busRange -= 1                # 다음 정류장에 도착했기 때문에 거리 -1
            



    print(f'#{i+1} {chargeCount}')


