import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(r'C:/Users/obluch/Downloads/kc_house_data.csv', encoding='latin-1')
df.head()# покажет первые 5 значений таблице сверху
print(df.head())


# Задача 3

#Исследуйте, какие характеристики недвижимости влияют на стоимость недвижимости, с применением не менее 5 диаграмм из урока.
#Анализ сделайте в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.

 # 1. Построим матрицу корреляции

corr_matrix = df.corr(numeric_only=True)
corr_matrix = np.round(corr_matrix, 1)
corr_matrix[np.abs(corr_matrix) < 0.3] = 0
corr_matrix


plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, linewidths=.5, cmap='coolwarm')
plt.title('Correlation matrix')
plt.show()

# 2. Изучим взаимосвязь стоимости и жилой площади

sns.jointplot(x=df['price'], y=df['sqft_living'], kind='reg')
plt.show()

# Вывод: Здесь прослеживается линейная связь. Значит чем выше  стоимость недвижимости, тем больше жилая площадь.



# 3.Изучим взаимосвязь стоимости и уровень качества

sns.jointplot(x=df['price'], y=df['grade'], kind='reg')
plt.show()

# Вывод: Здесь прослеживается линейная связь. Значит чем выше качество конструкции и дизайна дома, тем выше его стоимость.



# 4. Изучим взаимосвязь стоимости и уровеня качества с помощью Диаграммы размаха (ящик с усами)

plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'], y=df['grade'].astype('str'), whis=1.5)
plt.xlabel('Стоимость')
plt.ylabel('Уровень качества')
plt.title('Взаимосвязь стоимости и уровеня качества')
plt.show()

# Вывод:  Наибольшую стоимость имеют дома с уровень качества 13.
# А наиболее доступные по цене дома имеют уровень качества на 3, 4, 5, 6,7



# 5. Изучим взаимосвязь стоимости и этажности с помощью Диаграммы размаха (ящик с усами)


plt.figure(figsize=(6,4))
sns.boxplot(x=df['price'], y=df['floors'].astype('str'), whis=1.5)
plt.xlabel('Стоимость')
plt.ylabel('Этажность')
plt.title('Взаимосвязь стоимости и этажности')
plt.show()

# Вывод:  Наибольшую стоимость имеют дома  с количеством этажей 2,5 -  3,5.




