class Password:
    def __init__(self, password, letter, min_count, max_count):
        self.password = password
        self.letter = letter
        self.min_count = min_count
        self.max_count = max_count

    def __str__(self):
        return ', '.join([self.password, self.letter, self.min_count, self.max_count])

    @staticmethod
    def parse_input_to_password(line):
        line_split = line.split(' ')
        line_sub_split = line_split[0].split('-')

        return Password(line_split[2].rstrip(), line_split[1][:-1], int(line_sub_split[0]), int(line_sub_split[1]))


def password_philosophy_letter_frequency(password_list):
    """
    O(NP)
    """

    valid_count = 0

    for el in password_list:
        letter_count = sum(1 for letter in el.password if letter == el.letter)
        valid_count = valid_count + 1 if el.min_count <= letter_count <= el.max_count else valid_count

    return valid_count


def password_philosophy_letter_position(password_list):
    """
    O(N)
    """

    valid_count = 0

    for el in password_list:
        min_count_pos = el.password[el.min_count - 1] == el.letter
        max_count_pos = el.password[el.max_count - 1] == el.letter
        valid_count = valid_count + 1 if min_count_pos + max_count_pos == 1 else valid_count

    return valid_count


def load_data(file_path):

    with open(file_path) as f:
        data = [Password.parse_input_to_password(line) for line in f]

    return data


if __name__ == '__main__':

    data = load_data('advent-of-code-2020/data/day_2_input.txt')

    answer_letter_frequency = password_philosophy_letter_frequency(data)
    print('Answer letter frequency -> {}'.format(answer_letter_frequency))

    answer_letter_position = password_philosophy_letter_position(data)
    print('Answer letter position -> {}'.format(answer_letter_position))

