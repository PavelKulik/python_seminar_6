list_in = list(map(int, input("Введите элементы массива: ").split()))
left, right = map(int, input("Введите диапозон: ").split())

list_index = []
for i in range(len(list_in)):
    if list_in[i] in range(left, right + 1):
        list_index.append(i)

print(*list_index)