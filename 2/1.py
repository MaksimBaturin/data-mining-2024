import matplotlib.pyplot as plt
from math import sqrt, pi, exp, erf

def rho_norm(x, mu=0, s=1):
    return 1/sqrt(2*pi*s)*exp(-(x-mu)**2/2/s**2)

def f_norm(x, mu=0, s=1):
    return (1+erf((x-mu)/sqrt(2)/s))/2

def inv_f_norm(p, mu, s, t=0.001): # t - точность
    # сначала перейдем к стандартному распределению
    if mu != 0 or s != 1:
        return mu + s * inv_f_norm(p,0,1,t)
    # ищем в полосе значений -100…100
    low_x, low_p = -100.0, 0
    hi_x, hi_p = 100.0, 1
    while hi_x - low_x > t:
        mid_x = (low_x + hi_x)/2
        mid_p = f_norm(mid_x)
        if mid_p < p:
            low_x, low_p = mid_x, mid_p
        elif mid_p > p:
            hi_x, hi_p = mid_x, mid_p
        else:
            break
    return mid_x

def p_value(x, mu=0, s=1):
    if x >= mu:
        return 2*(1-f_norm(x, mu, s))
    else:
        return 2*f_norm(x, mu, s)
    
def TestHypothesis(x, n):
    x = x/(8*n) * 100
    alpha = 0.05

    p_0 = 4/8
    p_a = 3/8

    mu_0 = n * p_0
    mu_a = n * p_a

    sigma_0 = sqrt(n * p_0 * (1-p_0))
    sigma_a = sqrt(n * p_a * (1-p_a))

    p_low = inv_f_norm(alpha/2, mu_0, sigma_0)
    p_high = 2*mu_0 - p_low

    P_value = p_value(x, mu_0, sigma_0)

    power = 1 - rho_norm(x,mu_a,sigma_a)
    if p_value(x, mu_0, sigma_0) > alpha:
        print(f"Критические точки: {p_low}, {p_high}")
        print(f"P-значение: {P_value}")
        print(f"Мощность: {power}")
        print("Нулевая гипотеза не опровергнута")
        return True
    return False

def plot_distribution(n, x):
    p_0 = 4/8
    mu_0 = n * p_0
    sigma_0 = sqrt(n * p_0 * (1-p_0))

   
    x_min = mu_0 - 4 * sigma_0
    x_max = mu_0 + 4 * sigma_0
    x_vals = [x_min + i*(x_max - x_min)/1000 for i in range(1001)]
    y_vals = [rho_norm(x, mu_0, sigma_0) for x in x_vals]

    plt.plot(x_vals, y_vals, label='Нормальное распределение')
    plt.axvline(x, color='r', linestyle='--', label='Наблюдаемое значение')
    plt.axvline(inv_f_norm(0.025, mu_0, sigma_0), color='g', linestyle='--', label='Критическая точка (нижняя)')
    plt.axvline(2*mu_0 - inv_f_norm(0.025, mu_0, sigma_0), color='b', linestyle='--', label='Критическая точка (верхняя)')
    plt.legend()
    plt.title(f'Нормальное распределение для i={n} часов и')
    plt.xlabel('x')
    plt.ylabel('Плотность вероятности')
    plt.show()

NumbOfTiles = 700
for i in range(1, 1000):
    if TestHypothesis(NumbOfTiles, i):
        print(f"Потребовалось {i} часов")
        plot_distribution(i, NumbOfTiles/(8*i) * 100)
        break