def roman_numerals_to_int(roman_numeral):
    roman_to_int_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    i = 0
    while i < len(roman_numeral):
        if i + 1 < len(roman_numeral) and roman_to_int_dict[roman_numeral[i]] < roman_to_int_dict[roman_numeral[i + 1]]:
            result += roman_to_int_dict[roman_numeral[i + 1]] - roman_to_int_dict[roman_numeral[i]]
            i += 2
        else:
            result += roman_to_int_dict[roman_numeral[i]]
            i += 1
    if int_to_roman(result) == roman_numeral:
        return result
    else:
        return None

def int_to_roman(num):
    num_to_roman_dict = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD",
                         500: "D", 900: "CM", 1000: "M"}
    result = ""
    for val, symbol in sorted(num_to_roman_dict.items(), reverse=True):
        while num >= val:
            result += symbol
            num -= val
    return result


print(roman_numerals_to_int('IIII'))
print(int_to_roman(4))

assert roman_numerals_to_int('I') == 1
assert roman_numerals_to_int('II') == 2
assert roman_numerals_to_int('III') == 3
assert roman_numerals_to_int('IV') == 4
assert roman_numerals_to_int('V') == 5
assert roman_numerals_to_int('VI') == 6
assert roman_numerals_to_int('VII') == 7
assert roman_numerals_to_int('VIII') == 8
assert roman_numerals_to_int('IX') == 9
assert roman_numerals_to_int('X') == 10
assert roman_numerals_to_int('XI') == 11
assert roman_numerals_to_int('XII') == 12
assert roman_numerals_to_int('XIII') == 13
assert roman_numerals_to_int('XIV') == 14
assert roman_numerals_to_int('XV') == 15
assert roman_numerals_to_int('XVI') == 16
assert roman_numerals_to_int('XVII') == 17
assert roman_numerals_to_int('XVIII') == 18
assert roman_numerals_to_int('XIX') == 19
assert roman_numerals_to_int('XX') == 20
assert roman_numerals_to_int('MMXXI') == 2021
assert roman_numerals_to_int('MCMXCIV') == 1994
assert roman_numerals_to_int('IIII') == None
assert roman_numerals_to_int('IXX') == None
assert roman_numerals_to_int('IL') == None
assert roman_numerals_to_int('VX') == None
