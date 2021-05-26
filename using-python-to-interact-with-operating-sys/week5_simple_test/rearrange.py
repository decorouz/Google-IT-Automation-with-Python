#!/usr/bin/env python3
# An important characteristics of unit test is isolation
import re
# rearange function


def rearrange_name(name):

    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


rearrange_name("Hamilton")


my_txt = "abcdfge"


def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    if result is None:
        return txt
    return result


print(LetterCompiler(my_txt))
