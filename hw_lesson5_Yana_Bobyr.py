#Є рядок "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
#Завдання:
#1. Розбити рядок на список окремих слів;
#. Замінити в кожному слові усі голосні літери іншим символом, наприклад #
#3. Бонусне завдання: Відновити рядок зі списку, зі вже заміненими словами.

sentence = 'Мені дуже подобєаться вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'
word = sentence.split()

print(word)

char_remove = ['е', 'і', 'у', 'о', 'є', 'и', 'а', 'я']
for char in char_remove:
    sentence = sentence.replace(char, "#")

word = sentence.split()
print(word)

def word(sentence):
    for i in range(len(sentence)):
        sentence = sentence.replace(char, "#")
    for i in sentence:
        if i.upper().startswith("М"):
            print(i + "true")
        else:
            i.lower().startswith("м")
            print(i + "false")
print(sentence)

word = ''.join(sentence)
print(word)









