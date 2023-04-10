countries_and_rivers = {
    'Қазақстан': ['Ертіс', 'Іртіш', 'Шу', 'Тобыл', 'Қарағанды'],
    'Россия': ['Волга', 'Дон', 'Обь'],
    'Канада': ['Святой Лаврентий', 'Маккензи'],
    'США': ['Миссисипи', 'Колорадо', 'Колумбия'],
    'Китай': ['Янцзы', 'Хуанхэ', 'Гань'],
    'Бразилия': ['Амазонка', 'Парана', 'Сан-Франсиску'],
}
def ozen_out():
    print('Ел мен өзендер тізімі:')
    for country, rivers in countries_and_rivers.items():
        for river in rivers:
            print(f'{river} : {country}')

def el(river):
    for country, rivers in countries_and_rivers.items():
        if river in rivers:
            return (f'{river} — {country}')
            break
    else:
        return(f'{river} — табылмады')
ozen_out()
i=0
while i<5:
    river=input("Өзен аты:") 
    print(el(river))

