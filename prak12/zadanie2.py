# Открываем файлы с именами девочек и мальчиков
with open('GirlNames.txt', 'r') as girl_names_file:
    girl_names = girl_names_file.read().splitlines()

with open('BoyNames.txt', 'r') as boy_names_file:
    boy_names = boy_names_file.read().splitlines()

# Запрашиваем у пользователя имена, которые он хочет проверить
boy_name = input("Введите имя мальчика: ")
girl_name = input("Введите имя девочки: ")

# Проверяем, есть ли эти имена в списке самых популярных имен
if boy_name in boy_names and girl_name in girl_names:
    print(f"Имя {boy_name} и имя {girl_name} находятся среди самых популярных имен.")
elif boy_name in boy_names:
    print(f"Имя {boy_name} находится среди самых популярных имен для мальчиков.")
elif girl_name in girl_names:
    print(f"Имя {girl_name} находится среди самых популярных имен для девочек.")
else:
    print("Введенные имена не являются самыми популярными именами.")
