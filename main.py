def sum(n1, n2):
    return n1 + n2

while True:
    num1 = input("Ingrese número primer número: ")
    num2 = input("Ingrese número segundo número: ")

    try:
        value_num = suma(int(num1), int(num2))
        break
    except:
        print("Ingrese nuevamente los números.\n")
        continue

print(value_num)