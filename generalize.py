def repr_as_sum_of_pow_of(num, base):
    array = []
    portion_of_num = num
    while portion_of_num != 0:
        power = 0
        num_copy = portion_of_num
        while num_copy >= base:
            num_copy = int(num_copy / base)
            power += 1
        array.append((num_copy, base, power))
        portion_of_num = portion_of_num - (num_copy * base ** power)

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


s = repr_as_sum_of_pow_of(23, 3)
print(s)



