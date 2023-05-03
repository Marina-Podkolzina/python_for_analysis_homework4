import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:/Users/obluch/Downloads/kc_house_data.csv', encoding='latin-1')
df.head()# покажет первые 5 значений таблице сверху
print(df.head())

# Задача 1
#Постройте график
#Назовите график
#Сделайте именование оси x и оси y
#Сделайте выводы
#1.1. Скачать данные по ссылке


#1.2 Изучите стоимости недвижимости

# Строим гистограмму с помощью atplotlib

plt.figure(figsize=(6,4))
plt.hist(df['price'], bins= 20)
plt.title('Распределение стоимости недвижимости')
plt.xlabel('Стоимость')
plt.ylabel('Количество')
plt.show()
# Вывод: Колличество домов прямопропорционально их цене.

 
#1.3 Изучите распределение квадратуры жилой

#Строим гистограмму с помощью seaborn 

plt.figure(figsize=(6,4))
sns.histplot(df['sqft_living'], bins=20)
plt.title('Распределение жилой площади')
plt.xlabel(' Жилая квадратура')
plt.ylabel('Количество')
plt.show()

# Вывод: Большая часть недвижимости имеет небольшие или средние показатели квадратуры.


#1.4 Изучите распределение года постройки

#Строим гистограмму с помощью seaborn 

plt.figure(figsize=(6,4))
sns.histplot(df['yr_built'], bins=30)
plt.title('Распределение года постройки')
plt.xlabel('Год постройки')
plt.ylabel('Количество')
plt.show()

# Вывод: Большая часть недвижимости была построена в период: с 1950г до 2017г. Самый пик пришелся на начало 2000х