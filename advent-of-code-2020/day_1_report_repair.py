def report_repair_sum_2(report):
    """
    O(N)
    """

    report_set = set(report)

    for el in report:
        if 2020 - el in report_set:
            return (2020 - el) * el

    raise ValueError('Report does not contain two elements which sum to 2020')


def report_repair_sum_3(report):
    """
    O(N^2)
    """

    report_set = set(report)

    for el1 in report:
        for el2 in report:
            if 2020 - el1 - el2 in report_set:
                return el1 * el2 * (2020 - el1 - el2)

    raise ValueError('Report does not contain three elements which sum to 2020')


def load_data(file_path):

    with open(file_path) as f:
        data = [int(line) for line in f]

    return data


if __name__ == '__main__':

    data = load_data('advent-of-code-2020/data/day_1_input.txt')

    answer_sum_2 = report_repair_sum_2(data)
    print('Answer sum 2 -> {}'.format(answer_sum_2))

    answer_sum_3 = report_repair_sum_3(data)
    print('Answer sum 3 -> {}'.format(answer_sum_3))
