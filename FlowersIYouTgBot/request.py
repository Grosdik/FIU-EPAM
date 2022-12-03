import requests
import json
import time

"""while(True):
    link = 'http://localhost:53116/Orders/GetOrderInfo'
    responseL = requests.get(link).text

    if(responseL != 'null'):
        link = 'http://localhost:53116/Orders/GetUnacceptedOrders'
        responseC = requests.get(link).text

        countOrders = int(responseC);

        PauseTime = 30

        if(countOrders == 0):
            PauseTime = 30
        elif(countOrders > 0 and countOrders < 5):
            PauseTime = 15
        else:
            PauseTime = 5

        data =  json.loads(responseL)

        count_msv = len(data['products'])

        address = data['address']
        result = 'Адрес: ' + address

        for x in range(0, count_msv):
            prod = data['products'][x]['name']
            result += '\nПозиция для доставки №' + str(x+1) + ': ' + prod

        print(result)

        urlQ = 'http://localhost:53116/Orders/AcceptOrder/' + str(data['id'])

        response = requests.put(urlQ, json={
            # 'Date': '2022-03-26 00:00:00.000',
            # 'Address': '45.062445, 38.998157',
            # 'Decription': '',
            # 'Price': 25999,
            # 'Range': 4452,
            # 'IsPaid': True,
            'IsAccepted': True
        })


        print(response.status_code)
        time.sleep(PauseTime)
"""
url = 'http://localhost:53116/Orders/AcceptOrder/' + "8"

response = requests.put(url, json={
    'IsAccepted': False
})

print(response.status_code)

link = 'http://localhost:53116/Orders/GetOrderInfo'
responseL = requests.get(link).text
print(responseL)
