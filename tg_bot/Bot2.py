# -*- coding: utf-8 -*-

import requests
import json
TOKEN_DADATA = "d6c4e6cc7f93ad1ff6b8e8c76528d501135eb7ec"
URL_DADATA = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"

#for telegram bot
TOKEN_BOT = '1988666354:AAEN2cxASigBH-fBmglNBaFzY1Io1tkuV1k'

#for api leasing-trade
TOKEN_LT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjVkYjE1Y2U2MjQwZGRkMDhjYWUwZmIxMiIsImlhdCI6MTYyOTQ0OTA0OX0.7VggX0mQFEAC2Y7uyRDhn33_FoVr1iEf4SevWUWqyFI'
URL_LT = 'https://api2.leasing-trade.ru:4000/graphql'

#for api damia
TOKEN_DM = '8b67f61866498ce93c36257099f2f44de00b37b4'
URL_DM = 'https://api.damia.ru/rs/balance'
YEAR_DM = '2020'
CODE_DM = '2110'
message = '1655096633'


def get_info_DM(message):
    try:
        param_request = {'inn': message, 'key': TOKEN_DM}  
        response = requests.get(URL_DM,  params=param_request)
        z = response.status_code
        if z == '200':
            print("Не удалось получить ответ от сервера.")
        else:
            data = json.loads(response.text)
            DM=[]
            DM.append(data[message][YEAR_DM][CODE_DM])
            x = DM[0] 
            print("Выручка за 2020 год: " + str(x) + " тыс.руб.")
    except Exception as e:

        print(e)


get_info_DM(message)
