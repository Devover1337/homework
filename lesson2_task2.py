# Задача номер 2 второго урока по Python

def get_sign(x):
    if x[0] in '+-':
        return x[0]

elements = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(elements):
    sign = get_sign(elements[i])
    if elements[i].isdigit() or (sign and elements[i][1:].isdigit()):
        if sign:
            elements[i] = sign + elements[i][1:].zfill(2)
        else:
            elements[i] + elements[i].zfill(2)

        elements.insert(i, '"')
        elements.insert(i + 2, '"')
        i += 2

    i += 1
message = ' '.join(elements)

print(message)



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False



for element in elements:
    print(element, end = ' ')
    if is_number(element):
        print(" - число")
    else:
        print(" - не число")

