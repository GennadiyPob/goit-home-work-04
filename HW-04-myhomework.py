# Task 06 
#MY WORK

# def split_list(*grade):
#     quantity = int(len(grade))                    # кількість елементів (оцінок) списку 
#     print(quantity)
#     average_grade = int(sum(grade) / quantity)    # середня оцінка: сума елементів розділена на кількість 
#     print(average_grade)
#     list_below_average = []                        # список для оцінок нижче середньої  
#     list_above_average = []                        # список для оцінок вище середньої  
    
#     for gr in grade:
#         if average_grade >= gr:
#             list_below_average.append(gr)  # елемент додаємо в список "нижче середньої" 
#         else:
#             list_above_average.append(gr)  # елемент додаємо в список "вище середньої" 
        
#     print(list_below_average)            # виводимо список оцінок нижче середньої 
#     print(list_above_average)            # виводимо список оцінок вище середньої 
  
# split_list(4,5,4,3,5,3)

# #CHATGPT
 
# def split_list(scores):
#     if not scores:
#         return [], []  # Повертаємо два порожніх списки для порожнього вхідного списку

#     average_score = sum(scores) / len(scores)
#     lower_avg_list = [score for score in scores if score <= average_score]
#     higher_avg_list = [score for score in scores if score > average_score]

#     return lower_avg_list, higher_avg_list

# #Mentor

# def split_list(grade):
#     if len(grade) == 0:  
#         return ([], [])  
#     average = sum(grade) / len(grade)  
#     over_grade = []  
#     lower_grade = []  
#     for gr in grade:  
#         if gr > average:  
#             over_grade.append(gr)  
#         else:  
#             lower_grade.append(gr)  
#     return lower_grade, over_grade  

# split_list = [4,5,3,4,5,3]
# print(split_list)

# def your_func(*args):
#     print(args)

# #your_func(1,2,3,4)  
# your_func(*[1,2,3,4])

# Task 07

points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

 
def calculate_distance(coordinates):
    if len(coordinates) <= 1:
        return 0

    total_distance = 0
    for i in range(len(coordinates) - 1):
        point_a = min(coordinates[i], coordinates[i + 1])
        point_b = max(coordinates[i], coordinates[i + 1])
        distance = points[(point_a, point_b)]
        total_distance += distance

    return total_distance

quad_coordinates = [0, 1, 3, 2, 0]
total_distance = calculate_distance(quad_coordinates)
print("Загальна відстань проліту дрона:", total_distance)
    