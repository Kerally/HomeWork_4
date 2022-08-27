from email.contentmanager import raw_data_manager
import math
import itertools 


#1
x = int(input("Enter the first distance: "))
y = int(input("Enter the last distance: "))

# створюємо нескінченний цикл for для підрахунку днів
for i in itertools.count(start=0, step=1):
    x = x+(x*(10/100)) # додаємо 10% к/м до кожного нового дня
    if x > y:
        print("Count of days: ", i)
        break

#2
mass = [] # створюємо масив
amount = 0
mult = 1
while 0 not in mass:
    # заповнюємо масив
    mass.append(abs(int(input("Enter the number: "))))
# виводимо к-сь елементів у масиві
print("Number of elements: ", len(mass) - 1)
# видаляємо 0 з масива
mass.remove(0)

# знаходимо сумму і добуток елементів масива
for i in mass:
    amount = amount + i
    mult *= i

# виводимо суму і добуток елементів масива
print("Sum of elements: ", amount)
print("Mult of elements: ", mult)

# середнє арифметичне 
print("Average: ", sum(mass) / len(mass))

# знаходимо найбільше число в масиві і його позицію
high = mass[0]
position = 0
for i in range(len(mass)):
    if mass[i] > high:
        high_elem = mass[i]
        position = i + 1
print("Max element: ", high_elem)
print("Position: ", position)

# знаходимо кількість парних і не парних чисел #2
mass_sort = [] # второй массив
mass_sort = mass.copy() # копирую первый массив
mass_sort = sorted(mass_sort, reverse=True)
print("Max element: ", mass_sort[0])
print("Position: 1")
print("Second max element: ", mass_sort[1])
print("Position: 2")

# знаходимо кількість парних і не парних чисел #1
odd_num = 0
clear_num = 0
for i in mass:
    if i % 2 != 0:
        odd_num += 1
    if i % 2 == 0:
        clear_num += 1
print("Number of odd elements: ", odd_num)
print("Number of clear elements: ", clear_num)

# знаходимо кількість найбільших елементів
counter = 0
for i in mass:
    if i == max(mass):
        counter += 1
print("Number of high elements: ", counter)

#3
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

if A < B:
    for i in range(A , B+1):
        print(i)
if A > B:
     for i in reversed(range(B, A+1)):
         print(i)


#4
number = int(input("Enter the number until 9: "))
for i in range(1, number + 1 ):
    for j in range(1, i + 1 ):
        print( j, end = "" ) # вивід цифр
    print() # пробіли

#5
input_word = str(input("Enter the word: "))

print(input_word[3])
print(input_word[-2])
print(input_word[:5])
print(input_word[:-2])
len_word = len(input_word)
for i in range(len_word):
    if i % 2 == 0:
        print(input_word[i])
        
for i in range(len_word):
    if i % 2 != 0:
        print(input_word[i])
        
for i in range(len_word):
    if i %2 == 0:
        print(input_word[i])


#6
mass = []
counter = 0
mass_size = int(input("Enter the size: "))
# заповнюємо масив
for i in range(mass_size):
    mass.append(int(input("Enter the number: ")))
for i in range(1, len(mass) - 1):
    # знаходмимо найбільший елемент між сусідами 
    if mass[i - 1] < mass[i] > mass[i + 1]:
        counter += 1 # підраховуємо кількість чисел
print(counter)


#7
mass_1 = []
mass_2 = []
mass_3 = []
mass_4 = []
mass_size_1 = int(input("Enter the size for first massive: "))
mass_size_2 = int(input("Enter the size for second massive: "))

# заповнюємо перший масив
for i in range(mass_size_1):
    mass_1.append(int(input("Enter the number for first massive: ")))

# заповнюємо другий масив
for i in range(mass_size_1):
    mass_2.append(int(input("Enter the number for second massive: ")))

for i in mass_1:
    # знаходимо спільні 
    if i in mass_2:
        mass_3.append(i)
    # знаходимо елменти які є тільки в першому
    if i not in mass_2:
        mass_4.append(i)
# знаходимо різні елементи
for i in mass_2:
    if i not in mass_1:
        mass_4.append(i)