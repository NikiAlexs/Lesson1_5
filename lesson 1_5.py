# списки
#food = ["apple","coconut","banana"]
#print(food[0])
#food[0] = "peach"
#print(food)
#food.append(True)
#print(food)
#food.extend(["string", 2])
#print(food)
#food.remove("peach")
#print(food)
#print("coconut" not in food)
#print(food[0:5:2])
# кортежи
tuple_ = 1,2,3,4, True, "String"
tuple_2 = (1,2,3,4)
tuple_3 = tuple([1,2,3,4])
print(tuple_)
print(tuple_2)
print(tuple_3)

# Практическое задание
immutable_var = (24, 11, 2024, 'Niki', 'Alix', True)
print(immutable_var)
#immutable_var[2] = 2025  - Кортеж не поддерживает обращение к элементам, изменить элементы кортежа не возможно.
#print(immutable_var)
mutable_list = [25, 12, 2025, 'Alexs', 'Niki', True]
print(mutable_list)
mutable_list[0] = 24
mutable_list[1] = 11
mutable_list[2] = 2024
mutable_list[3] = 'Alix'
mutable_list.append(False)
print(mutable_list)
mutable_list.remove(True)
print(mutable_list)
