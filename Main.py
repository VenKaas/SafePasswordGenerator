#Создаём генератор безопасных паролей

import random
import string

# Константы для генерации пароля
DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
chars = ''

# Считывание данных
count_password = int(input('Укажите количество паролей: '))
length_password = int(input('Укажите длину пароля: '))
include_digits = input('Включать цифры? (y/n):').strip()
include_high_letters = input('Включать буквы? (y/n):').strip()
include_low_letters = input('Включать строчные буквы? (y/n):').strip()
include_punctuation = input('Включать знаки? (y/n):').strip()
exclude_unusual = input('Исключать необычные символы? (y/n):').strip()

# Сценарии генарации пароля
if include_digits == 'y':
    chars += DIGITS
if include_high_letters == 'y':
    chars += UPPERCASE_LETTERS
if include_low_letters == 'y':
    chars += LOWERCASE_LETTERS
if include_punctuation == 'y':
    chars += PUNCTUATION
if exclude_unusual == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

# Генерация пароля
for _ in range(count_password):
    password = ''
    for _ in range(length_password):
        password += random.choice(chars)
    print(password)

