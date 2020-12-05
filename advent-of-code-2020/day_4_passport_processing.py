import re


class Passport:

    def __init__(self, byr, iyr, eyr, hgt, hcl, ecl, pid, cid):

        self.byr = byr  # (Birth Year)
        self.iyr = iyr  # (Issue Year)
        self.eyr = eyr  # (Expiration Year)
        self.hgt = hgt  # (Height)
        self.hcl = hcl  # (Hair Color)
        self.ecl = ecl  # (Eye Color)
        self.pid = pid  # (Passport ID)
        self.cid = cid  # (Country ID)

    def __str__(self):
        return ', '.join([self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid])

    def valid_fields(self):
        return None not in [self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid]

    def valid_byr(self):
        return 1920 <= int(self.byr) <= 2002

    def valid_iyr(self):
        return 2010 <= int(self.iyr) <= 2020

    def valid_eyr(self):
        return 2020 <= int(self.eyr) <= 2030

    def valid_hgt(self):
        if self.hgt is None: return False

        measurement_cm = self.hgt[-2:] == 'cm'
        measurement_inch = self.hgt[-2:] == 'in'
        value_is_valid = bool(re.match('[0-9]', self.hgt[:-2]))

        if (not measurement_cm and not measurement_inch) or (not value_is_valid):
            return False
        elif measurement_cm:
            return 150 <= int(self.hgt[:-2]) <= 193
        elif measurement_inch:
            return 59 <= int(self.hgt[:-2]) <= 76

    def valid_hcl(self):
        return bool(re.match('^[#][0-9a-f]{6}', self.hcl))

    def valid_ecl(self):
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def valid_pid(self):
        return bool(re.match('[0-9]{9}', self.pid))

    def valid_passport(self):

        return self.valid_fields() and \
               self.valid_byr() and \
               self.valid_iyr() and \
               self.valid_eyr() and \
               self.valid_hgt() and \
               self.valid_hcl() and \
               self.valid_ecl() and \
               self.valid_pid()

    @staticmethod
    def parse_to_passport(passport_dict):

        return Passport(
            byr=passport_dict.get('byr', None),
            iyr=passport_dict.get('iyr', None),
            eyr=passport_dict.get('eyr', None),
            hgt=passport_dict.get('hgt', None),
            hcl=passport_dict.get('hcl', None),
            ecl=passport_dict.get('ecl', None),
            pid=passport_dict.get('pid', None),
            cid=passport_dict.get('cid', None)
        )


def load_data(file_path):

    passports = []
    with open(file_path) as f:

        output_dict = {}
        for line in f:
            line = line.rstrip()
            if len(line) != 0:
                line = line.split(' ')
                output_dict = {**output_dict, **{el.split(':')[0]: el.split(':')[1] for el in line}}
            elif len(line) == 0:
                passports.append(Passport.parse_to_passport(output_dict))
                output_dict = {}
        passports.append(Passport.parse_to_passport(output_dict))

    return passports


data = load_data('advent-of-code-2020/data/day_4_input.txt')

valid_fields = sum((passport.valid_fields() for passport in data))
print('Answer valid fields -> {}'.format(valid_fields))

valid_passports = sum((passport.valid_passport() for passport in data))
print('Answer valid passports -> {}'.format(valid_passports))
