
def fibonacci(n):
    list = [1, 1]
    i = 0

    while (i < n - 2):
        sum = list[i] + list[i + 1]
        list.append(sum)
        i += 1

    return list


def sort(list = []):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def calc(num1, num2, sym):
    if sym == "+":
        return num1 + num2
    if sym == "-":
        return num1 - num2
    if sym == "*":
        return num1 * num2
    if sym == "/":
        return num1 / num2





