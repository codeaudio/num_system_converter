def num_system_converter(string: str, system_from=2, system_to=None):
    def from_binary(string, system_to):
        if {'2', '3', '4', '5', '6', '7', '8', '9'}.intersection(string):
            raise Exception('invalid string')
        char_digit = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F',
        }
        system_map = {
            16: 4,
            8: 3,
            4: 2,
            10: 1,
            2: 1
        }
        if system_to not in system_map:
            raise Exception('invalid system')
        nums = '8421'
        el = system_map.get(system_to)
        if el == 1:
            nums = [1] + [
                2 ** i for i in range(1, len(string))
            ]
        else:
            nums = nums[::-1][:el]
        string = string[::-1]
        result = ''
        if system_to == 10:
            result = str(sum(
                [
                    i[0]
                    for i in filter(
                    lambda x: x[1] != '0',
                    zip(nums[:len(string)], string)
                )
                ]
            )
            )
            return result
        for i in range(1, (len(string)) // el + 1):
            if i - 1 == 0:
                ind = 0
            else:
                ind = (i - 1) * el
            slice = string[ind:i * el]
            sum_res = sum(
                [
                    int(i[0])
                    for i in filter(
                    lambda x: x[1] != '0',
                    zip(nums[len(nums) - len(slice):], slice)
                )
                ]
            )
            if sum_res in char_digit:
                sum_res = char_digit.get(sum_res)
            result += str(sum_res)
        sum_res = sum(
            [
                int(i[0])
                for i in filter(
                lambda x: x[1] != '0',
                zip(nums[:len(string) - (i * el)], string[i * el:])
            )
            ]
        )
        if sum_res != 0:
            if sum_res in char_digit:
                sum_res = char_digit.get(sum_res)
            result += str(sum_res)
        return result[::-1]

    def to_binary(string, system_from):
        result = ''
        char_digit = {
            'A': 10,
            'B': 11,
            'C': 12,
            'D': 13,
            'E': 14,
            'F': 15,
        }
        if system_from != 10:
            string = string[::-1]
            num = sum([
                char_digit.get(string[i]) * (system_from ** i)
                or int(string[i]) * (system_from ** i)
                for i in range(0, len(string))
            ])
        else:
            num = int(string)
        while num / 2 != 0:
            num, divm = divmod(num, 2)
            result += str(divm)
        return result[::-1]

    if system_from == 2:
        return from_binary(string, system_to)
    else:
        if system_to == 2:
            return to_binary(string, system_from)
        return from_binary(to_binary(string, system_from), system_to)


if __name__ == '__main__':
    print(num_system_converter('AC', system_from=16, system_to=2))
    print(num_system_converter('AC', system_from=16, system_to=4))
    print(num_system_converter('AC', system_from=16, system_to=8))
    print(num_system_converter('AC', system_from=16, system_to=16))
    print(num_system_converter('AC', system_from=16, system_to=10))
    print(num_system_converter('10101100', system_from=2, system_to=4))
    print(num_system_converter('10101100', system_from=2, system_to=8))
    print(num_system_converter('10101100', system_from=2, system_to=16))
    print(num_system_converter('10101100', system_from=2, system_to=10))
