# Задание 1
from pyautogui import write
from pyexpat.errors import messages

# txt = input("Введите строку: ")
#
# clean_txt = txt.replace(" ", "").lower()
#
# if clean_txt == clean_txt[::-1]:
#     print("Это палиндром!")
# else:
#     print("Это не палиндром.")

# Задание 2

# text = input("Введите текст: ")
#
# reser = input("Введите зарезервированные слова: ").split()
# words = text.split()
# for i in range(len(words)):
#     if words[i] in reser:
#         words[i] = words[i].upper()
# new_text = ' '.join(words)
# print("Измененный текст:", new_text)

# Задание 3

# def count_sentences(text):
#     return text.count('.') + text.count('!') + text.count('?')
#
# text = input("Введите текст: ")
# sentence_count = count_sentences(text)
# print(f"Количество предложений в тексте: {sentence_count}")

# classwork2403

# myStr = "1234567890"
# print(myStr[2:8:2])
# print(myStr[8:2:-2])
# print(myStr[::])

# myStr = ("There is no shoryage of material to learn "
#          "Python. \n\t\tThe following books might serve")
# print(myStr)

# myStr = "\x2b"
# print(myStr)

# \\ - для отображения символа <\>


# myStr = "Jhhh '\\t' ghg hghbsd  '\\n' hgdhj"
# print(myStr)

# normalStr = r"This is a \n normal string"
# print(normalStr)

# :b - двоичная система
# :d - десятичный формат
# :o - 8-й формат
# :x - 16-й формат

# text = input("Введите текст: ")
#
# isprav = '. '.join(s.strip().capitalize() for s in '! '
#         .join(s.strip().capitalize() for s in '? '
#         .join(s.strip().capitalize() for s in
#         text.split('?')).split('!')).split('.'))
#
# dig = sum(c.isdigit() for c in text)
# znaki = sum(text.count(p) for p in '.,!?;:')
# voskl = text.count('!')
#
# print("Исправленный текст:", isprav)
# print("Цифр в тексте:", dig)
# print("Знаков препинания:", znaki)
# print("Восклицательных знаков:", voskl)

# :< - Выравнивание по левому краю
# :> - Выравнивание по правому краю
# :^ - Выравнивание по цетру

# import string
# print(string.ascii_letters)
# print(string.ascii_uppercase)
#
# import random
# import string
#
# userLogin = "".join(random.sample((string.ascii_lowercase),6))
# userPsw = "".join(random.sample((string.ascii_letters + string.digits),8))
# print(userLogin)
# print(userPsw)

# import string
#
# myStr = (" We have BEEN happy\n to welcome\n "
#          "back OLD friends, \n\n and make new ones")
# print(string.capwords(myStr))
# print()
# print(string.)
# print(myStr)

# from string import Formatter
# formatter = Formatter()
#
# print(formatter.format('{userLog}', userLog='Admin'))

# from string import Template
# t = Template('$userName has the rights to $userRights in tge $appName')
# resStr = t.substitute(userName="Admin", userRights = 'edit', appName="SuperApp")
# print(resStr)

# import re
# userStr = "abcd abc efgh"
# match = re.search(r'\w{4}', userStr)
# print(match.group())
# print(match.group(0))

# import re
# userStr='abcd abc 123 efgh 456'
# match = re.search(r'\d{3}', userStr)
# print(match.group())
# print(match.group(0))

# import re
# userStr="My cell phone numbers: Vodafone +38(095)1234457; Cellcom +38(095)1274895"
# match1 = re.search(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)(\d\d\d\d\d\d\d)',userStr)
# print(match1.group(1,2))

# import re
# userStr="2021-2022 Competition Calendar:30.11.2021 — 2021 Grand Prix Series; 14.01.2022 — Grand Pemio D'Italia"
# match2=re.findall(r'\d{2}\.\d{2}\.\d{4}', userStr)
# print(match2)

# import re
# userStr1="My cell phone numbers: Vodafone +38(095)1234567; Cellcom +38(067)9875612"
# userStr2="Vodafone +38(095)1234567; Cellcom +38(067)9875612 — my cell phone numbers"
# match3 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)'
#                   r'(\d\d\d\d\d\d\d)', userStr1)
# match4 = re.match(r'Vodafone \+38\(095\)(\d\d\d\d\d\d\d); Cellcom \+38\(067\)'
#                   r'(\d\d\d\d\d\d\d)', userStr2)
# print(match3)
# print(match4.group())

