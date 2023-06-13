#1. Створити функцію, що приймає число з консолі (використати фунцію input()); Функція повинна
# обробити значення таким чином: використовуючи вбудовану функцію int() спробувати конвертувати
# рядок в число (input() завжди повертає рядок). Якщо конвертувати не виходить, то вивести
#в консоль "Entered not valid data".

def integer_sent(input_string):
    try:
        integer_value = int(input_string)
        print("It is good!")
    except ValueError:
        print("Entered not valid data")

int_input = input('Введіть ціле число: ')
integer_sent(int_input)


#2. Створити функцію, що приймає 2 рядки;
#Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з 'єднуємо рядки),'
#' якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.

def line(line_1, line_2):
    try:
        value_1 = int(line_1)
        value_2 = int(line_2)
        result = value_1 + value_2
        print("Good job")
    except Exception:
        string_line = line_1 + line_2
        print("Not good", string_line)

user_input_1 = input("weight: ")
user_input_2 = input('growth: ')
line(user_input_1, user_input_2)

#3. Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа, тоді
#просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
#Коли користувач вводить число, дякуємо йому)

def integer_input():
    while True:
        try:
            user_input = int(input("Please enter an integer: "))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

# Example usage
number = integer_input()
print("You entered:", number)

#4. Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
#Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його(return)

class OnlyEvenError(Exception):
    pass
def check_digit(number):
    if number % 2 == 0:
        return number
    else:
        raise OnlyEvenError('You enter wrong number: ')

try:
    value = int(input('Enter valid number: '))
    result = check_digit(value)
    print("Your number is even:", result)
except OnlyEvenError as error:
    print('Error: ', str(error))


#5. Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit, в яку
#передавати це число. Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1.
#Інакше, помножити число на 2. Результат виводити в консоль.
#Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую". Використовувати try-except- else -finally

def check_digit(pocket):
    try:
        if not isinstance(pocket, int):
            raise TypeError("The pocket parameter must be an integer.")

        if pocket < 0:
            raise ValueError("The pocket parameter must be a non-negative integer.")

        pocket *= 2

    except Exception as e:
        print("An error occurred:", str(e))

    else:
        try:
            total = pocket + 1
            digit_sum = sum(int(digit) for digit in str(total))
            return digit_sum % 10
        except Exception as e:
            print("An error occurred during the digit sum calculation:", str(e))

    finally:
        print("Я все одно завжди щось друкую")

    return None

# Example usage
pocket_money = 4
digit = check_digit(pocket_money)
print("Check digit:", digit)