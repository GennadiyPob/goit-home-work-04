''' Лекція 25.07 '''
# my_list = [] #empty list. 
# my_list = [1, 1, 'snake', 'text', 'person', 45, 57, 568, 235, 213, -346, True, False]

# included_list = [[567, 1080], ['sony','video'], [True, 123]]

# print(included_list)

# my_list = [1, 1, 45, 57, 568, 235, 213, -346, -10, -45, 0, 100, 57]

# for elem in my_list:   # прохід по елементам списку
#     if elem <= 20:
#         print(elem)

# for elem in range(len(my_list)):  # прохід по номерам списку
#     if my_list[elem] <= 20:
#         print(my_list[elem])

# for elem in range(len(my_list)):       
#     print(my_list[elem])

#my_list = [1, 1, 45, 57, 568, None, 235, 213, -346, -10, None, -45, 0, 100, 57]

# my_list.append(16) #додає елемент в кінець списку
# print(my_list)

#print(my_list[3])

# my_list.insert(3, -100) #додає елемент перед позицією
# print(my_list)

# my_list.pop(3) #забирає елемент по ІНДЕКСУ. Якщо немає, видаляється останній
# print(my_list)

# my_list.remove(-346) #забирає елемент по ЗНАЧЕННЮ
# print(my_list)

# #ЗАМІНА ЕЛЕМЕНТА по ІНДЕКСУ

# my_list.pop(3)
# my_list.insert(3, -100)
# print(my_list)

# # Об'єднання списків
# new_list = ['look', "start"]
# my_list.extend(new_list)
# print(my_list) 

# Пошук елементів: знайти індекс елемента 
#print(my_list.index(-10))

'''Шукаємо None в списку. Видаляємо None якщо такі є'''

# my_list = [1, 1, 45, 57, 568, None, 235, 213, -346, -10, None, -45, 0, 100, 57]
# res = None
# try:
#     res = my_list.index(None)     # Перевіряємо чи є None у списку 
#     for _ in range(len(my_list)):
#         if None in my_list:
#            break 
#         res = my_list.index(None)    # Знаходимо індекс елемента None 
#         my_list.pop(res)
#         #my_list.pop(my_list.index(None))
#         print(res) 
# except ValueError:                  # Якщо немає None - виходимо 
#     print('No value in list')
# finally:
#     print(my_list)

'''Створення копії списку'''
#my_list = [1, 1, 45, 57, 568, 235, 213, -346, -10, -45, 0, 100, 57]

# new_list = my_list          #Присвоювання: зміни що будуть вноситися і в копію
# new_list = my_list.copy()   #Створення копії: зміни будуть лише в новому списку
# new_list.append(6)
# print(new_list, my_list, sep='\n')


'''Сортування'''
# sorted_list = sorted(my_list)
# print(sorted_list) 

# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)


'''Перевірка ведених данних на дублювання'''
# my_list = list()

# user_input = int(input('Enter value : '))
# while user_input != 0:
#     if user_input not in my_list:     #Чи є число в списку
#         my_list.append(user_input)
#     user_input = int(input('Enter value : '))

# print(my_list)  
# print(sorted(my_list))

'''Зрізи'''

# my_list = [1, 1, 45, 57, 568, 235, 213, -346, -10, -45, 0, 100, 57]

# print(my_list[::-1]) #обернений список. Початок з останнього

# print(my_list[-1]) # берем останній елемент. 

# print(my_list[3:]) # від 3-го елемента і до кінця

# print(my_list[:6]) # до 6-го елемента. 6 не включається.

# print(my_list[2:10]) # від 2-го до 9-го включно!

# print(my_list[2:10:2]) #від 2-го до 9-го включно через 2 елемента

# print(my_list[:6:-1]) # зворотній напрямок від останньго до 6-го включно!

# print(my_list[:]) # друк всіх елементів в звичайному порядку 


'''Словники'''

# person = {'name': 'Oleh', 'age': 22, 'phone': '38(0**)***', 'married': False}
# print(person)

# # person.update({'location': 'Ukraine, Lviv', 'lang': 'ukr'}) #Додаємо ключі і значення
# # print(person)

# new_data = {'location': 'Ukraine, Lviv', 'lang': 'ukr'}
# person.update(new_data) #Додаємо ключі і значення // Другий Спосіб
# print(person)

# person.pop('lang') #Видаляємо ключ. Значення також видаляється
# print(person)

# copy_person = person.copy()
# print(copy_person)

#Беремо значення зі словника. Якщо значення немає - виводимо значення після коми
# print(person.get('name', 'Noname'))
# print(person.get('phone', 'None'))
# print(person.get('lang', 'Undefined'))

# person = {'name': 'Oleh', 'age': 22, 'phone': '38(0**)***', 'married': False}
# #не можна зробити словник в словнику, але можна зробити список в словнику
# person.update({'secret': ['location', 'Ukraine', 'Lviv', 'lang', 'ukr']})
# print(person)
# print(person.get('secret', 'SECRET')) #Беремо значення зі словника.

# person['age'] = 100
# print(person)

# dict_a = {'Alex':12, 'Olga':10}
# dict_b = {'Boris':9, 'Dima': 10}
# dict_c = {'Ira':11, 'Vova': 6}

# #Створюємо новий словник, шляхом об'єднання трьох інших
# dict_united = dict()
# for value in (dict_a, dict_b, dict_c):
#     dict_united.update(value)
# print(dict_united)

# #Створюємо новий словник, шляхом приєднання до одного
# for value in (dict_b, dict_c):
#     dict_a.update(value)
# print(dict_a)

'''Множини 01:24'''

# my_list = [1, 1, 45, 57, 568, 235, 213, -346, -10, -45, 0, 100, 57]
# my_set = set(my_list)
# print(my_set)

# # my_set = set('Hi there')
# # print(my_set)
# my_list_new = sorted(list(my_set))
# print(my_list)
# print(my_list_new)

# #ще один коротший варіант
# print(sorted(list(set(my_list))))

'''Множини 01:31'''

my_set = {4, 6, 'Sam', 'Python', 100}
print(my_set)

my_set.add('Test')
print(my_set)

my_set.remove(6) # видаляє значення 6 з множини.
print(my_set)

my_set.discard('Test')  # видаляє значення Test з множини.
print(my_set)

'''Множини 01:37'''