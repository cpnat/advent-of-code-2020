from functools import reduce


def anyone_yes(data):

    response_set = [set(letters) for letters in data]
    response_set_union = reduce(set.union, response_set)

    return len(response_set_union)


def everyone_yes(data):

    response_set = [set(letters) for letters in data]
    response_set_intersection = reduce(set.intersection, response_set)

    return len(response_set_intersection)


def load_data(file_path):

    data = [[]]
    with open(file_path) as f:

        for line in f:
            line = line.rstrip()
            if not line:
                data.append([])
            else:
                data[-1].append(line)

        return data


if __name__ == '__main__':

    data = load_data('advent-of-code-2020/data/day_6_input.txt')

    anyone_yes = sum(anyone_yes(el) for el in data)
    print('Answer anyone yes -> {}'.format(anyone_yes))

    everyone_yes = sum(everyone_yes(el) for el in data)
    print('Answer everyone yes -> {}'.format(everyone_yes))
