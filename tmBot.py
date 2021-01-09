import requests
import json
import time


print('Введите API ключ:')
#iN7VqdLoBtD2L5R22csH5YOwckDlZl6
KEY = input()
print('Введите шаг изменения цены(в рублях):')
step = float(input())
print('Введите процент максимального изменения цены:')
minPercent = float(input())/100
print('')
print('Запуск бота!')


firstItemList = requests.get(f'https://market.csgo.com/api/Trades/?key={KEY}').json()
while True:
    try:
        for i in firstItemList:
            classid = i['i_classid']
            instanceid = i['i_instanceid']
            ui_id = i['ui_id']
            minPrice = requests.get(f"https://market.csgo.com/api/BestSellOffer/{classid}_{instanceid}/?key={KEY}").json()

            if minPrice['success'] == True:
                price = str(float(minPrice['best_offer']) - (step * 100))
                if ((float(i['ui_price']) - (float(i['ui_price']) * minPercent)) * 100) < float(price):
                    suc = requests.get(f"https://market.csgo.com/api/SetPrice/{ui_id}/{price}/?key={KEY}")
                    if suc['success'] == True:
                        print(f"Цена для {i['i_name']} изменена!")
                        print(f"Новая цена: {str(float(price)/100)}")


            time.sleep(5)




        time.sleep(180)

    except Exception as e:
        print(str(e))
