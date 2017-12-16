import functools


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    # return map(char2num, s)
    return functools.reduce(fn, map(char2num, s))


if __name__ == '__main__':
    inter_number = str2int(list("123456"))
    print(inter_number, type(inter_number))

    print({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}["4"])
