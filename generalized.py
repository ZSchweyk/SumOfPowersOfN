def repr_as_sum_of_pow_of(num: int, base: int):
    array = []
    portion_of_num = num
    while portion_of_num != 0:
        power = 0
        multiplier = portion_of_num
        while multiplier >= base:
            multiplier = multiplier // base
            power += 1
        array.append((multiplier, base, power))
        portion_of_num = portion_of_num - (multiplier * base ** power)

    return print_as_sum_of_powers_of(array)


def print_as_sum_of_powers_of(array):
    result = ""
    index = 0
    for multiplier, base, power in array:
        if multiplier != 0:
            if index != 0:
                result += " + "
            result += f"{multiplier}({base})^{power}"
        index += 1
    return result


s = repr_as_sum_of_pow_of(23, 7)
print(s)



