def type_hint_note(name:str = "world") -> str:
    """
         类型提示（形参类型提示，返回值类型提示）
        name:str = "world"   str为形参类型提示
         -> str: str为返回值类型提示
    """
    return 'Hello ' + name


if __name__ == '__main__':
    print(type_hint_note())
