def binary_boarding(letters, min_row=0, max_row=127):

    mid = -(-(max_row - min_row) // 2)

    if min_row == max_row:
        return min_row
    elif letters[0] in ('F', 'L'):
        return binary_boarding(letters=letters[1:], min_row=min_row, max_row=max_row - mid)
    elif letters[0] in ('B', 'R'):
        return binary_boarding(letters=letters[1:], min_row=min_row + mid, max_row=max_row)


def load_data(file_path):

    with open(file_path) as f:
        return [line.rstrip() for line in f]


if __name__ == '__main__':

    data = load_data('advent-of-code-2020/data/day_5_input.txt')

    result = [binary_boarding(el[:-3], 0, 127) * 8 + binary_boarding(el[-3:], 0, 7) for el in data]
    print('Answer max seat -> {}'.format(max(result)))

    min_result, max_result, total = min(result), max(result), 0
    for i in range(min_result, max_result+1):
        total += i
    print('Answer missing seat -> {}'.format(sum(result)-total))
