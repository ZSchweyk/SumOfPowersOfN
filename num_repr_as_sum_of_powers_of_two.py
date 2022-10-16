def powers_of_two(num):
    bin_repr = [1 if char == '1' else 0 for char in list(bin(num)[2:])]
    length = len(bin_repr)
    result_str = ""
    for i, is_on in enumerate(bin_repr):
        if is_on:
            if i != 0:
                print(" + ", end="")
                result_str += " + "
            power = length - i - 1
            print(f"2^{power}", end="")
            result_str += f"2^{power}"
    return result_str


file_name = "powers_of_two.txt"

with open(file_name, "w") as f:
    f.write("")

start_num = 1
end_num = 999999
with open(file_name, "a") as f:
    while start_num < end_num + 1:
        print(start_num, end=": ")
        f.write(f"{start_num}: {powers_of_two(start_num)}\n")
        print()
        start_num += 1

