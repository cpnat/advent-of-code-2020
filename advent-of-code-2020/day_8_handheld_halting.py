class Game:
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator, self.valid_instructions = self.run()

    def run(self):
        visited_instructions = set()
        accumulator = 0
        current_index = 0

        while current_index not in visited_instructions and current_index < len(self.instructions):

            visited_instructions.add(current_index)

            if self.instructions[current_index][0] == 'acc':
                accumulator += self.instructions[current_index][1]

            if self.instructions[current_index][0] == 'jmp':
                current_index += self.instructions[current_index][1]
            else:
                current_index += 1

        return accumulator, current_index == len(self.instructions)


def accumulator_before_infinite_loop(instructions):
    return Game(instructions).accumulator


def try_fix(current_instructions, instruction, index):

    inverse_instruction = 'nop' if instruction == 'jmp' else 'jmp'
    current_instructions[index] = [inverse_instruction, current_instructions[index][1]]
    game = Game(current_instructions)
    return {'valid': game.valid_instructions, 'accumulator': game.accumulator}


def fixed_instruction_set(instructions):

    for index, instruction in enumerate(instructions):

        if instruction[0] == 'acc':
            continue

        fixed = try_fix(instructions.copy(), instruction[0], index)
        if fixed['valid']:
            return fixed['accumulator']


def load_data(file_path):
    return_instructions = []
    with open(file_path) as f:
        for line in f:
            line_split = line.strip().split(' ')
            return_instructions.append([line_split[0], int(line_split[1])])

    return return_instructions


data = load_data('advent-of-code-2020/data/day_8_input.txt')
accumulator_before_infinite_loop_answer = accumulator_before_infinite_loop(data)
print('Answer accumulator before infinite loop -> {}'.format(accumulator_before_infinite_loop_answer))
fixed_instruction_set_answer = fixed_instruction_set(data)
print('Answer fixed instruction set accumulator -> {}'.format(fixed_instruction_set_answer))
