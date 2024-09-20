import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def GetData(data = []):
    url = 'https://cryptocharts.ru/bitcoin-dollar/'
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    table_class = 'TableRates'
    table = soup.find('table', class_=table_class)

    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        for cell in cells[1::2]:
            data.insert(0, cell.text.strip())

def gauss(M, b):
    n = len(M)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(M[j][i]) > abs(M[max_row][i]):
                max_row = j
        M[i], M[max_row] = M[max_row], M[i]
        b[i], b[max_row] = b[max_row], b[i]

        for j in range(i + 1, n):
            factor = M[j][i] / M[i][i]
            b[j] -= factor * b[i]
            for k in range(i, n):
                M[j][k] -= factor * M[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / M[i][i]
        for j in range(i - 1, -1, -1):
            b[j] -= M[j][i] * x[i]
    return x

def approx_poly(x, t, r):
    M = [[] for _ in range(r + 1)]
    b = []
    for l in range(r + 1):
        for q in range(r + 1):
            M[l].append(sum(list(map(lambda z: z ** (l + q), t))))
        b.append(sum(xi * ti ** l for xi, ti in zip(x, t)))
    a = gauss(M, b)
    return a

#Гипотеза h0
h0 = 4

#Гипотеза ha
ha = 5

dataset = []
GetData(dataset)
dataset = [float(value.replace(',', '.')) for value in dataset]  # Преобразуем строки в числа
t = list(range(len(dataset)))

A_0 = approx_poly(dataset, t, h0)
A_a = approx_poly(dataset, t, ha)
# Вычисляем аппроксимированные значения

x_0_approx = [sum(A_0[i] * ti ** i for i in range(len(A_0))) for ti in t]
x_a_approx = [sum(A_a[i] * ti ** i for i in range(len(A_a))) for ti in t]

# Строим график
plt.figure(figsize=(10, 6))
plt.plot(t, dataset, label='Исходные данные', marker='o')
plt.plot(t, x_0_approx, label=f'Аппроксимированная кривая {h0} степени', linestyle='-')
plt.plot(t, x_a_approx, label=f'Аппроксимированная кривая {ha} степени', linestyle='-')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('Аппроксимация полиномом')
plt.legend()
plt.grid(True)
plt.show()