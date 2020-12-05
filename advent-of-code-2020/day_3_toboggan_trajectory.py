from functools import reduce


def toboggan_trajectory(forest_array, right, down):
    """
    O(N)
    """

    line_length = len(forest_array[0])  # when you go past the bounds, this is used to reset to the first position

    count = 0
    for i in range(down, len(forest_array), down):
        count = count + 1 if forest_array[i][(i // down * right) % line_length] == '#' else count

    return count


def check_multiple_trajectories(data, trajectories):
    """
    O(NT)
    """
    results = [toboggan_trajectory(data, trajectory[0], trajectory[1]) for trajectory in trajectories]
    return reduce(lambda x, y: x * y, results)


def load_data(file_path):

    with open(file_path) as f:
        return [list(line.rstrip()) for line in f]


if __name__ == '__main__':

    data = load_data('advent-of-code-2020/data/day_3_input.txt')

    toboggan_trajectory_answer = toboggan_trajectory(data, 3, 1)
    print('Answer toboggan trajectory (3, 1) -> {}'.format(toboggan_trajectory_answer))

    trajectories = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    multiple_toboggan_trajectory_answer = check_multiple_trajectories(data, trajectories)
    print('Answer toboggan trajectories {} -> {}'.format(trajectories, multiple_toboggan_trajectory_answer))
