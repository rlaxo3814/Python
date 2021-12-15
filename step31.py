def hello():
    return 'hi'


from datetime import datetime as dt

def getCurrentDate():
    today = dt.now()
    print(today)
    strtoday = today.strftime('%Y/%m/%d %H:%M:%S')
    print(strtoday)
    pass

class Test:
    def __init__(self):
        self.id = 'admin'
        self.pwd = '1234'

    pass