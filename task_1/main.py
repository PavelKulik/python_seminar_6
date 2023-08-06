print("Введите первый элемент, разность,оличество элементов:")
first, stap, count = map(int, input().split())

list_prog = []
for i in range(first, stap * count, stap):
    list_prog.append(i)

print(*list_prog)