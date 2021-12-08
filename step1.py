def test():
    print("welcome!")


def test1(a,b):
    print(a+b)
    pass


def controlStatement():
    #1~10까지 반복문 작성
    for i in range(1,11):
        print(i, end="\t")
        pass
    print()
    for letter in 'abcde':
        print(letter, end="\t")
    print()
    for i in range(1,11):
        if(i % 2 == 0):
            print(i)
            pass
        pass


    pass


def viewCalendar():
    # 8월 달력을 출력하는 코드 작성하세요
    print("\t\t\t8월\t\t\t")
    print("일\t월\t화\t수\t목\t금\t토")
    for i in range(1,32):
        print(i, end="\t")
        #if i%7==0:
        if i==7 or i==14 or i==21 or i==28:
            print()
        pass
    pass

# 윤년 체크 2021년 2월 윤년여부를 확인하여 결과를 리턴하는 코드 작성
def isLeapYear():
    flag = False # 윤년이 아니다.
    year = 2021
    condition1 = year % 400 == 0
    condition2 = year % 4 == 0 and year % 100 != 0
    if condition1 or condition2:
        flag = True
    return flag










