import requests
def sendURL():
    url = 'http://localhost:9090/echo/reqInfo'
    data = {'id':'admin','pwd':'1234'}

    response = requests.post(url,data)
    print(response.text)

    pass