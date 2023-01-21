import textwrap
import math


def wrap(string, max_width):
    len_string = len(string)
    j = 0
    res = ""
    end_result = []
    while (j < len_string):
        res += string[j]
        if (len(res) == max_width):
            end_result.append(res)
            res = ""
        j += 1

    sobra = len_string % max_width
    # print(sobra)
    sobra_str = string[len_string - sobra:len_string + 1]
    # print(sobra_str)
    end_result.append(sobra_str)
    # if (res != ""):
    #     while (len(res) < max_width):
    #         res += ""
    #     end_result.append(res)

    # print(end_result)
    end_string = "\n".join(end_result)
    # print(end_string)
    return end_string


if __name__ == '__main__':
    print(wrap('ACBDEFGHIJK', 4))