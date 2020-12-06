from __future__ import annotations

from functools import reduce
import re
from typing import Callable, Dict, List, Optional

# PASSPORT FIELDS
class PassportField:
    def __init__(self, name: str, value: Optional[str]):
        self.name = name
        self.value = value

    def present(self) -> bool:
        return self.value is not None

class Byr(PassportField):
    def validate(self):
        return self.present() and len(self.value) == 4 and (1920 <= int(self.value) <= 2002)

class Iyr(PassportField):
    def validate(self):
         return self.present() and len(self.value) == 4 and (2010 <= int(self.value) <= 2020)

class Eyr(PassportField):
    def validate(self):
         return self.present() and len(self.value) == 4 and (2020 <= int(self.value) <= 2030)

class Hgt(PassportField):
    def validate(self):
        if not self.present():
            return False

        unit = self.value[-2:]
        if unit not in {'cm', 'in'}:
            return False

        measurment = int(self.value[:-2])
        if unit == 'cm':
            return 150 <= measurment <= 193
        else:
            return 59 <= measurment <= 76

class Hcl(PassportField):
    def validate(self):
        return self.present() and re.search('#[0-9a-f]{6}$', self.value) is not None

class Ecl(PassportField):
    def validate(self):
        return self.present() and \
            self.value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

class Pid(PassportField):
    def validate(self):
        return self.present() and re.match('[0-9]{9}$', self.value) is not None

class Cid(PassportField):
    def validate(self):
        return True

# PASSPORT
class Passport:
    field_constructors = [
        ('byr', Byr), ('iyr', Iyr), ('eyr', Eyr), ('hgt', Hgt),
        ('hcl', Hcl), ('ecl', Ecl), ('pid', Pid), ('cid', Cid)
    ]
    def _parse_fields(self, raw_fields: List[str]) -> Dict[str, PassportField]:
        parsed_fields = {}
        for field in raw_fields:
            k, v = field.split(':')
            parsed_fields[k] = v

        fields = {}
        for key, con in self.field_constructors:
            if key in parsed_fields:
                fields[key] = con(key, parsed_fields[key])
            else:
                fields[key] = con(key, None)

        return fields

    def __init__(self, raw_fields: List[str]) -> None:
        self.fields = self._parse_fields(raw_fields)

    @classmethod
    def validate(cls, passport: Passport, validator: Callable[[Passport], bool]) -> bool:
        return validator(passport)

def _parse_input() -> List[Passport]:
    with open('day4/input.txt') as f:
        passports, fields = [], []
        for ln in f.readlines():
            if ln.strip() == '':
                passports.append(Passport(fields))
                fields = []
            else:
                fields.extend(ln.strip().split(' '))

        if len(fields) > 0:
            passports.append(Passport(fields))

        return passports

def part1(passports: List[Passport]) -> int:
    def validator(passport: Passport) -> bool:
        for key, field in passport.fields.items():
            if not field.present() and key != 'cid':
                return False
        return True

    return reduce(
        lambda cnt, pp: cnt + int(Passport.validate(pp, validator)),
        passports,
        0
    )

def part2(passports: List[Passport]) -> int:
    def validator(passport: Passport) -> bool:
        return reduce(
            lambda valid, field: valid and field[1].validate(),
            passport.fields.items(),
            True
        )

    return reduce(
        lambda cnt, pp: cnt + int(Passport.validate(pp, validator)),
        passports,
        0
    )


if __name__ == '__main__':
    print('AoC 2020 Day 4\n')
    passports = _parse_input()

    print('Solving part 1...')
    print(f'The answer is: {part1(passports)}\n')

    print('Solving part 2...')
    print(f'The answer is: {part2(passports)}\n')