# list3 = [i * 5 for i in "abcdtf"]
# print(list3)

# customers = ['Bob', 'Pipa', 'Nikita', 'Jeka', 'Andri']
# list5 = [i for i in customers if i != 'Nikita' and i != 'Andri']
# print(list5)

# list6 = [[x * y for x in range(1,4)] for y in range (1,4)]
# print(list6, end=' ')

# myList = ['user', 12, 200.34, False, True]
# print(myList[0])
# print(myList[-2])
# print(myList[len(myList)-1])

# 31/03

# prices = [100, 250.45, 1200, 20.78]
# prices.sort(reverse=True)
# print(prices)
#
# prices = [100, 250.45, 1200, 20.78]
# prices.sort()
# print(prices)

# customers = ["Bob", "Anna", "Joi", "Bob", "Nick"]
# # print('Bob' in customers)
# if ('Bob' in customers):
#     print("Bob is our customers")
# else:
#     print('Fail')

# list1 = [1,2,3,4,5]
# list2 = list1
# list2[1]="Hello"
# print(list2)

# list1 = [1,2,3,4,5]
# list2 = list1
# list3 = [6,7,8]
#
# print(list2 is list1)
# print(list1 is list3)

# list1 = [1,2,3,4,5]
# list2 = list1.copy()
# list2[1] = "Hello"
# list3 = list(list1)
#
# list1 = list2[:]
# list1[3]="Hello"
# print(list1)

# studScore = [["Bob", 11,8,10,12],["Jane", 12,11,11,11],["Kate", 7,8,9,9]]
# for i in studScore:
#     print(i)
#
# for i in studScore:
#     print(i[0], max(i[1:]))

# Задание 1

# import random
# numbers = [random.randint(-10, 10) for _ in range(10)]
# print("Список чисел:", numbers)
#
# # 1
# otric = 0
# for num in numbers:
#     if num < 0:
#         otric += num
# print("Отрицательные", otric)
#
# # 2
# chet = 0
# for num in numbers:
#     if num % 2 == 0:
#         chet += num
# print("Чет:", chet)
#
# # 3
# nechet = 0
# for num in numbers:
#     if num % 2 != 0:
#         nechet += num
# print("Нечет:", nechet)
#
# # 4
# tri = 1
# for i in range(len(numbers)):
#     if i % 3 == 0:
#         tri *= numbers[i]
# print("Произведение крат 3:", tri)
#
# # 5
#
# minmax = min(numbers) * max(numbers)
# print("Произведение между min и max:", minmax)
#
# # 6
#
# first = -1
# last = -1
#
# for i in range(len(numbers)):
#     if numbers[i] > 0:
#         first = i
#         break
#
# for i in range(len(numbers)-1, -1, -1):
#     if numbers[i] > 0:
#         last = i
#         break
#
# sum = 0
# if first != -1 and last != -1:
#     for i in range(first + 1, last):
#         sum += numbers[i]
# print("Сумма между первым и последним положительными:", sum)

# Задание 2

# 03.04

# print("*" * 7)
# print("*" * 7)
# print("*" * 7)
# print("*" * 7)
# print("*" * 7)

# for _ in range(5):
#     print('*'*7)
# print()
# for _ in range(5):
#     print('*'*7)
# print()
# for _ in range(5):
#     print('*'*7)
# print()

# def draw_box(height, width):
#     for _ in range(height):
#         print('*' *width)
#     print()
# # draw_box(5,10)
#
# n = 10
# m = 4
#
# draw_box(n,m)

# Задание 1

# def txt():
#     print('\033[3m\"Don\'t let the noise of others\' opinions"')
#     print('drown out your own inner voice.')
#     print('\t\t\t\t\t\t\tSteve Jobs')
# txt()

# Задание 2

# def dig(a, b):
#     for num in range(a, b + 1):
#         if num % 2 != 0:
#             print(num)
# dig(3, 10)

# Задание 3

# def line(dlina, napravlenie, symbol):
#     if napravlenie == 'h':
#         print(symbol * dlina)
#     else:
#         for i in range(dlina):
#             print(symbol)
# line(5, 'h', '*')


