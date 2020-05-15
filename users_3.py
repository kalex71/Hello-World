import json

# читаем файл
with open('123.json', 'r') as users_db:
    users_data = users_db.read()
    users = json.loads(users_data)
print("\nПроверка сохранённого словоря\t" + str(users) + "\n")
# проверяем регистрацию
pol = input("\n введите свой номер телефона.\n")
if pol in users.keys():
    print("да есть такой пользователь")
else:
    print("\nТакого пользователя нет")

# Создание список пользователей
n_us = {}
pol = input("введите свой номер телефона.\n")
name = input("Здравствуйте!Я Ваш курьер\nвsедите Ваше имя\n")
print("Привет " + name.title() + "!")
fname = input(name.title() + ", введите свою Фамилию.\n")
gor = input(name.title() + ", где вы находитесь?\n")

n_us[pol] = {}
n_us[pol]["first"] = name
n_us[pol]["last"] = fname
n_us[pol]["location"] = gor

# записываем в файл
'''
with open("123.json", "a") as user_data:
    user_data.write(str(n_us))
'''

for username, user_info in n_us.items():
    print("\nПроверте правильно ли я всё запомнил \n")
    print("\tПользователь: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

print("\n")

