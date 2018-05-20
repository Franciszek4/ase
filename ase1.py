import numpy as np
import time

# x = np.random.randint(0, 1000, size=1000)
# np.random.shuffle(x)

x = np.arange(5000)
np.random.shuffle(x)

print('Przed sortowaniem bąbelkowym: ')
print(x)

start = time.time()
sorted = False

for i in range(x.size):
    sorted = True
    for j in range(x.size - 1):
        if x[j] > x[j+1]:
            temp = x[j]
            x[j] = x[j+1]
            x[j+1] = temp
            sorted = False
    if sorted is True:
        break

finish = time.time()

print('Po sortowaniu bąbelkowym: ')
print(x)
print('czas[s]: ', end='')
print(round(finish-start, 4))
np.random.shuffle(x)

print('\nPrzed sortowaniem drugim: ')
print(x)

start = time.time()
min = x.max()
min_index = None

for i in range(0, x.size):
    for j in range(i, x.size):
        if x[j] < min:
            min = x[j]
            min_index = j
    temp = x[i]
    x[i] = min
    x[min_index] = temp
    min = x.max()

finish = time.time()
print('Po sortowaniu drugim: ')
print(x)
print('czas[s]: ', end='')
print(round(finish-start, 4))


np.random.shuffle(x)


print('\nPrzed sortowaniem \'quick sort\': ')
print(x)

def quick_sort(x):
    pivot_value = x[0]
    while True:
        bigger_value_index = x.size - 1
        smaller_value_index = 0
        for i in range(0, x.size):
            if x[i] > pivot_value:
                bigger_value_index = i
                break
        for i in range(x.size - 1, -1, -1):
            if x[i] <= pivot_value:
                smaller_value_index = i
                break

        if smaller_value_index <= bigger_value_index:
            x = replace_elements(x, 0, smaller_value_index)
            if smaller_value_index >= 1:
                x[0:smaller_value_index+1] = quick_sort(x[0:smaller_value_index+1])
            if x.size - bigger_value_index > 1:
                x[bigger_value_index:x.size] = quick_sort(x[bigger_value_index:x.size])
            return x

        x = replace_elements(x, smaller_value_index, bigger_value_index)

def replace_elements(x, ind1, ind2):
    temp = x[ind1]
    x[ind1] = x[ind2]
    x[ind2] = temp
    return x

start = time.time()
x = quick_sort(x)
finish = time.time()

print('Po sortowaniu \'quick sort\': ')
print(x)
print('czas[s]: ', end='')
print(round(finish-start, 4))