# Задание 4

# def dig(a, b, c, d):
#     return max(a, b, c, d)
# print(max(5,4,9,10))

# Задание 5

# def a(x,y):
#     return x * y
# print(a(5,9))

# Задание 6

# def is_lucky(number):
#     n = str(number)
#     return int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5])
# print(is_lucky(123420))


# def PrintMessageWithName(name:str):
#     name = name.capitalize()
#     print("Привет", name)
# PrintMessageWithName("pAVEL")

# import random
# def Desaider() -> bool:
#     playerChoise = input("Орел или решка?").strip().lower()
#     return playerChoise =="орел"
# def IsWin(coin: int, playerChoise: bool):
#     if coin == playerChoise:
#         print("Победа")
#     else:
#         print("Поражение")
# def Main():
#     coin = random.randint(0, 1)
#     playerChoise = Desaider()
#     IsWin(coin, playerChoise)
# Main()

# import random
# coin = random.randint(0, 1)
# def IsWin (coin):
#     return coin == 1
# if IsWin(coin):
#     print("Вы выиграли!")
# else:
#     print("Вы проиграли.")

# 07/04

# def black_hole(*args):
#     print(type(args))
#     for argument in args:
#         print(argument)
# black_hole(0,5,6, "Name", "address", 2*5)

# def black_hole_named(**kwargs):
#     print(type(kwargs))
#     for argument in kwargs:
#         print(argument)
# black_hole_named(name="Nick", planet='Earth', galaxy='Milky Way', age=1010101010)

# def black_hole_named(**kwargs):
#     print(type(kwargs))
#     for key, value in kwargs.items():
#         print(key, value)
# black_hole_named(name="Nick", planet='Earth', galaxy='Milky Way', age=1010101010)

# def black_hole_full(*args, **kwargs):
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(key, value)
# black_hole_full(*1,2,3,4,"Stroka", planet="Earth", age = 13000)

# dict_1 = {"name": 'Nick', "planet":'Earth', "age":2434}
# for i in dict_1:
#     print(i[])

# def way(v, t):
#     way = v * t
#     print(way)
# way(100,30)

# list_1 = 60, 2
# print(type(list_1))
#
# dict_1 = {'t':2, 'v':60}
# def way(v, t):
#     way = v * t
#     print(way)
# way(**dict_1)

# dict_1 = {'t': 2, 'v': 60}
#
# def way(v, t):
#     ymnoz = v * t
#     dele = v / t
#     print("Умножение:", ymnoz)
#     print("Деление:", dele)
#
# way(**dict_1)

# dict_1 = {"var_3":3, "var_4":4}
# list_1 = [2]
#
# def some_func (var_1, var_2, var_3, var_4):
#     print(var_1, var_2, var_3, var_4)
# some_func(1, *list_1, **dict_1)

# import random
#
# list_of_questions = [
#     "Do you have a word that you invented yourself?",
#     "Have you ever lied about your age?",
#     "What's the biggest joke you've ever made?",
# ]
# list_of_actions = [
#     "Can't blink for a minute",
#     "Run around the house three times",
# ]
# def get_players():
#     players = []
#     while True:
#         name = input("Enter player name (2+ letters): ").strip()
#         if len(name) < 2:
#             print("Name too short!")
#             continue
#         players.append(name.capitalize())
#         if len(players) >= 2:
#             more = input("Add more players? (Y/N): ").lower()
#             if more not in ('y', 'yes'):
#                 break
#     return players
#
# def game_round(questions, actions, players):
#     for player in players:
#         print(f"\n{player}'s turn!")
#         choice = input("Question (Q) or Action (A)? ").lower()
#         if choice in ('q', 'question'):
#             if questions:
#                 item = random.choice(questions)
#                 questions.remove(item)
#                 print(f"Question: {item}")
#             else:
#                 print("No more questions left!")
#
#         elif choice in ('a', 'action'):
#             if actions:
#                 item = random.choice(actions)
#                 actions.remove(item)
#                 print(f"Action: {item}")
#             else:
#                 print("No more actions left!")
#
#         else:
#             print("Invalid choice! Do both:")
#             if questions:
#                 print(f"Question: {random.choice(questions)}")
#             if actions:
#                 print(f"Action: {random.choice(actions)}")
# def main_game():
#     players = get_players()
#     if len(players) < 2:
#         print("Need at least 2 players!")
#         return
#     questions = list_of_questions.copy()
#     actions = list_of_actions.copy()
#     while True:
#         game_round(questions, actions, players)
#         if not questions and not actions:
#             print("\nNo more questions or actions left!")
#             break
#         cont = input("\nAnother round? (Y/N): ").lower()
#         if cont not in ('y', 'yes'):
#             print("Game over!")
#             break
#         if not questions:
#             print("Adding new questions!")
#             questions = list_of_questions.copy()
#         if not actions:
#             print("Adding new actions!")
#             actions = list_of_actions.copy()
# if __name__ == "__main__":
#     main_game()

