
#1. Створити функцію, що приймає число з консолі (використати фунцію input()); Функція повинна
# обробити значення таким чином: використовуючи вбудовану функцію int() спробувати конвертувати
# рядок в число (input() завжди повертає рядок). Якщо конвертувати не виходить, то вивести
#в консоль "Entered not valid data".

numb = int(input("Enter your number phone: "))
try:
    numb = int(input("Enter your number phone: "))
    print("Your phone is:", numb)
except KeyboardInterrupt:
    print("Entered not valid data")


#2. Створити функцію, що приймає 2 рядки;
#Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з 'єднуємо рядки),'
#' якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.

def main():
    data = {'website': 'google'}
    print(data['url'])
    summ = 1+1
    print(summ)


#3. Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа, тоді
#просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
#Коли користувач вводить число, дякуємо йому)



#4. Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
#Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його(return)
check_digit(1, 2, 3, 4)
a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print("Yes")
    else:
        print("No")
else:
    print("No")


#5. Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit, в яку
#передавати це число. Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1.
#Інакше, помножити число на 2. Результат виводити в консоль.
#Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую". Використовувати try-except- else -finally