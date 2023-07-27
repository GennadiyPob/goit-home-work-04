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

my_list = [1, 1, 45, 57, 568, 235, 213, -346, -10, -45, 0, 100, 57]

print(my_list[::-1]) #обернений список. Початок з останнього

print(my_list[-1]) # берем останній елемент. 

print(my_list[3:]) # від 3-го елемента і до кінця

print(my_list[:6]) # до 6-го елемента. 6 не включається.

print(my_list[2:10]) # від 2-го до 9-го включно!

print(my_list[2:10:2]) #від 2-го до 9-го включно через 2 елемента

print(my_list[:6:-1]) # зворотній напрямок від останньго до 5-го включно!

print(my_list[:]) # друк всіх елементів в звичайному порядку 

