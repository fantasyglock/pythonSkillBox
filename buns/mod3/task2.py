a = int(input())
if a > 0:
    print(bin(a)[2::], oct(a)[2::], hex(a)[2::])
else:
    print('Неверный ввод')