import re


def contains_gold(bags):

    containing_gold = set()

    def search_for_gold(bag_colour='shiny gold'):

        for bag in bags:
            if bag_colour in bags[bag]:
                containing_gold.add(bag)
                search_for_gold(bag)

    search_for_gold()
    return len(containing_gold)


def quantity_of_gold(bags):

    def search_for_gold(bag_colour='shiny gold'):
        count = 1
        for inner_bag in bags[bag_colour]:
            multiplier = bags[bag_colour][inner_bag]
            count += multiplier * search_for_gold(inner_bag)
        return count

    return search_for_gold() - 1


def load_data(file_path):

    with open(file_path) as f:
        return_bags = {}

        for line in f:

            line = line.replace('bags', '')
            line = line.replace('bag', '')
            line = line.replace('.', '')

            line_split = re.split(',|contain', line)
            bags = [bag.strip() for bag in line_split]

            current_bag = {}
            for bag in bags[1:]:
                if bag == 'no other':
                    return_bags[bags[0]] = {}
                    continue

                bag_parts = bag.split(' ', 1)
                current_bag[bag_parts[1]] = int(bag_parts[0])

            return_bags[bags[0]] = current_bag

    return return_bags


data = load_data('advent-of-code-2020/data/day_7_input.txt')
contains_gold_answer = contains_gold(data)
print('Answer contains gold -> {}'.format(contains_gold_answer))
quantity_of_gold_answer = quantity_of_gold(data)
print('Answer quantity of gold -> {}'.format(quantity_of_gold_answer))
