import random


def generate_password(len_pas, chars):
    return ''.join(random.sample(chars, len_pas))


def valid_answer(ans):
    list_ans = ['д', 'н', 'y', 'n']
    while ans.lower() not in list_ans:
        ans = input(f'Неверный ответ! Введите ответ из списка {list_ans}: ')
    return ans


def valid_digit(num):
    while not num.isdigit():
        num = input(f'Неверный ввод! Введите цифру : ')
    return int(num)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^'
strange_chr = 'il1Lo0O'
sansw = '(y / д - да, n / н - нет)'
chars = ''

print('Это программа для генерации паролей')
print('Укажите данные:')
count_pas = valid_digit(input('Количество паролей для генерации '))
len_pas = valid_digit(input('Длина одного пароля '))
if valid_answer(input(f'Включать ли цифры {digits}? {sansw} ').lower()) in 'yд':
    chars += digits
if valid_answer(input(f'Включать ли строчные буквы {lowercase_letters}? {sansw} ').lower()) in 'yд':
    chars += lowercase_letters
if valid_answer(input(f'Включать ли прописные буквы {uppercase_letters}? {sansw} ').lower()) in 'yд':
    chars += uppercase_letters
if valid_answer(input(f'Включать ли символы {punctuation}? {sansw} ').lower()) in 'yд':
    chars += punctuation
if valid_answer(input(f'Исключать ли неоднозначные символы {strange_chr}? {sansw} ').lower()) in 'yд':
    # for c in strange_chr: chars = chars.replace(c, '')
    chars = ''.join(s for s in chars if s not in strange_chr)

print()
print('Вот список паролей на выбор:')
print(*[generate_password(len_pas, chars) for _ in range(count_pas)], sep='\n')