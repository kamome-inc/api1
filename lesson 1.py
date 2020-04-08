import requests
import pandas as pd  # создает дата фреймы для обработки данных
import json
req = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")

data = pd.DataFrame(json.loads(req.text)["Valute"])
print(data["USD"])
print(req.text)

"""
Изучить библиотеки, разобраться с назначением библиотеки Пандас
"""