# import random
#
# list_of_question = ["У тебя есть слово, которое ты придумал сам?",
# "Ты когда-нибудь лгал о своем возрасте?",
# "Какую самую смешную шутку ты когда-либо придумывал?",
# "У тебя есть странный/особенный талант?",
# "Ты поешь в ванной?", "Как вы обманываете , пытаясь избежать помощи по дому?",
# "Вы боитесь привидений?", "Вы когда-нибудь поливали растения молоком?",
# "Вы когда-нибудь что-нибудь ломали , никому об этом не говоря?",
# "Если бы у вас была 1 минута, чтобы быстро уйти что бы вы взяли с собой из дома?"]
# list_of_action = ["Не могу моргнуть в течение минуты", "Обегите вокруг дома три раза",
# "Обнимите свой почтовый ящик (или дерево / украшение на лужайке) на 20 секунд", "Говорите, высунув язык",
# "Сделайте действие следующим игроком, чтобы выбрать категорию действия", "Отправьте передайте кому-нибудь сообщение, используя только свой нос",
# "Представьте, что вы играете на воздушной гитаре",
# "Спойте детский стишок", "Говорите и ведите себя как робот",
# "После всего, что вы говорите, добавляйте слова Вау… Я в порядке! в течение следующих 15 минут"
# ]
# gamer_list = []
#
# def gamers(list):
#     while True:
#         name = input("Введите Имя - ")
#         if 0 < len(name) <= 2:
#             continue
#         list.append(str.capitalize(name))
#         if len(list) >= 2:
#             need_next_player = input("Много игроков? - Y/N ")
#             if need_next_player == str.lower("y") or need_next_player == str.lower("yes"):
#                 continue
#             else:
#                 break
# gamers(gamer_list)
#
# def game(list_of_question, list_of_action, *args):
#     while True:
#         next_step = None
#         for gamer in args:
#             print(gamer)
#             user_choise = input("Question or Action? ")
#             if user_choise == str.lower("q") or user_choise == str.lower("question"):
#                 question_index = random.randint(0, len(list_of_question)-1)
#                 print(list_of_question[question_index])
#                 list_of_question.pop(question_index)
#             elif user_choise == str.lower("a") or user_choise == str.lower("action"):
#                 action_index = random.randint(0, len(list_of_action)-1)
#                 print(list_of_action[action_index])
#                 list_of_action.pop(action_index)
#             else:
#                 print("Do and answer")
#                 question_index = random.randint(0, len(list_of_question)-1)
#                 print(list_of_question[question_index])
#                 list_of_question.pop(question_index)
#                 action_index = random.randint(0, len(list_of_action)-1)
#                 print(list_of_action[action_index])
#                 list_of_action.pop(action_index)
#             if args[-1] == gamer:
#                 break
#             next_step = input("Next player? - Y/N ")
#             if next_step == str.lower("y") or next_step == str.lower("yes"):
#                 continue
#             else:
#                 print("Game is over")
#                 break
#         if next_step == str.lower('y') or next_step == str.lower('yes'):
#             pass
#         else:
#             break
#         select = input("New round? - Y/N ")
#         if select == str.lower("y") or select == str.lower("yes"):
#             continue
#         else:
#             break
# game(list_of_question, list_of_action, *gamer_list)

# 14\04

# import random as r
# print(r.randint(1,10))

# from random import randint as r
# print(r(1,10))

# from random import randint as r, choice as ch
# print(r(1,10))
# print(ch([1,2,3,4,56,7,8]))

# from pytes.test import numbers
# print(numbers)

