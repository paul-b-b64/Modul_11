import pandas as pd
from matplotlib import pyplot as plt

# загружаем таблицу из файла Excel
with pd.ExcelFile('Test.xlsx') as excel:
    tabl = pd.read_excel(excel, header=0)
    print(tabl)

# добавил столбцы
tabl['Цвет глаз'] = ['серый', 'голубой', 'малиновый', 'красный', 'зеленый', 'прозрачный']
print(tabl)
tabl['Возраст'] = [33, 23, 34, 34, 25, 45]
print(tabl)
# выводим столбец с телефонами
print(tabl['Телефон'])
# выводим вторую запись
print(tabl.iloc[1])
# печатаем график возраста клиентов
sf = tabl.plot(x='Nпп', y=['Возраст'])
plt.show()
