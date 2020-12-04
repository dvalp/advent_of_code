from __future__ import annotations

from collections import namedtuple
from typing import NamedTuple

sample_text = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

FIELDS = set("ecl pid eyr hcl byr iyr hgt".split())


def validate_passports(pp_list):
    for line in pp_list:
        yield all((field in line) for field in FIELDS)


PPField = namedtuple("PPField", "key value")


class Passport(NamedTuple):
    ecl: str
    pid: str
    eyr: str
    hcl: str
    byr: str
    iyr: str
    hgt: str
    cid: str = None

    @staticmethod
    def parse_info(pp_info: str) -> Passport:
        parsed_pp = dict(PPField(*field.split(":")) for field in pp_info.split())
        return Passport(**parsed_pp)

    @property
    def valid_byr(self):
        valid_year = 1920 <= int(self.byr) <= 2002
        valid_length = len(self.byr) == 4
        return all([valid_year, valid_length])

    @property
    def valid_iyr(self):
        valid_year = 2010 <= int(self.iyr) <= 2020
        valid_length = len(self.iyr) == 4
        return all([valid_year, valid_length])

    @property
    def valid_eyr(self):
        valid_year = 2020 <= int(self.eyr) <= 2030
        valid_length = len(self.eyr) == 4
        return all([valid_year, valid_length])

    @property
    def valid_hgt(self):
        if (unit := self.hgt[-2:]) == "cm" or unit == "in":
            if unit == "cm":
                return 150 <= int(self.hgt[:-2]) <= 193
            elif unit == "in":
                return 59 <= int(self.hgt[:-2]) <= 76
        return False

    @property
    def valid_hcl(self):
        return all([self.hcl.startswith("#"), len(self.hcl) == 7, self.hcl[1:].isalnum()])

    @property
    def valid_ecl(self):
        colors = set("amb blu brn gry grn hzl oth".split())
        return self.ecl in colors

    @property
    def valid_pid(self):
        return (len(self.pid) == 9) and self.pid.isnumeric()

    @property
    def valid_passport(self):
        return all([self.valid_byr, self.valid_iyr, self.valid_eyr, self.valid_hgt, self.valid_ecl, self.valid_hcl,
                    self.valid_pid])


def validate_all_passports(documents: list[str]):
    for document in documents:
        try:
            passport = Passport.parse_info(document)
            yield passport.valid_passport
        except TypeError:
            print("*** Failed:", document.split())
            yield False
        except Exception as e:
            print(e)
            raise e


if __name__ == '__main__':
    with open("../data/input_day04.txt", "r") as f:
        input_texts = f.read().split("\n\n")
    print("Final answer:", sum(validate_all_passports(input_texts)))

    # # print(sum(validate_passports(input_text)))
    # pp = Passport.parse_info(input_text[0])
    # print(pp)
    # print("byr:", pp.valid_byr)
    # print("iyr:", pp.valid_iyr)
    # print("eyr:", pp.valid_eyr)
    # print("hcl:", pp.valid_hcl)
    # print("ecl:", pp.valid_ecl)
    # print("pid:", pp.valid_pid)

#     invalid_passports = """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007"""
#
#     print(sum(validate_all_passports(invalid_passports.split("\n\n"))))
#
#     valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
#
#     print("Valid passports:", sum(validate_all_passports(valid_passports.split("\n\n"))))
