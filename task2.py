import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:/Users/obluch/Downloads/kc_house_data.csv', encoding='latin-1')
df.head()# покажет первые 5 значений таблице сверху
print(df.head())

#Задача 2

#Постройте график
#Сделайте выводы

#2.1 Изучите распределение домов от наличия вида на набережную

# Готовим данные для круговой диаграммы
data = df['waterfront'].value_counts()
expl = [0.2, 0.5] 
list_colors =['#6338f2', '#9c168c']  

# Строим круговою диаграмму
plt.figure(figsize=(6, 4))
plt.pie(data, autopct='%1.1f%%', colors=list_colors, explode= expl)
plt.legend(['no', 'yes'])
plt.show()

# Вывод: Вид на набережную имеет только 0.8 % недвижимости.

#2.2 Изучите распределение этажей домов

# Готовим данные для круговой диаграммы
data_f = df['floors'].value_counts()
names = data_f.index
values = data_f.values

expl_2 = [0.2, 0.03, 0.04, 0.05, 0.07, 0.5]

# Строим круговою диаграмму
plt.figure(figsize=(8, 6))
plt.pie(values, labels= names, autopct='%1.1f%%', explode= expl_2)
plt.title('Количество этажей')
plt.show()
# Вывод: Большая часть недвижимости - это  одноэтажные дома, они составили 49.4%, на втором месте - двухэтажные (38.1%)


#2.3Изучите распределение состояния домов

# Готовим данные для круговой диаграммы

data_с = df['condition'].value_counts()
names1 = data_с.index
values1 = data_с.values
expl_3 = [0.2, 0.03, 0.04, 0.05, 0.9]

# Строим круговою диаграмму
plt.figure(figsize=(6, 4))
plt.pie(values1, labels= names1, autopct='%1.1f%%', explode= expl_3)
plt.title('Состояние домов')
plt.show()


# Вывод: Большая часть недвижимости - это дома с оценкой состояния на троечку,они составили 64.9%. Дома в хорошем состоянии на   втором месте и они составляют 26.3%. Домов в отличном состоянии  всего 7.9%. Домов в плохом и отвратительном состоянии минимальное, незначительное количество

