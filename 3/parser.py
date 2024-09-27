from bs4 import BeautifulSoup
import requests
from time import sleep
from datetime import datetime, timedelta

# Функция для проверки даты
def is_recent(date_str):
    try:
        # Преобразуем строку даты в объект datetime
        date = datetime.strptime(date_str, '%d %B %Y, %H:%M')
        # Проверяем, что дата не старше суток
        return datetime.now() - date <= timedelta(days=1)
    except ValueError:
        return False

# Минимальная и максимальная допустимая цена
MIN_PRICE = 1000  # Минимальная цена, например, 1000 рублей
MAX_PRICE = 100000  # Максимальная цена, например, 100000 рублей

page = 1
url = f'https://www.avito.ru/simferopol/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?cd=1&geoCoords=44.948314%2C34.100192&p={page}&radius=100&searchRadius=100'
base_url_str = 'https://www.avito.ru/'
data = []

while True:
    response = requests.get(url)
    html_content = response.text    
    # Создаем объект BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    items = soup.find_all('div', attrs={'data-marker': 'item'})

    if items == []: break

    for item in items[:2]:
        id = item.get("id")
        name = item.find('h3', attrs={"itemprop":"name"}).text.strip()
        price =  item.find('meta', attrs={"itemprop":"price"})["content"]

        item_url = item.find('a', attrs={"itemprop":"url"})["href"]
        item_response = requests.get(base_url_str + item_url)
        item_html = item_response.text
        soup = BeautifulSoup(item_html, 'html.parser')
        date = soup.find('span', attrs={"data-marker" : "item-view/item-date"}).text.strip()

        data.append({
            "id:": id,
            "name": name,
            "price": price,
            "date": date
        })
        sleep(0.1)
    page += 1

# Фильтрация данных после парсинга
filtered_data = []
seen_ids = set()  # Множество для хранения уникальных ID

for item in data:
    id = item["id:"]
    if id in seen_ids:
        continue  # Пропускаем дубликаты
    seen_ids.add(id)

    price = float(item["price"])
    if not (MIN_PRICE <= price <= MAX_PRICE):
        continue  # Пропускаем объявления с некорректной ценой

    date = item["date"]
    if not is_recent(date):
        continue  # Пропускаем объявления, которые старше суток

    filtered_data.append(item)

# Выводим результат
print(filtered_data)