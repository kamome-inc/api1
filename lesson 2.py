import requests
import json

"""Запрос на сайт почты, по стоимости посылки от, до, масса, ценность, с учетом НДС
КОДЫ ОТВЕТОВ HTML; Код 200 - успешно 

отличия post и get requests: гет работает с url = <сайт>?<параметры>
                             пост работает post(url, headers, <параметры>)
                             
Для передачи параметров в виде как GET необходимо выставить: 
                "Content-type": "application/x-www-form-urlencoded",
    Параметры: "from=105064&to=620000&mass=600&valuation=500&vat=1"  
              
Для передачи параметров в виде JSON:
                "Content-type": "application/json",
    Параметры: json.dumps(<словарь с параметрами>) # что за функция???
    

"""

request_headers = {
    "Content-type": "application/json",
    "Accept": "aplication/json;charset=UTF-8"
}

url = "https://postprice.ru/engine/russia/api.php?from=105064&to=620000&mass=600&valuation=500&vat=1"

response = requests.get(url, headers=request_headers)
print("Код ответа: ", response.status_code)

# Какая разница между Load и Loads в Json???
response = json.loads(response.text)
print(response)
print("Стоимость отправки простого письма: ", response["simple_letter"], "руб.")