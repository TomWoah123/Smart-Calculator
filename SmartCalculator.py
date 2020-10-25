# write your code here

def compute(arr):
    # if isInvalidArr(arr):
    #     print("Invalid expression")
    #     return
    subtract = False
    result = 0
    for thing in arr:
        # if isInvalidExp(thing):
        #     print("Invalid expression")
        #     return
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


def isInvalidExp(exp):
    if not exp.lstrip('+-').isdigit():
        return True
    elif not exp[len(exp) - 1].isdigit():
        return True
    return False


def isOnlyPlus(exp):
    for sign in exp:
        if not sign == '+':
            return False
    return True


def isOnlyMinus(exp):
    for sign in exp:
        if not sign == '-':
            return False
    return True


def isInvalidArr(arr):
    if isOnlyPlus(arr[len(arr) - 1]) or isOnlyMinus(arr[len(arr) - 1]):
        return True
    for i in range(0, len(arr), 2):
        if i == len(arr) - 1 and isInvalidExp(arr[i]):
            return True
        if not arr[i].lstrip('+-').isdigit() and not (isOnlyPlus(arr[i + 1]) or isOnlyMinus(arr[i + 1])):
            return True
    return False

while True:
    array = input().split()
    dic = {}
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
        elif isInvalidExp(array[0]):
            print("Invalid expression")
        else:
            print(int(array[0]))
    else:
        compute(array)
