#Создаём генератор безопасных паролей

import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

# Считывание пользовательских данных:

n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()

# Настройка генерируемых паролей:

if add_digit.lower() == 'д': # добавляем цифры
    chars += digits
if add_lowercase.lower() == 'д': # добавляем строчные буквы
    chars += lowercase_letters
if add_uppercase.lower() == 'д': # добавляем прописные буквы
    chars += uppercase_letters
if add_punctuation.lower() == 'д': # добавляем специальные символы
    chars += punctuation
if remove_badsymbols.lower() == 'д': # удаляем специальные символы
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

# Функция генерации пароля:

def generate_password(length, chars):
    password = ''
    for j in range(length): # генерируем пароль
        password += random.choice(chars)
    return password

# Генерация нужного количества паролей:

for _ in range(n):
    generate_password(length, chars)