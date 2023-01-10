
def required_param_func(word, freq):
    print(word * freq)


required_param_func('Gen', 3)


def optional_param_func(word, add=5, freq=1):      # default value for freq is 1 if no argument was passed for freq
    print(word * (freq + add))


optional_param_func('Gen')          # can accept a function call with/without freq argument
optional_param_func('Gen', 3)
optional_param_func('Gen', freq=2)
