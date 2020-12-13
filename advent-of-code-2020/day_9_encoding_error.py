class XMAS:
    def __init__(self, sequence, preamble):
        self.sequence = sequence
        self.preamble = preamble

    def check_sequence(self):

        for i in range(self.preamble, len(self.sequence)):
            sequence_set, matching_pair = set(self.sequence[i - self.preamble: i]), False

            for j in range(i - self.preamble, i):
                # each number should be unique, so divide the target by two to ensure that j isn't double counted
                if (self.sequence[i] - self.sequence[j] in sequence_set) and (self.sequence[i]/2 != self.sequence[j]):
                    matching_pair = True
                    break

            if not matching_pair:
                return self.sequence[i]

    def check_contiguous_sequence(self):

        target = self.check_sequence()
        target_index = self.sequence.index(target)

        for i in range(0, target_index):

            start_idx, curr_sum = i, 0
            for j in range(i, target_index):

                curr_sum += self.sequence[j]

                if curr_sum == target:
                    return_sequence = self.sequence[start_idx: j+1]
                    return min(return_sequence) + max(return_sequence)

                if curr_sum > target:
                    break


def load_data(file_path):
    with open(file_path) as f:
        return [int(line.strip()) for line in f]


data = load_data('advent-of-code-2020/data/day_9_input.txt')
xmas = XMAS(data, 25)
print('Answer check sequence -> {}'.format(xmas.check_sequence()))
print('Answer check contiguous sequence -> {}'.format(xmas.check_contiguous_sequence()))