# from pytes.test import *
# print(numbers)
# print(func())
# print(MyClass)

# import test
#
# def func_a():
#     test.func_b()
# class Base:
#     pass

# from calc import add,sub,mul,div,pro,ctep
#
# num1 = int(input("Enter num1"))
# num2 = int(input("Enter num2"))
#
# print(add(num1,num2))
# print(sub(num1,num2))
# print(mul(num1,num2))
# print(div(num1,num2))
# print(pro(num1,num2))
# print(ctep(num1,num2))

# Задача 4

# from random import choice
# print(choice(["😄","🤡","🤩","👽","🕵️‍♀️","👾","🤣","😱","🤠","😝"]))


# def BinarySearch(lys, val):
#     first = 0
#     last = len(lys) - 1
#     index = -1
#     while (first <= last) and (index == -1):
#         mid = (first + last) // 2
#         if lys[mid] == val:
#             index = mid
#         else:
#             if val < lys[mid]:
#                 last = mid - 1
#             else:
#                 first = mid + 1
#     return index
#
# print(BinarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 7))

# def FibonacciSearch(lys, val):
#     fibM_minus_2 = 0
#     fibM_minus_1 = 1
#     fibM = fibM_minus_1 + fibM_minus_2
#     while fibM < len(lys):
#         fibM_minus_2 = fibM_minus_1
#         fibM_minus_1 = fibM
#         fibM = fibM_minus_1 + fibM_minus_2
#
#     index = -1
#
#     while fibM > 1:
#         i = min(index + fibM_minus_2, len(lys) - 1)
#
#         if lys[i] < val:
#             fibM = fibM_minus_1
#             fibM_minus_1 = fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#             index = i
#         elif lys[i] > val:
#             fibM = fibM_minus_2
#             fibM_minus_1 = fibM_minus_1 - fibM_minus_2
#             fibM_minus_2 = fibM - fibM_minus_1
#         else:
#             return i
#     if (fibM_minus_1 and index < len(lys) and lys[index + 1] == val):
#         return index + 1
#     return -1

# def insertion_sort(alist):
#     for i in range(1, len(alist)):
#         temp = alist[i]
#         j = i - 1
#         while (j >= 0 and temp < alist[j]):
#             alist[j + 1] = alist[j]
#             j = j -1
#         alist[j + 1] = temp
#
# alist = input('Введите число:').split()
# alist = [int(x) for x in alist]
# insertion_sort(alist)
# print('Отсортированный массив: ', end='')
# print(alist)

# def merge_list(aList, start, mid, end):
#     left = aList[start:mid]
#     right = aList[mid:end]
#     k = start
#     i = 0
#     j = 0
#     while (start + i < mid and mid + j < end):
#         if (left[i] <= right[j]):
#             aList[k] = left[i]
#             i = i + 1
#     else:
#         aList[k] = right[j]
#         j = j + 1
#         k = k + 1
#     if start + i < mid:
#         while k < end:
#             aList[k] = left[i]
#             i = i + 1
#             k = k + 1
#     else:
#         while k < end:
#             aList[k] = right[j]
#             j = j + 1
#             k = k + 1
# aList = input('Введите числа: ').split()
# aList = [int(x) for x in aList]
# merge_list(aList, 0,len(aList))
# print('Отсортированный массив: ', end='')
# print(aList)


# def merge_list(aList, start, mid, end):
#     left = aList[start:mid]
#     right = aList[mid:end]
#     k = start
#     i = 0
#     j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             aList[k] = left[i]
#             i += 1
#         else:
#             aList[k] = right[j]
#             j += 1
#         k += 1
#
#     while i < len(left):
#         aList[k] = left[i]
#         i += 1
#         k += 1
#
#     while j < len(right):
#         aList[k] = right[j]
#         j += 1
#         k += 1
#
#
# def merge_sort(aList, start, end):
#     if end - start > 1:
#         mid = (start + end) // 2
#         merge_sort(aList, start, mid)
#         merge_sort(aList, mid, end)
#         merge_list(aList, start, mid, end)
#
#
# aList = input('Введите числа через пробел: ').split()
# aList = [int(x) for x in aList]
# merge_sort(aList, 0, len(aList))
# print('Отсортированный список:', aList)

# сортировка методом шелла

# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#
# data = input("Введите числа через пробел: ").split()
# data = [int(x) for x in data]
# shell_sort(data)
# print("Отсортированный массив:", data)

# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[left] > arr[largest]:
#         largest = left
#
#     if right < n and arr[right] > arr[largest]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
# def heap_sort(arr):
#     n = len(arr)
#
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#
# numbers = [12, 11, 13, 5, 6, 7]
# print("До сортировки:", numbers)
#
# heap_sort(numbers)
#
# print("После сортировки:", numbers)

# 24.04

# import time
# import random
#
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left = merge_sort(arr[:mid])
#         right = merge_sort(arr[mid:])
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 arr[k] = left[i]
#                 i += 1
#             else:
#                 arr[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             arr[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             arr[k] = right[j]
#             j += 1
#             k += 1
#     return arr
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
#
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)
#
# def heap_sort(arr):
#     def heapify(arr, n, i):
#         largest = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#         if l < n and arr[i] < arr[l]:
#             largest = l
#         if r < n and arr[largest] < arr[r]:
#             largest = r
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
#
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     return arr
#
# def shell_sort(arr):
#     n = len(arr)
#     gap = n // 2
#     while gap > 0:
#         for i in range(gap, n):
#             temp = arr[i]
#             j = i
#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap
#             arr[j] = temp
#         gap //= 2
#     return arr
#
# sizes = [500, 1000, 10000]
# test_data = {size: [random.randint(0, size) for _ in range(size)] for size in sizes}
#
# results = {size: {} for size in sizes}
# algorithms = {
#     "Пузырьковая сортировка": bubble_sort,
#     "Сортировка слиянием": merge_sort,
#     "Сортировка вставками": insertion_sort,
#     "Быстрая сортировка": quick_sort,
#     "Пирамидальная сортировка": heap_sort,
#     "Метод Шелла": shell_sort}
#
# for algo_name, algo_func in algorithms.items():
#     for size in sizes:
#         data = test_data[size].copy()
#         start_time = time.time()
#         algo_func(data)
#         execution_time = time.time() - start_time
#         results[size][algo_name] = execution_time
#
# for size in sizes:
#     sorted_results = sorted(results[size].items(), key=lambda x: x[1])
#     for idx, (algo, time_val) in enumerate(sorted_results, 1):
#         results[size][algo] = (time_val, idx)
#
# print("{:<25} {:<10} {:<10} {:<10}".format("Алгоритм", "500", "1000", "10000"))
# print("-" * 55)
# for algo in algorithms:
#     times = []
#     for size in sizes:
#         time_val, place = results[size][algo]
#         times.append(f"{time_val:.4f} (место {place})")
#     print("{:<25} {:<10} {:<10} {:<10}".format(algo, *times))

# 28/04

# my_dict = {"name": "Pavel", "age": 33, "city": "TLT"}
# print(my_dict["age"])
# my_dict["car"]="Toyota"
# print(my_dict["car"])

# castle = [1, ["c"], 543, "P", ["n", ["r"]], "i", [[["s"]]]]
# print(f'{castle[3]}{castle[4][1][0]}{castle[5]}{castle[4][0]}'
#       f'{castle[1][0]}{chr(101)}{castle[6][0][0][0]}{castle[6][0][0][0]}')

# message = [("We",),"rec",{"r":"o"},{"o":"r"},{"m1":"ded"},{"m3":["a "],
#            "m4":{"m5":"UFO"}}]
#
# abc = [
#     message[0][0],
#     message[1],
#     message[2]["r"],
#     message[3]["o"],
#     message[4]["m1"],
#     message[5]["m3"][0],
#     message[5]["m4"]["m5"]
# ]
# cod = " ".join(abc)
# print(cod)

# 05/05

# 1

# def razn(list1, list2):
#     return set(list1) - set(list2)
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# print(razn(list1, list2))

# 2

# def proverka(list1, list2):
#     return set(list1).issubset(set(list2))
# list1 = [1, 2, 3]
# list2 = [1, 2, 3, 4, 5]
# print(proverka(list1, list2))

# 3

# def unique(text):
#     letters = set()
#     for char in text.lower():
#         if char.isalpha():
#             letters.add(char)
#     return letters
# text = "Hi, World! 8854"
# result = unique(text)
# print(result)

# 4

