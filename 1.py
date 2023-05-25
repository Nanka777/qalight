sentence = 'Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення'
print(sentence.split( ))

new_sentence = sentence.replace('е', '#').replace('і', '#').replace('о','#').replace('а','#')\
    .replace('у','#').replace('и','#')
print(sentence)
print(new_sentence)