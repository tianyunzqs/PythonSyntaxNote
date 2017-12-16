def return_note():
    param1 = None
    # 如果param1为None，或""，或0，或{}，或[]，即为空，那么返回值为"not None"
    return param1 or "not None"


if __name__ == '__main__':
    return_note()
