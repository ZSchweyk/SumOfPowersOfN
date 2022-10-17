def repr_as_sum_of_pow_of(num: int, base: int):
    array = []  # save multipliers, bases, and powers respectively in a 2D array. I process the elements in this array
    # later and in a separate function.
    portion_of_num = num  # this is the portion of the number remaining after finding a multiple of the biggest unique
    # power of {base}
    while portion_of_num != 0:  # while there is still some remainder of the number that is not 0...
        power = 0  # initiate a variable that represents the number of times {base} can be divided into {num}
        multiplier = portion_of_num
        while multiplier >= base:
            multiplier = multiplier // base
            power += 1
        array.append((multiplier, base, power))
        portion_of_num = portion_of_num - (multiplier * base ** power)

    return print_as_sum_of_powers(array)


def print_as_sum_of_powers(array):
    result = ""
    index = 0
    for multiplier, base, power in array:
        if multiplier != 0:
            if index != 0:
                result += " + "
            result += f"{multiplier}({base})^{power}"
        index += 1
    return result


s = repr_as_sum_of_pow_of(9999999, 9)
print(s)



