#Функция вывода данных о пользователе
def user_data (*args):
    return args

print ('Введите данные пользователя: ')

#Запрос данных о пользователе
name = str (input ('Имя: '))
surname = str (input ('Фамилия: '))
burn_year = str (input ('Год рождения: '))
city = str (input ('Город проживания: '))
mail = str (input ('E-mail: '))
phone = str (input ('Телефон: '))

print (user_data (name, surname, burn_year, city, mail, phone))
