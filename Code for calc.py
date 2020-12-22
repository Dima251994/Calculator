
while True:
        first_number = float(input("Enter first number: ")) # Получаем первое число от пользователя
        second_number = float(input("Enter second number: ")) # Получаем второе число от пользователя
        choise_of_operation = input("Enter what do with numbers (plu - plussing, min- minusing, mul-mitiple, div-divided)  ") # Что сделать с числами
        break


if choise_of_operation == "plu":
    plussing = float(first_number + second_number) # Пиибавление
    print(plussing)

elif choise_of_operation == "min":
    minusing = float(first_number - second_number) # Вычисление
    print(minusing)

elif choise_of_operation == "mul":
    multiple = float(first_number * second_number) # Умножение
    print(multiple)
elif choise_of_operation == "div":
    divided  = float(first_number / second_number) # Деление
    print(divided)