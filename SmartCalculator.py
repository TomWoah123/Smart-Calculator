def compute(arr):
    subtract = False
    result = 0
    for thing in arr:
        if not thing.lstrip('-').isdigit():
            for sign in thing:
                if sign == '-':
                    subtract = not subtract
        elif not subtract:
            result += int(thing)
        else:
            result -= int(thing)
            subtract = False
    print(result)


while True:
    array = input().split()
    if len(array) == 0:
        continue
    elif len(array) == 1:
        if array[0] == '/exit':
            print('Bye!')
            break
        elif array[0] == '/help':
            print('The program calculates the sum of numbers')
        elif array[0][0] == '/':
            print('Unknown command')
        else:
            print(int(array[0]))
    else:
        compute(array)
