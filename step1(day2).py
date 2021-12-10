def hello():
    return 'hello! World'


import random
def makeRandomNumber():
    # 1~45까지 수중 랜덤으로 6개의 수를 생성해서 리스트에 삽입한 후 출력
    # 하는 코드 작성 --> 중복처리 하시오
    list = []
    for _ in range(6):
        rnd = random.randint(1,45)
        list.append(rnd)
        #print(rnd, end=" ")
    print(list)
    print(sorted(list))
    print(list)
    print(list.sort())
    print(list)
    pass


def getLottoNumber():
    mlist = []
    while True:
        rnd = random.randint(1,45)
        if rnd not in mlist:
            mlist.append(rnd)
            pass
        if len(mlist)==6:
            break
            pass

    print(sorted(mlist))
    pass

import calendar
def getMonthData():
    date, lastDay = calendar.monthrange(2021,11)
    print(date, lastDay)
    pass


def viewMonth(year,month):
    space, lastDay = calendar.monthrange(year, month)
    print("\t\t{0}년 {1}월\t\t".format(year,month))
    print("일\t월\t화\t수\t목\t금\t토")
    for _ in range(space+1):
        print(" ",end="\t")

    for i in range(1,lastDay+1):
        print(i, end="\t")
        if (space+1+i)%7==0:
            print()
        pass
    pass