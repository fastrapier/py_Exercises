from spellchecker import SpellChecker


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
    print(words)
    check = []
    while j != 0:
        words.append(str(input("Enter your word: ")))
        j -= 1
    # for word in check:
    #     print(word in words)
    print(check)


print(thirdEx())
