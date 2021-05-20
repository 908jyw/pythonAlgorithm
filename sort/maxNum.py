def solution(numbers):
    l = []
    for number in numbers:
        original = str(number)
        number = list(str(number))
        i = 0
        while len(number) <= 4:
            number.append(original[i])
            i = (i + 1) % len(original)
        number = int("".join(number))
        l.append([number, original])

    # ex1. [6, 10, 2]
    # l = [[66666, '6'], [10101, '10'], [22222, '2']]
    # ex2. [3, 30, 34, 5, 9]
    # l = [[33333, '3'], [30303, '30'], [34343, '34'], [55555, '5'], [99999, '9']]

    l.sort(reverse=True)
    l = sorted(l, reverse=True)
    return str(int("".join([item[1] for item in l])))


numbers = [3, 30, 34, 5, 9]

print(solution(numbers))