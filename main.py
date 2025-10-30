# #переменные
# name = 10
#
# #Типы данных
# #Integer
# name = 10
# #Float
# name = 10.01
# #int + float -> float
# #String
# name = "aadkljhfljsdhfg08359sdf"
# #str + str = strstr
# #Boolean
# #name = True/False(1/0)
#
#
# name = int("adf")
# print(type(name))


#list
# arr = [1, 2, 3]
# arr.append(4)
# print(arr[-1])
# arr[4] = 5
# print(arr[-1])


#dict
# d = {"key1": "value1", "key2": "value2"}
# d["key3"] = "value3"
# print(d.get("key4"))

# a = int(input("Введите число: "))
# if a == 1:
#     print(1)
# elif a == 2:
#     print(4)
# elif a == 3:
#     print(9)
# elif a == 4:
#     print(16)
# else:
#     print("Я не знаю")


# while True:



#range(n) -> n итераций с шагом +1 -> [0,n-1]
#range(10) -> 10 итераций с шагом +1 -> [0, 9(10-1)]
#range(n, m) -> m-n интераций с шагом +1 -> [n,m-1]
#range(10, 15) -> 5 итераций с шагом +1 -> [10, 14(15-1)]
#range(n, m, k) -> (m-n)/k + 1 итераций с шагом +k -> [n, m-1(n + k*x <= m-1)]
#range(10, 25, 5) -> 4 итерации с шагом +5 -> [10, 15, 20]

# for i in range(100):
#     print("Hello, World!")

# list1 = [5, 3, 6, 1, 7]
#for i in list1:
#     print(i)
# for i in range(len(list1)):
#     print(list1[i])
# for i, j in enumerate(list1):
#     print(f"{i} - {j}")

def quad(n):
    return n**3


while True:
    try:
        n = int(input("Введите число: "))
    except ValueError:
        print("Необходимо ввести число, а не строку!")
        continue

    print(quad(n))

#from new commit














