def solution1():
    f_sequence = [1, 2]  # Fibonacci sequence
    while True:
        num = f_sequence[-1] + f_sequence[-2]
        if num > 4_000_000: break
        f_sequence.append(num)

    sum = 0
    for num in f_sequence:
        if num % 2 == 0: sum += num

    print("Summary1: {}".format(sum))


def solution2():
    sum, num1, num2 = 0, 1, 2

    while num2 <= 4_000_000:
        # print(num1) # u can print the values of Fibonacci numbers (num1) in order to check whether the sequence is true
        if num2 % 2 == 0: sum += num2
        temp = num1 + num2
        num1, num2 = num2, temp

    print("Summary2: {}".format(sum))


if __name__ == '__main__':
    solution1()
    solution2()
