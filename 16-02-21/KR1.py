def firstEx():
    nums = [int(input('Enter next number: '))]
    while sum(nums) != 0:
        nums.append(int(input('Enter next number: ')))
    return [elem ** 2 for elem in nums]


# print(firstEx())


def secondEx():
    first_num = float(input("Input first number: "))
    second_num = float(input("Input second number: "))
    oper = input("What we will do: ")
    if oper == '+':
        return first_num + second_num
    elif oper == '-':
        return first_num - second_num
    elif oper == '/':
        return first_num / second_num
    elif oper == '*':
        return first_num * second_num
    elif oper == 'mod':
        return first_num % second_num
    elif oper == 'pow':
        return pow(first_num, second_num)
    elif oper == 'div':
        return first_num // second_num


# print(secondEx())

def thirdEx():
    i = int(input('Input words count: '))
    words = []
    while i != 0:
        words.append(input("Enter your word: "))
        i -= 1
    j = int(input('Input check words count: '))
    check = []
    while j != 0:
        check.append(input("Enter your word: ").split())
        j -= 1
    for arr in check:
        for word in arr:
            if word not in words:
                print(word)
