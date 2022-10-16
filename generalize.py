def repr_as_sum_of_pow_of(num, base):
    array = []
    num_copys = [num]
    while num_copys[-1] != 0:
        power = 0
        num_copy = num_copys[-1]
        while num_copy >= base:
            num_copy = int(num_copy / base)
            power += 1
        array.append((num_copy, base, power))
        num_copys.append(num_copys[-1] - (num_copy * (base) ** power))

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


s = repr_as_sum_of_pow_of(275, 10)
print(s)