# def dic(lst):
#     dict = {}
#     for item in lst:
#         dict[item] = dict.get(item, 0) + 1
#     return dict
# numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# print(dic(numbers))

# 5

# def povtor(list1, list2, list3):
#     return {x for x in list1 if x in list2 and x in list3}
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# c = [5, 6, 7, 8, 9]
# print(povtor(a, b, c))

# 6
# повтор второго задания
# def dupl(list1, list2):
#     for item in list1:
#         if item not in list2:
#             return False
#     return True
# list1 = [1, 2, 3]
# list2 = [1, 2, 3, 5, 4]
# print(dupl(list1, list2))

# 7

# def word(text):
#     lower_text = text.lower()
#     znaki = '!?,.'
#     clean_text = ""
#     for char in lower_text:
#         if char not in znaki:
#             clean_text += char
#     words = clean_text.split()
#     unique = set(words)
#     return unique
# text = "Привет, мир!"
# print(word(text))

# 12/05

# def process():
#     import os; os.rename('example3.txt', 'example4.txt')
#     return
# result = process()
# print(result)


# 15/05

# 1-append
# 2-хронение и упорядоченние данных
# 3-set
# 4-Редактируемость
# 5-нельзя
# 6-in
# 7-неупорядоченный набор значений
# 8-union
# 9-нет
# 10-set
# 11-tuple


# with open('1.txt', encoding='utf-8' ) as file:
#     str1 = file.read()
# print(str1)

# with open('1.txt', encoding='utf-8') as file:
#     srt1 = file.readlines()
# print(srt1)

# 16.05

# import csv
# filename = "test.csv"
# shop_list={"картофель":[2,100], "яблоки":[3,250], "морковь":[1,35]}
# with open(filename, "w", encoding="utf-8", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "weight", "price"], quoting=csv.QUOTE_ALL)
#     writer.writeheader()
#     for name, values in sorted(shop_list.items()):
#         writer.writerow(dict(name=name, weight=values[0], price=values[1]))
#
# with open (filename, 'r', encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     rows = list(reader)
# for row in rows:
#     print(row)

# import pickle
#
# filename = "test1.txt"
#
# shop_list = {"овощи":["картофель","капуста"], "бакалея":["мука"], "бюджет": 500}
# with open(filename, "wb") as file:
#     pickle.dump(shop_list, file)
#
# shop_list_2 = []
# with open(filename,"rb") as file:
#     shop_list_2 = pickle.load(file)
# print(shop_list_2)

# Задача 1

# import json
#
# data = {}
# while len(data) < 3:
#     name = input("Имя: ")
#     if name in data:
#         print("Такое имя уже есть!")
#         continue
#     age = input("Возраст: ")
#     data[name] = age
# with open('test.txt', 'w') as f:
#     json.dump(data, f)

# Задача 2

# n = int(input("Введите количество дел: "))
# spisok = [input(f"Дело {i+1}: ") for i in range(n)]
#
# with open('dela.txt', 'w') as f:
#     f.write(' '.join(spisok[::2]))

# Задача 1

words = open('bad.txt').read().split()
text = open('in.txt').read()
for word in words:
    text = text.replace(word, '***')
open('out.txt', 'w').write(text)

# Задача 2



# Задача 3

# with open('объединенный.txt', 'w') as result:
#     while True:
#         имя = input("Введите имя файла (или quit): ")
#         if имя == 'quit':
#             break
#         result.write(open(имя).read() + '\n')

# Задача 4

# files = []
# while (f := input("Файл: ")) != 'quit': files.append(f)
#
# common = set(open(files[0]).read()) if files else set()
# for f in files[1:]: common &= set(open(f).read())
#
# open('common.txt', 'w').write(''.join(common))

# Задача 1

# with open('input.txt') as f_in, open('output.txt', 'w') as f_out:
#     text = f_in.read()
#     long_words = [word for word in text.split() if len(word) >= 7]
#     f_out.write(' '.join(long_words))

# Задача 2

# with open('input.txt', 'r', encoding='utf-8') as source:
#     with open('output.txt', 'w', encoding='utf-8') as target:
#         for line in source:
#             target.write(line)

# Задача 3

# with open('input.txt', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
# with open('output.txt', 'w', encoding='utf-8') as f:
#     f.writelines(reversed(lines))

# 22.05

