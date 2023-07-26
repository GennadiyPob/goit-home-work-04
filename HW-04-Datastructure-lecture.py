''' Лекція 25.07 '''
# my_list = [1, 1, 'snake', "text", 'lazy person', 45, 57, 568, 235, -346, True, False]
# #List in list
# included_list = [[567, 1080], ['snake',"text"]]

# my_list = [1, 1, 45, 57, 568, 235, 213,-346, -10, -45, 0, 100, 57]
#print(my_list[2])
# for elem in my_list:
#     print(elem)

# for elem in my_list:
#     if elem <= 20:
#         print(elem)

# for elem in range(len(my_list)):
#     if elem <= 20:
#         print(elem)

# for elem in range(len(my_list)):
#     if elem <= 20:
#         print(elem)


# my_list.append(16)
# print(my_list)




# print(my_list[3])

# my_list.insert(3, -100)
# print(my_list)

# my_list.pop(3)      #remove element based Index. If index=none - > last element
# print(my_list)

# my_list.remove(-346) #remove element based Value
# print(my_list)

# new_list = ['loop', 'start']
# my_list.extend(new_list)
# print(my_list)

#print(my_list.index(-10)) 

# my_list = [1, 1, 45, 57, 568, None, 235, 213,-346, -10, None, -45, 0, 100, 57]

# #Remove None from list
# print(my_list)
# try:
#     res = my_list.index(None)
#     for _ in range(len(my_list)):
#         #res = my_list.index(None)
#         my_list.pop(my_list.index(None))
# except ValueError:
#     print('No value in list')
# finally:
#     print(my_list)


#new_list = my_list.#copy()
# new_list = my_list
# my_list.append(6)
# print(new_list, my_list, sep='\n')

# sorted_list = sorted(my_list)
# print(sorted_list)

# my_list.sort()
# print(my_list)

# my_list.sort(reverse=True)
# print(my_list)

# my_list = list()
# user_input = int(input('Enter value'))
# while user_input != 0:
#     if user_input not in my_list:
#         my_list.append(user_input)
#     user_input = int(input('Enter value'))

# print(my_list)

#my_list
# print(my_list[::-1])
# print(my_list[-1])
# print(my_list[3:])
# print(my_list[:6])
# print(my_list[2:10:2])
# print(my_list[:6:-1])

#Списки
# person = {'name': 'Oleh', "age": 22, 'phone': '30***', 'married' : False}
# print(person)

# new_data = ({'location': 'Ukraine, Lviv', 'lang' : 'ukr'})
# person.update(new_data)

# person.pop('lang')
# print(person)

# copy_person = person.copy()
# print(copy_person)

# person.update({'secret': ['location', 'Ukraine, Lviv', 'lang' : 'ukr']})
# print(person)


# dict_a = {'Alex' : 12, 'Olga' : 13}
# dict_b = {'Boris' : 9, 'Ivan' : 10}
# dict_c = {'Ira' : 7, 'Nina' : 15}

# dict_united = dict()
# for value in (dict_a, dict_b, dict_c):
#     dict_united.update(value)
# print(dict_united)

# my_list = [1, 1, 45, 57, 568, 235, 213,-346, -10, -45, 0, 100, 57]
# #my_set = set('Hi there!')
# #print(my_set)
# my_list_new = sorted(list(my_list))
# print(my_list_new)


# my_set = {'4', '6', 'Sam', 'Python', 100}

# my_set.add('Test')
# print(my_set)

# my_set.remove(5)
# print(my_set)

# #my_set.discard('Test')
# print(my_set)



# list_data_one = [1, 1, 2, 3, 5, 8, 13, 21, 7, 5, 100]
# list_data_two = [11, 1, 21, 31, 15, 8, 13, 21, 7, 15, 101]

# print(list(set(list_data_one) & set(list_data_two)))



# list_data_one = [1, 1, 2, 3, 5, 8, 13]
# list_data_two = [11, 1, 21, 31, 15, 8]

# def unique(data):
#     return len(data) 


# my_tuple = (2, 5, 6, 7, 8, 100, 3, 566)

# print(my_tuple[3])
# print(my_tuple[2:6])

# circle = {
#     (0, 0): "Circle center"
#     (0, 1): "90"
#     (1, 0): "0 or 360"
#     (0, -1): "270"
#     (-1, 0): "180"
    
# }

# print ()

# my_string = 'Hello my little friends!'
# print(my_string)
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.startswith('Hello'))
# print(my_string.startswith('Hi'))
# print(my_string.endswith('!'))
# print(my_string.endswith('.'))

# my_string = 'Hello my LITTLE friends!'


my_list = [1]
print(type(my_list), id(my_list), my_list, sep='\t')

my_list.append(2)
print(type(my_list), id(my_list), my_list, sep='\t')

my_tuple = ('1', )
print(type(my_tuple), id(my_tuple), my_tuple, sep='\t')




from pathlib import Path

parent_folder_path = Path('.')

def parse_folder(path):
    for elements in path.iterdir():
        if elements.is_dir():
            print(f'parse_folder: This is folder - {elements.name}')
        else:
            print(f'parse_file: This is file - {elements.name}')

parse_folder(parent_folder_path)






